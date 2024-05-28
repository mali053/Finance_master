import asyncio
import unittest
from datetime import datetime

import pytest
import pytz

from app.controllers import revenue_controller
from app.models.revenue import Revenue


@pytest.mark.asyncio
class TestHH(unittest.TestCase):
    def test_get_revenue_by_id(self):
        expected_response = {
            "_id": {
                "$oid": "664d1f0dce18655edd996695"
            },
            "id": 11,
            "userId": "325962801",
            "amount": 500,
            "date": {
                "$date": "2004-05-21T22:23:55.084Z"
            },
            "benefactor": "string",
            "documentation": "string"
        }
        result = asyncio.run(revenue_controller.get_revenue_by_id(11, "325962801"))
        assert result == expected_response

    def test_add_revenue(self):
        revenue = Revenue(id=20, userId='325962801', amount=100, date="2000-05-28T14:48:54.574Z", benefactor="mali",
                          documentation="payment on the work")
        result = asyncio.run(revenue_controller.add_revenue(revenue))
        assert result == "The income has been added successfully😘😘"

    def test_update_revenue(self):
        revenue = Revenue(id=20,
                          userId='325962801',
                          amount=150,
                          date=datetime(2000, 5, 28, 14, 48, 54, 574000, tzinfo=pytz.UTC),
                          benefactor="mali",
                          documentation="payment on the work")

        expected_response = {
            "id": 23,
            "userId": "325962801",
            "amount": 150.0,
            "date": datetime(2000, 5, 28, 14, 48, 54, 574000, tzinfo=pytz.UTC),
            "benefactor": "mali",
            "documentation": "payment on the work"
        }
        result = asyncio.run(revenue_controller.update_revenue(23, revenue))
        assert result == expected_response

    def test_delete_revenue(self):
        expected_response = {
            "_id": {
                "$oid": "665649a163de9b3da9526763"
            },
            "id": 25,
            "userId": "325962801",
            "amount": 100.0,
            'date': {'$date': '2000-05-28T14:48:54.574Z'},
            "benefactor": "mali",
            "documentation": "payment on the work"
        }
        result = asyncio.run(revenue_controller.delete_revenue(25, "325962801"))
        assert result == expected_response

