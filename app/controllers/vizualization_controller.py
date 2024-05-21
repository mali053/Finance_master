from fastapi import APIRouter, HTTPException
from app.services import visualization_service

visualization_router = APIRouter()


@visualization_router.get("/expense_and_revenue_by_date")
async def get_expense_and_revenue_by_date(user_id: str):
    """
    Endpoint to generate a graph showing expenses and revenues over time for a specific user.
    Args:
        user_id (int): The ID of the user.
    Raises:
        HTTPException: If there is an error during the process.

    Returns:
        None
    """
    try:
        await visualization_service.expense_and_revenue_by_date(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@visualization_router.get("/balance-over-time")
async def get_balance_over_time(user_id: str):
    """
    Endpoint to generate a graph showing the balance over time for a specific user.
    Args:
        user_id (int): The ID of the user.
    Raises:
        HTTPException: If there is an error during the process.
    Returns:
        None
    """
    try:
        await visualization_service.balance_over_time(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@visualization_router.get("/expense-distribution-by-category")
async def get_expense_distribution_by_category(user_id: str):
    """
    Endpoint to generate a pie chart showing the distribution of expenses by category for a specific user.
    Args:
        user_id (int): The ID of the user.
    Raises:
        HTTPException: If there is an error during the process.
    Returns:
        None
    """
    try:
        await visualization_service.expense_distribution_by_category(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@visualization_router.get("/monthly_summary")
async def monthly_summary(user_id: str):
    """
    Endpoint to generate a bar chart showing the monthly summary of revenues and expenses for a specific user.
    Args:
        user_id (int): The ID of the user.
    Returns:
        None
    """
    try:
        await visualization_service.monthly_summary(user_id)
    except Exception as e:
        raise e
