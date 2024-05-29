import json

from bson import json_util

from app.database import repository
from app.database.database_connection import Collections
from app.log import log_decorator
from app.models.expense import Expense
from app.models.revenue import Revenue
from app.services import balance_service


@log_decorator('app.log')
async def get_revenues(user_id: str):
    """
    Retrieve all revenues from the database for a specific user.
    Args:
        user_id (str): The ID of the user whose revenues will be retrieved.
    Returns:
        list: A list of revenue documents from the database.
    Raises:
        Exception: If there is an error during the retrieval process.
    """
    try:
        revenues = await repository.get_all(Collections.revenues)
        filtered_revenues = [revenue for revenue in revenues if revenue.get('userId') == user_id]
        return filtered_revenues
    except Exception as e:
        raise e


@log_decorator('app.log')
async def get_revenue_by_id(revenue_id: int, user_id: str):
    """
    Retrieve a revenue entry by its ID.
    Args:
        revenue_id (int): The ID of the revenue entry to retrieve.
        user_id (str): The ID of the user who owns the revenue.
    Returns:
        dict: The revenue document if found.
    Raises:
        ValueError: If the revenue entry is not found.
        Exception: If there is an error during the retrieval process.
    """
    try:
        revenue = await repository.get_by_id(Collections.revenues, revenue_id)
        if user_id == revenue['userId']:
            return revenue
        raise ValueError('you try get revenue of another user')
    except Exception as e:
        raise e


@log_decorator('app.log')
async def add_revenue(new_revenue: Revenue):
    """
    Add a new revenue entry to the database.
    Args:
        new_revenue (Revenue): The revenue object to add.
    Returns:
        dict: The added revenue document.
    Raises:
        ValueError: If the revenue object is null or the revenue ID already exists.
        Exception: If there is an error during the addition process.
    """
    if new_revenue is None:
        raise ValueError("Expense object is null")
    revenues = await repository.get_all(Collections.revenues)
    max_item = max(revenues, key=lambda item: item['id'])
    new_revenue.id = max_item['id']+1
    try:
        print(new_revenue)
        await balance_service.change_balance(new_revenue.userId, new_revenue.amount)
        return await repository.add(Collections.revenues, new_revenue.dict())
    except ValueError as ve:
        raise ValueError(ve)
    except Exception as e:
        raise e


@log_decorator('app.log')
async def update_revenue(revenue_id: int, new_revenue: Revenue):
    """
    Update an existing revenue entry's data.
    Args:
        revenue_id (int): The ID of the revenue entry to update.
        new_revenue (Revenue): The updated revenue object.
    Returns:
        dict: The updated revenue document.
    Raises:
        ValueError: If the revenue object is null or the revenue entry is not found.
        Exception: If there is an error during the update process.
    """
    if new_revenue is None:
        raise ValueError("Revenue object is null")
    existing_revenue = await get_revenue_by_id(revenue_id, new_revenue.userId)
    if existing_revenue is None:
        raise ValueError("Revenue not found")
    print(existing_revenue['amount'])
    existing_revenue = Revenue(**existing_revenue)
    new_revenue.id = existing_revenue.id
    try:
        print(new_revenue.amount)
        print(existing_revenue.amount)
        await balance_service.change_balance(new_revenue.userId, new_revenue.amount - existing_revenue.amount)
        return await repository.update(Collections.revenues, revenue_id, new_revenue.dict())
    except ValueError as ve:
        raise ValueError(ve)
    except Exception as e:
        raise e


@log_decorator('app.log')
async def delete_revenue(revenue_id: int, user_id: str):
    """
    Delete a revenue entry from the database.
    Args:
        revenue_id (int): The ID of the revenue entry to delete.
        user_id (str): The ID of the user who owns the revenue.
    Returns:
        dict: The deleted revenue document.
    Raises:
        ValueError: If the revenue entry is not found.
        Exception: If there is an error during the deletion process.
    """
    existing_revenue = await get_revenue_by_id(revenue_id, user_id)
    if existing_revenue is None:
        raise ValueError("Expense not found")
    existing_revenue = Revenue(**existing_revenue)
    try:
        await balance_service.change_balance(existing_revenue.userId, existing_revenue.amount * -1)
        return await repository.delete(Collections.revenues, revenue_id)
    except ValueError as ve:
        raise ValueError(ve)
    except Exception as e:
        raise e
