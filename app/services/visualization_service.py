import matplotlib.pyplot as plt
import pandas as pd

from app.services import expense_service, revenue_service, user_service


async def expense_and_revenue_by_date(user_id: str):
    """
    Generate a graph showing expenses and revenues over time for a specific user.

    Args:
        user_id (int): The ID of the user.

    Raises:
        Exception: If there is an error during the process.

    Returns:
        None
    """
    try:
        expenses = await expense_service.get_expenses(user_id)
        revenues = await revenue_service.get_revenues(user_id)
        expenses = sorted(expenses, key=lambda expense: expense['date'])
        expense_dates = [expense['date'] for expense in expenses]
        expense_amounts = [expense['amount'] for expense in expenses]
        revenues = sorted(revenues, key=lambda revenue: revenue['date'])
        revenue_dates = [revenue['date'] for revenue in revenues]
        revenue_amounts = [revenue['amount'] for revenue in revenues]

        print(expense_amounts)

        plt.figure(figsize=(10, 6))
        plt.plot(expense_dates, expense_amounts, 'o-', label='Expenses')
        plt.plot(revenue_dates, revenue_amounts, 'o-', label='Revenues')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title(f'Revenues & Expenses for User ID = {user_id}')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()

    except Exception as e:
        raise e


async def balance_over_time(user_id: str):
    """
    Generate a graph showing the balance over time for a specific user.
    Args:
        user_id (int): The ID of the user.
    Raises:
        Exception: If there is an error during the process.
    Returns:
        None
    """
    try:
        user = await user_service.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        expenses = await expense_service.get_expenses(user_id)
        revenues = await revenue_service.get_revenues(user_id)
        dates = sorted(list(set([expense['date'] for expense in expenses] + [revenue['date'] for revenue in revenues])))
        balance = user['balance']
        balances = [0.0]
        for date in dates:
            for expense in expenses:
                if expense['date'] == date:
                    balance -= expense['amount']
            for revenue in revenues:
                if revenue['date'] == date:
                    balance += revenue['amount']
            balances.append(balance)
        dates.insert(0, dates[0])
        plt.figure(figsize=(10, 6))
        plt.plot(dates, balances, 'o-', label='Balance')
        plt.xlabel('Date')
        plt.ylabel('Balance')
        plt.title(f'Balance Over Time for User ID = {user_id}')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()

    except Exception as e:
        raise e


async def expense_distribution_by_category(user_id: str):
    """
    Generate a pie chart showing the distribution of expenses by category for a specific user.

    Args:
        user_id (int): The ID of the user.

    Raises:
        Exception: If there is an error during the process.

    Returns:
        None
    """
    try:
        expenses = await expense_service.get_expenses(user_id)
        categories = {}
        for expense in expenses:
            category = expense['beneficiary']
            amount = expense['amount']
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

        labels = categories.keys()
        sizes = categories.values()

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(f'Expense Distribution by Category for User ID = {user_id}')
        plt.axis('equal')
        plt.show()

    except Exception as e:
        raise e


async def monthly_summary(user_id: str):
    """
    Generate a bar chart showing the monthly summary of revenues and expenses for a specific user.
    Args:
        user_id (int): The ID of the user.
    Raises:
        Exception: If there is an error during the process.
    Returns:
        None
    """
    try:
        expenses = await expense_service.get_expenses(user_id)
        revenues = await revenue_service.get_revenues(user_id)
        expense_df = pd.DataFrame(expenses)
        revenue_df = pd.DataFrame(revenues)
        expense_df['date'] = pd.to_datetime(expense_df['date'])
        revenue_df['date'] = pd.to_datetime(revenue_df['date'])
        expense_df['month'] = expense_df['date'].dt.to_period('M')
        revenue_df['month'] = revenue_df['date'].dt.to_period('M')
        monthly_expenses = expense_df.groupby('month')['amount'].sum()
        monthly_revenues = revenue_df.groupby('month')['amount'].sum()
        df = pd.DataFrame({
            'Expenses': monthly_expenses,
            'Revenues': monthly_revenues
        }).fillna(0)
        df.plot(kind='bar', figsize=(10, 6))
        plt.title(f'Monthly Summary for User ID = {user_id}')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.show()

    except Exception as e:
        raise e