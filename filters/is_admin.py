from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsAdmin(BaseFilter):
    def __init__(self, user_ids: list) -> None:
        self.user_ids = user_ids

    async def __call__(self, message: Message) -> bool:
        return str(message.from_user.id) in self.user_ids