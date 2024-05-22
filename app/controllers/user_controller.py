import json
from bson import json_util
from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.services import user_service

user_router = APIRouter()


@user_router.get('')
async def get_users():
    """
    Retrieves details about all users from the database.
    Returns:
        list: A list of dictionaries, each representing a user.
    Raises:
        HTTPException: If an error occurs while fetching users from the database.
    """
    try:
        users = await user_service.get_user()
        return json.loads(json_util.dumps(users))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@user_router.get('/{user_id}')
async def get_user_by_id(user_id: str):
    """
       Retrieves details about a specific user by their ID from the database.
       Args:
           user_id (int): The ID of the user to retrieve.
       Returns:
           dict: A dictionary representing the user.
       Raises:
           HTTPException: If the specified user ID is not found or if an error occurs.
       """
    try:
        user = await user_service.get_user_by_id(user_id)
        return json.loads(json_util.dumps(user))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred while fetching user: {e}")


@user_router.post('/')
async def add_user(new_user: User):
    """
       Adds a new user to the database.
       Args:
           new_user (User): An instance of the User class representing the user to be added.
       Returns:
           dict: A dictionary representing the newly added user.
       Raises:
           HTTPException: If an error occurs while adding the user.
       """
    try:
        return await user_service.add_user(new_user)
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.put('/{user_id}')
async def update_user(user_id: str, updated_data: User):
    """
     Updates an existing user in the database.
     Args:
         user_id (int): The ID of the user to update.
         new_user (User): An instance of the User class representing the user to be updated.
     Returns:
         dict: A dictionary representing the updated user.
     Raises:
         HTTPException: If the specified user ID is not found or if an error occurs.
         :param user_id:
         :param updated_data:
     """
    try:
        return await user_service.update_user(user_id, updated_data)
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.delete('/{user_id}')
async def delete_user(user_id: str):
    """
      Deletes an existing user from the database.
      Args:
          user_id (str): The ID of the user to delete.
      Returns:
          dict: A dictionary representing the deleted user.
      Raises:
          HTTPException: If the specified user ID is not found or if an error occurs.
      """
    try:
        deleted_user = await user_service.delete_user(user_id)
        return json.loads(json_util.dumps(deleted_user))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred while deleting user: {e}")
