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
    Retrieves details about all revenues from the database.
    Args:
        user_id (int): The ID of the user.
    Returns:
        list: A list of dictionaries, each representing a revenue entry.
    Raises:
        HTTPException: If an error occurs while fetching revenues from the database.
    """
    try:
        revenues = await revenue_service.get_revenues(user_id)
        return json.loads(json_util.dumps(revenues))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@revenue_router.get('/{revenue_id}')
async def get_revenue_by_id(revenue_id: int, user_id: str):
    """
    Retrieves details about a specific revenue entry by its ID from the database.
    Args:
        revenue_id (int): The ID of the revenue entry to retrieve.
        user_id (int): The ID of the user.
    Returns:
        dict: A dictionary representing the revenue entry.
    Raises:
        HTTPException: If the specified revenue ID is not found or if an error occurs.
    """
    try:
        revenue = await revenue_service.get_revenue_by_id(revenue_id, user_id)
        return json.loads(json_util.dumps(revenue))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@revenue_router.post('')
async def add_revenue(new_revenue: Revenue):
    """
    Adds a new revenue entry to the database.
    Args:
        new_revenue (Revenue): An instance of the Revenue class representing the revenue entry to be added.
    Returns:
        dict: A dictionary representing the newly added revenue entry.
    Raises:
        HTTPException: If an error occurs while adding the revenue entry.
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
    Updates an existing revenue entry in the database.
    Args:
        revenue_id (int): The ID of the revenue entry to update.
        new_revenue (Revenue): An instance of the Revenue class representing the revenue entry to be updated.
    Returns:
        dict: A dictionary representing the updated revenue entry.
    Raises:
        HTTPException: If the specified revenue ID is not found or if an error occurs.
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
    Deletes an existing revenue entry from the database.
    Args:
        revenue_id (int): The ID of the revenue entry to delete.
    Returns:
        dict: A dictionary representing the deleted revenue entry.
    Raises:
        HTTPException: If the specified revenue ID is not found or if an error occurs.
    """
    try:
        deleted_revenue = await revenue_service.delete_revenue(revenue_id, user_id)
        return json.loads(json_util.dumps(deleted_revenue))
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))