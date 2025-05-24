from fastapi import APIRouter, Depends, status, HTTPException, Request

from uuid import UUID


from app.v1.schemas.users.user import UserCreate, UserResponse, UserUpdate, UserListResponse, LoginForm

user_router = APIRouter(prefix="/users", tags=["User Related Endpoint"])

@user_router.post("", status_code=status.HTTP_201_CREATED)
async def register_user(request: UserCreate):
    pass


@user_router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(data: LoginForm):
    pass


@user_router.put("/me", status_code=status.HTTP_200_OK)
async def update_current_user(data: UserUpdate):
    pass

@user_router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(data: UserUpdate, user_id: UUID):
    pass


@user_router.get("", status_code=status.HTTP_200_OK)
async def get_all_users():
    pass

@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_one_user(user_id: UUID):
    pass


@user_router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id):
    pass


@user_router.delete("{user_id}/delete", status_code=status.HTTP_204_NO_CONTENT)
async def hard_delete_user(user_id):
    """
    This will delete the user permanently delete a user from the database.

    :param user_id: the ID of the user to be deleted
    :return: null
    """
    pass


@user_router.delete("{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id):
    """
    This will soft-delete a user, which means the user will still exist on the database but to will only be filtered when it's needed by the admin.
    :param user_id:
    :return:
    """
    pass

