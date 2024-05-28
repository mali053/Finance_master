import json
from bson import json_util
from fastapi import APIRouter, HTTPException

from app.models.expense import Expense
from app.models.revenue import Revenue
from app.services import expense_service, revenue_service

revenue_router = APIRouter()


@revenue_router.get('')
async def get_revenues(user_id: str):
    """
    Retrieves details about all expenses from the database.
    Returns:
        list: A list of dictionaries, each representing an expense entry.
    Raises:
        HTTPException: If an error occurs while fetching expenses from the database.
    """
    try:
        revenues = await revenue_service.get_revenues(user_id)
        return json.loads(json_util.dumps(revenues))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@revenue_router.get('/{revenue_id}')
async def get_revenue_by_id(revenue_id: int, user_id: str):
    """
    Retrieves details about a specific expense entry by its ID from the database.
    Args:
        expense_id (int): The ID of the expense entry to retrieve.
    Returns:
        dict: A dictionary representing the expense entry.
    Raises:
        HTTPException: If the specified expense ID is not found or if an error occurs.
        :param user_id:
        :param revenue_id:
    """
    try:
        revenue = await revenue_service.get_revenue_by_id(revenue_id, user_id)
        return json.loads(json_util.dumps(revenue))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@revenue_router.post('')
async def add_revenue(new_revenue: Revenue):
    """
    Adds a new expense entry to the database.
    Args:
        new_expense (Expense): An instance of the Expense class representing the expense entry to be added.
    Returns:
        dict: A dictionary representing the newly added expense entry.
    Raises:
        HTTPException: If an error occurs while adding the expense entry.
        :param new_revenue:
    """
    try:
        revenue = await revenue_service.add_revenue(new_revenue)
        return "The income has been added successfully😘😘"
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@revenue_router.put('/{revenue_id}')
async def update_revenue(revenue_id: int, new_revenue: Revenue):
    """
    Updates an existing expense entry in the database.
    Args:
        expense_id (int): The ID of the expense entry to update.
        new_expense (Expense): An instance of the Expense class representing the expense entry to be updated.
    Returns:
        dict: A dictionary representing the updated expense entry.
    Raises:
        HTTPException: If the specified expense ID is not found or if an error occurs.
        :param new_revenue:
        :param revenue_id:
    """
    try:
        return await revenue_service.update_revenue(revenue_id, new_revenue)
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@revenue_router.delete('/{revenue_id}')
async def delete_revenue(revenue_id: int, user_id: str):
    """
    Deletes an existing expense entry from the database.
    Args:
        expense_id (int): The ID of the expense entry to delete.
    Returns:
        dict: A dictionary representing the deleted expense entry.
    Raises:
        HTTPException: If the specified expense ID is not found or if an error occurs.
        :param user_id:
        :param revenue_id:
    """
    try:
        deleted_revenue = await revenue_service.delete_revenue(revenue_id, user_id)
        return json.loads(json_util.dumps(deleted_revenue))
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))