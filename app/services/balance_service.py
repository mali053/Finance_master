from app.models.user import User
from app.services import user_service


async def change_balance(user_id: int, difference: float):
    """
    Adjusts the balance of a user by a specified difference.
    Args:
        user_id (int): The ID of the user whose balance will be updated.
        difference (int): The amount to adjust the user's balance by.
    Returns:
        None
    Raises:
        Exception: If there is an error retrieving or updating the user.
    """
    try:
        existing_user = await user_service.get_user_by_id(user_id)
        new_user = User(**existing_user)
        new_user.balance += difference
        await user_service.update_user(user_id, new_user)
    except Exception as e:
        raise e