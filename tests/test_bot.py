import pytest
from aiogram.types import Message
from bot.main import dp, bot

@pytest.mark.asyncio
async def test_start_message():
    message = Message(message_id=1, text="/start", chat={"id": 123})
    
    from bot.main import start
    await start(message)
