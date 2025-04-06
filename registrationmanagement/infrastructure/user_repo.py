from core.utils.types import Error
from registrationmanagement.models import User
from registrationmanagement.utils.types import UserType


class UserRepo:
    @staticmethod
    def create_user(data: dict) -> tuple[UserType, Error]:
        try:
            user = User.objects.create_user(**data)
            return user, None
        except Exception as e:
            return None, str(e)
