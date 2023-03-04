from typing import Optional, Any, Union

from ..models.users import UserModel
from ..core.database import DynamoDB
from .auth import AuthService
from ..utils.response import HttpResponse as Rs

db = DynamoDB(UserModel)


async def get_pk_from_token(token: str) -> Union[str, Any]:
    decode = AuthService.verify_token(token)
    if decode:
        return decode["pk"]
    return None


async def get_user_by_email_or_username(user_id: str) -> dict:
    if "@" in user_id:
        user = await db.query(pk=user_id, index_name="email_index")
    else:
        user = await db.query(pk=user_id, index_name="username_index")
    if user:
        return {"success": True, "body": user[0]}
    return {"success": False, "msg": "User not found"}


async def get_all_user() -> Rs:
    try:
        users = await db.scan()
        for x in users:
            x["access_tokens"] = x["access_tokens"].attribute_values
        return Rs.success(data=users)
    except Exception as e:
        return Rs.server_error(e.__str__())
