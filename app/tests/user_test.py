import asyncio
import datetime
import unittest
from datetime import datetime
import pytz
import pytest
from app.controllers import user_controller
from app.models.user import User
from unittest.mock import patch


@pytest.mark.asyncio
class TestHH(unittest.TestCase):
    def test_sign_up(self):
        user = User(id='123123123', user_name="aaa", password="S@sw.1fdfg", email="user@example.com",
                    phone="053-4198051", birth_date="2000-05-28T14:48:54.574Z", balance=100)
        result = asyncio.run(user_controller.add_user(user))
        assert result == "You have successfully registered❤️❤️"

    @pytest.mark.asyncio
    def test_login(self):
        email = "user@example.com"
        password = "123Aaa$$$"
        result = asyncio.run(user_controller.login(email, password))
        assert result == {"_id": {"$oid": "664a430fda425d96c43168f3"},
                          "id": "325962801",
                          "user_name": "MALI",
                          "password": "123Aaa$$$",
                          "email": "user@example.com",
                          "phone": "053-4198051",
                          "birth_date": {
                              "$date": "2004-03-12T14:20:37.583Z"
                          },
                          "balance": 9557
                          }

    @pytest.mark.asyncio
    def test_update_user(self):
        user = User(
            id='123123123',
            user_name="mali",
            password="S@sw.1fdfg",
            email="user@example.com",
            phone="053-4198051",
            birth_date=datetime(2000, 5, 28, 14, 48, 54, 574000, tzinfo=pytz.UTC),
            balance=100
        )

        expected_response = {
            "id": "123123123",
            "user_name": "mali",
            "password": "S@sw.1fdfg",
            "email": "user@example.com",
            "phone": "053-4198051",
            "birth_date": datetime(2000, 5, 28, 14, 48, 54, 574000, tzinfo=pytz.UTC),
            "balance": 100
        }
        result = asyncio.run(user_controller.update_user("123123123", user))
        assert result == expected_response

    @pytest.mark.asyncio
    def test_delete_user(self):
        user_id = "369369369"
        expected_response = {
            "id": "369369369",
            "user_name": "aaa",
            "password": "S@sw.1fdfg",
            "email": "user@example.com",
            "phone": "053-4198051",
            "birth_date": datetime(2000, 5, 28, 14, 48, 54, 574000, tzinfo=pytz.UTC),
            "balance": 10
        }
        result = asyncio.run(user_controller.delete_user(user_id))
        assert result == expected_response
