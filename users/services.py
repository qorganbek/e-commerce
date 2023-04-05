import random
import uuid
from typing import Protocol, OrderedDict

from django.core.cache import cache
from rest_framework_simplejwt import tokens

from . import repos, models


class UserServicesInterface(Protocol):

    def create_user(self, data: OrderedDict) -> dict: ...

    def verify_user(self, data: OrderedDict) -> models.CustomUser | None: ...

    def create_token(self, data: OrderedDict) -> dict: ...

    def verify_token(self, data: OrderedDict) -> dict: ...


class UserServicesV1:
    user_repos: repos.UserReposInterface = repos.UserReposV1()

    def verify_user(self, data: OrderedDict) -> models.CustomUser | None:
        user_data = cache.get(data['session_id'])

        if not user_data:
            return

        if data['code'] != user_data['code']:
            return

        print("this is verify")
        user = self.user_repos.create_user(
            data={'email': user_data['email'], 'phone_number': user_data['phone_number']})
        self._send_letter_to_email(email=user.email)

    def create_user(self, data: OrderedDict) -> dict:
        session_id = self._verify_phone_number(data=data)

        return {
            "session_id": session_id
        }

    def verify_token(self, data: OrderedDict) -> dict:
        session = cache.get(data['session_id'])

        if not session:
            return

        if session['code'] != data['code']:
            return

        user = self.user_repos.get_user(data={'phone_number': session['phone_number']})
        access = tokens.AccessToken.for_user(user=user)
        refresh = tokens.RefreshToken.for_user(user=user)

        return {
            "access": str(access),
            "refresh": str(refresh)
        }

    def create_token(self, data: OrderedDict) -> dict:
        session_id = self._verify_phone_number(data=data)

        return {
            "session_id": session_id
        }

    def _verify_phone_number(self, data: OrderedDict) -> str:
        user = self.user_repos.get_user(data=data)
        code = self._generate_code()
        session_id = self._generate_session_id()
        cache.set(session_id, {'code': code, 'phone_number': str(user.phone_number)}, timeout=300)
        self._send_code_to_phone_number(code, data['phone_number'])
        return session_id

    @staticmethod
    def _send_letter_to_email(email: str) -> None:
        print(f'created account at email: {email}')

    @staticmethod
    def _send_code_to_phone_number(code: str, phone_number: str) -> None:
        print(f'Code: {code} to send {phone_number}')

    @staticmethod
    def _generate_code(length: int = 4) -> str:
        numbers = [str(x) for x in range(10)]
        return ''.join(random.choices(numbers, k=length))

    @staticmethod
    def _generate_session_id() -> str:
        return str(uuid.uuid4())
