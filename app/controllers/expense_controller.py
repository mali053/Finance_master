import json
from bson import json_util
from fastapi import APIRouter, HTTPException

from app.models.expense import Expense
from app.services import expense_service

expense_router = APIRouter()


@expense_router.get('')
async def get_expenses(user_id: str):
    """
        Retrieves details about all expenses for a specific user from the database.
        Args:
            user_id (str): The ID of the user whose expenses are to be retrieved.
        Returns:
            list: A list of dictionaries, each representing an expense entry.
        Raises:
            HTTPException: If an error occurs while fetching expenses from the database.
        """
    try:
        expenses = await expense_service.get_expenses(user_id)
        return json.loads(json_util.dumps(expenses))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@expense_router.get('/{expense_id}')
async def get_expense_by_id(expense_id: int, user_id: str):
    """
      Retrieves details about a specific expense entry by its ID from the database.
      Args:
          expense_id (int): The ID of the expense entry to retrieve.
          user_id (str): The ID of the user who owns the expense entry.
      Returns:
          dict: A dictionary representing the expense entry.
      Raises:
          HTTPException: If the specified expense ID is not found or if an error occurs.
      """
    try:
        expense = await expense_service.get_expense_by_id(expense_id, user_id)
        return json.loads(json_util.dumps(expense))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@expense_router.post('')
async def add_expense(new_expense: Expense):
    """
    Adds a new expense entry to the database.
    Args:
        new_expense (Expense): An instance of the Expense class representing the expense entry to be added.
    Returns:
        str: A confirmation message indicating the expense has been successfully added.
    Raises:
        HTTPException: If an error occurs while adding the expense entry.
    """
    try:
        expense = await expense_service.add_expense(new_expense)
        return "The expense has been successfully added👼👻"
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.put('/{expense_id}')
async def update_expense(expense_id: int, new_expense: Expense):
    """
       Updates an existing expense entry in the database.
       Args:
           expense_id (int): The ID of the expense entry to update.
           new_expense (Expense): An instance of the Expense class representing the expense entry to be updated.
       Returns:
           dict: A dictionary representing the updated expense entry.
       Raises:
           HTTPException: If the specified expense ID is not found or if an error occurs.
       """
    try:
        return await expense_service.update_expense(expense_id, new_expense)
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@expense_router.delete('/{expense_id}')
async def delete_expense(expense_id: int, user_id: str):
    """
       Deletes an existing expense entry from the database.
       Args:
           expense_id (int): The ID of the expense entry to delete.
           user_id (str): The ID of the user who owns the expense entry.
       Returns:
           dict: A dictionary representing the deleted expense entry.
       Raises:
           HTTPException: If the specified expense ID is not found or if an error occurs.
       """
    try:
        deleted_expense = await expense_service.delete_expense(expense_id, user_id)
        return json.loads(json_util.dumps(deleted_expense))
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))