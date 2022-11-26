from fastapi import APIRouter, Request, Depends
from ...auth import AuthBearer
from ...utils.response import Response as Rs
from ..cognito import Be3UserDashboard

router = APIRouter(prefix="/user/dashboard", tags=["User-Dashboard"])
m = Be3UserDashboard()


@router.post("/delete/{email}", dependencies=[Depends(AuthBearer())])
async def cognito_delete_user(email: str):
    try:
        signup = m.delete_user(email)
        if signup['success']:
            return Rs.success(signup, "User deleted successfully")
        return Rs.error(signup, "User not deleted")
    except Exception as e:
        return Rs.error(e.__str__())


@router.post("/sign-out", dependencies=[Depends(AuthBearer())])
async def user_sign_out(request: Request):
    try:
        access_token = request.headers['Authorization'].split(' ')[1]
        response = m.sign_out(access_token)
        return Rs.success(response, "User logged out successfully")
    except Exception as e:
        return Rs.error(e.__str__())