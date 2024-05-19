from fastapi import HTTPException

from app.database import repository
from app.database.database_connection import Collections
from app.models.user import User


async def get_user():
    """
      Retrieve all users from the database.
      Returns:
          list: A list of user documents from the database.
      Raises:
          Exception: If there is an error during the retrieval process.
      """
    try:
        return await repository.get_all(Collections.users)
    except Exception as e:
        raise e


async def get_user_by_id(user_id: str):
    """
        Retrieve a user by their ID.
        Args:
            user_id (int): The ID of the user to retrieve.
        Returns:
            dict: The user document if found.
        Raises:
            ValueError: If the user is not found.
            Exception: If there is an error during the retrieval process.
        """
    try:
        user = await repository.get_by_id(Collections.users, user_id)
        if not user:
            raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
        return user
    except Exception as e:
        raise e


async def add_user(new_user: User):
    """
       Add a new user to the database.
       Args:
           new_user (User): The user object to add.
       Returns:
           dict: The added user document.
       Raises:
           ValueError: If the user object is null or the user ID already exists.
           Exception: If there is an error during the addition process.
       """
    try:
        return await repository.add(Collections.users, new_user.dict())
    except Exception as e:
        raise e


async def update_user(user_id: str, updated_data: User):
    """
       Update an existing user's data.
       Args:
           user_id (int): The ID of the user to update.
           new_user (User): The updated user object.
       Returns:
           dict: The updated user document.
       Raises:
           ValueError: If the user object is null or the user is not found.
           Exception: If there is an error during the update process.
       """
    try:
        return await repository.update(Collections.users, user_id, updated_data.dict())
    except Exception as e:
        raise e


async def delete_user(user_id: str):
    """
     Delete a user from the database.
     Args:
         user_id (int): The ID of the user to delete.
     Returns:
         dict: The deleted user document.
     Raises:
         ValueError: If the user is not found.
         Exception: If there is an error during the deletion process.
     """
    try:
        return await repository.delete(Collections.users, user_id)
    except Exception as e:
        raise e
