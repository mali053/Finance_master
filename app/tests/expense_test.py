import asyncio
import unittest
from datetime import datetime

import pytest
import pytz

from app.controllers import revenue_controller, expense_controller
from app.models.expense import Expense
from app.models.revenue import Revenue


@pytest.mark.asyncio
class TestHH(unittest.TestCase):
    """
    A test suite for the expense-related functionality in the expense_controller.
    Each test is designed to verify the correct behavior of a specific function in the expense_controller.
    """

    def test_get_expense_by_id(self):
        """
        Test retrieving an expense entry by its ID.

        This test ensures that the get_expense_by_id function returns the correct expense entry
        when provided with a valid expense ID and user ID.

        Expected behavior:
            - The function should return the expense entry matching the provided ID and user ID.
        """
        expected_response = {
            "_id": {
                "$oid": "6654a9ce127d643d15c38f3e"
            },
            "id": 16,
            "userId": "325962801",
            "amount": 320,
            "date": {
                "$date": "2024-05-27T15:41:49.252Z"
            },
            "beneficiary": "string",
            "documentation": "string"
        }
        result = asyncio.run(expense_controller.get_expense_by_id(16, "325962801"))
        assert result == expected_response

    def test_add_expense(self):
        """
        Test adding a new expense entry.

        This test ensures that the add_expense function correctly adds a new expense entry
        and returns a success message.

        Expected behavior:
            - The function should add the new expense entry and return a confirmation message.
        """
        expense = Expense(id=20, userId='325962801', amount=100, date="2000-05-28T14:48:54.574Z", beneficiary="mali",
                          documentation="payment on the work")
        result = asyncio.run(expense_controller.add_expense(expense))
        assert result == "The expense has been successfully added👼👻"

    def test_update_expense(self):
        """
        Test updating an existing expense entry.

        This test ensures that the update_expense function correctly updates an existing expense entry
        and returns the updated expense entry.

        Expected behavior:
            - The function should update the specified expense entry and return the updated details.
        """
        expense = Expense(id=20,
                          userId='325962801',
                          amount=150,
                          date=datetime(2000, 5, 28, 14, 48, 54, 574000, tzinfo=pytz.UTC),
                          beneficiary="mali b",
                          documentation="payment on the work")

        expected_response = {
            "id": 17,
            "userId": "325962801",
            "amount": 150.0,
            "date": datetime(2000, 5, 28, 14, 48, 54, 574000, tzinfo=pytz.UTC),
            "beneficiary": "mali b",
            "documentation": "payment on the work"
        }
        result = asyncio.run(expense_controller.update_expense(17, expense))
        assert result == expected_response

    def test_delete_expense(self):
        """
        Test deleting an expense entry by its ID.

        This test ensures that the delete_expense function correctly deletes the specified expense entry
        and returns the details of the deleted entry.

        Expected behavior:
            - The function should delete the specified expense entry and return its details.
        """
        expected_response = {
            "_id": {
                "$oid": "665655198a59df43fd56be02"
            },
            "id": 17,
            "userId": "325962801",
            "amount": 150,
            "date": {
                "$date": "2000-05-28T14:48:54.574Z"
            },
            "beneficiary": "mali b",
            "documentation": "payment on the work"
        }
        result = asyncio.run(expense_controller.delete_expense(17, "325962801"))
        assert result == expected_response
