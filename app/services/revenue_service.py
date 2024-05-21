from app.database import repository
from app.database.database_connection import Collections
from app.models.expense import Expense
from app.models.revenue import Revenue
from app.services import balance_service


async def get_revenues(user_id: str):
    """
    Retrieve all expenses from the database.
    Returns:
        list: A list of expense documents from the database.
    Raises:
        Exception: If there is an error during the retrieval process.
    """
    try:
        revenues = await repository.get_all(Collections.revenues)
        filtered_revenues = [revenue for revenue in revenues if revenue.get('userId') == user_id]
        return filtered_revenues
    except Exception as e:
        raise e


async def get_revenue_by_id(revenue_id: int):
    """
    Retrieve an expense entry by its ID.
    Args:
        expense_id (int): The ID of the expense entry to retrieve.
    Returns:
        dict: The expense document if found.
    Raises:
        ValueError: If the expense entry is not found.
        Exception: If there is an error during the retrieval process.
        :param revenue_id:
    """
    try:
        return await repository.get_by_id(Collections.revenues, revenue_id)
    except Exception as e:
        raise e


async def add_revenue(new_revenue: Revenue):
    """
    Add a new expense entry to the database.
    Args:
        new_expense (Expense): The expense object to add.
    Returns:
        dict: The added expense document.
    Raises:
        ValueError: If the expense object is null or the expense ID already exists.
        Exception: If there is an error during the addition process.
        :param new_revenue:
    """
    if new_revenue is None:
        raise ValueError("Expense object is null")
    if await get_revenue_by_id(new_revenue.id) is not None:
        raise ValueError("Expense ID already exists")
    try:
        print(new_revenue)
        await balance_service.change_balance(new_revenue.userId, new_revenue.amount)
        return await repository.add(Collections.revenues, new_revenue.dict())
    except ValueError as ve:
        raise ValueError(ve)
    except Exception as e:
        raise e


async def update_revenue(revenue_id: int, new_revenue: Revenue):
    """
    Update an existing expense entry's data.
    Args:
        expense_id (int): The ID of the expense entry to update.
        new_expense (Expense): The updated expense object.
    Returns:
        dict: The updated expense document.
    Raises:
        ValueError: If the expense object is null or the expense entry is not found.
        Exception: If there is an error during the update process.
        :param new_revenue:
        :param revenue_id:
    """
    if new_revenue is None:
        raise ValueError("Revenue object is null")
    existing_revenue = await get_revenue_by_id(new_revenue.id)
    if existing_revenue is None:
        raise ValueError("Revenue not found")
    print(existing_revenue['amount'])
    existing_revenue = Revenue(**existing_revenue)
    try:
        print(new_revenue.amount)
        print(existing_revenue.amount)
        await balance_service.change_balance(new_revenue.userId, new_revenue.amount - existing_revenue.amount)
        return await repository.update(Collections.revenues, revenue_id, existing_revenue.dict())
    except ValueError as ve:
        raise ValueError(ve)
    except Exception as e:
        raise e


async def delete_revenue(revenue_id: int):
    """
    Delete an expense entry from the database.
    Args:
        expense_id (int): The ID of the expense entry to delete.
    Returns:
        dict: The deleted expense document.
    Raises:
        ValueError: If the expense entry is not found.
        Exception: If there is an error during the deletion process.
        :param revenue_id:
    """
    existing_revenue = await get_revenue_by_id(revenue_id)
    if existing_revenue is None:
        raise ValueError("Expense not found")
    existing_revenue = Revenue(**existing_revenue)
    try:
        await balance_service.change_balance(existing_revenue.userId, existing_revenue.amount * 1)
        return await repository.delete(Collections.revenues, revenue_id)
    except ValueError as ve:
        raise ValueError(ve)
    except Exception as e:
        raise e