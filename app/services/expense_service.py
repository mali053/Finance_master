from app.database import repository
from app.database.database_connection import Collections
from app.log import log_decorator
from app.models.expense import Expense
from app.services import balance_service


@log_decorator('app.log')
async def get_expenses(user_id: str):
    """
    Retrieve all expenses from the database.
    Returns:
        list: A list of expense documents from the database.
    Raises:
        Exception: If there is an error during the retrieval process.
    """
    try:
        expenses = await repository.get_all(Collections.expenses)
        filtered_expenses = [expense for expense in expenses if expense.get('userId') == user_id]
        return filtered_expenses
    except Exception as e:
        raise e


@log_decorator('app.log')
async def get_expense_by_id(expense_id: int, user_id: str):
    """
    Retrieve an expense entry by its ID.
    Args:
        expense_id (int): The ID of the expense entry to retrieve.
    Returns:
        dict: The expense document if found.
    Raises:
        ValueError: If the expense entry is not found.
        Exception: If there is an error during the retrieval process.
        :param expense_id:
        :param user_id:
    """
    try:
        expense = await repository.get_by_id(Collections.expenses, expense_id)
        if user_id == expense['userId']:
            return expense
        raise ValueError('you try get expense of another user')
    except Exception as e:
        raise e


@log_decorator('app.log')
async def add_expense(new_expense: Expense):
    """
    Add a new expense entry to the database.
    Args:
        new_expense (Expense): The expense object to add.
    Returns:
        dict: The added expense document.
    Raises:
        ValueError: If the expense object is null or the expense ID already exists.
        Exception: If there is an error during the addition process.
    """
    if new_expense is None:
        raise ValueError("Expense object is null")
    expenses = await repository.get_all(Collections.expenses)
    max_item = max(expenses, key=lambda item: item['id'])
    new_expense.id = max_item['id'] + 1
    try:
        await balance_service.change_balance(new_expense.userId, new_expense.amount * -1)
        return await repository.add(Collections.expenses, new_expense.dict())
    except ValueError as ve:
        raise ValueError(ve)
    except Exception as e:
        raise e


@log_decorator('app.log')
async def update_expense(expense_id: int, new_expense: Expense):
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
    """
    if new_expense is None:
        raise ValueError("Expense object is null")
    existing_expense = await get_expense_by_id(expense_id, new_expense.userId)
    if existing_expense is None:
        raise ValueError("Expense not found")
    existing_expense = Expense(**existing_expense)
    new_expense.id = existing_expense.id
    try:
        await balance_service.change_balance(new_expense.userId, existing_expense.amount - new_expense.amount)
        return await repository.update(Collections.expenses, expense_id, new_expense.dict())
    except ValueError as ve:
        raise ValueError(ve)
    except Exception as e:
        raise e


@log_decorator('app.log')
async def delete_expense(expense_id: int, user_id: str):
    """
    Delete an expense entry from the database.
    Args:
        expense_id (int): The ID of the expense entry to delete.
    Returns:
        dict: The deleted expense document.
    Raises:
        ValueError: If the expense entry is not found.
        Exception: If there is an error during the deletion process.
        :param expense_id:
        :param user_id:
    """
    existing_expense = await get_expense_by_id(expense_id, user_id)
    if existing_expense is None:
        raise ValueError("Expense not found")
    existing_expense = Expense(**existing_expense)
    try:
        await balance_service.change_balance(existing_expense.userId, existing_expense.amount)
        return await repository.delete(Collections.expenses, expense_id)
    except ValueError as ve:
        raise ValueError(ve)
    except Exception as e:
        raise e
