import aiohttp
from datetime import datetime
from functools import partial
import json
import logging

from telethon import TelegramClient
from telethon.events.raw import Raw

from config import settings

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(settings.LOGGING_LEVEL)


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        else:
            super(self).default(o)


async def send_data(data):
    event = {"event": data, "sourcetype": "_json"}
    token = f"Splunk {settings.HEC_TOKEN}"
    headers = {"Authorization": token}
    async with aiohttp.ClientSession(
        json_serialize=partial(json.dumps, cls=CustomJsonEncoder)
    ) as session:
        async with session.post(url=settings.HEC_SPLUNK_URL, json=event, headers=headers) as resp:
            resp_data = await resp.json()
            if resp.status != 200 or resp_data.get("code") != 0:
                logger.error(resp_data)


client = TelegramClient("monigram", settings.TELEGRAM_APP_ID, settings.TELEGRAM_APP_HASH)


@client.on(Raw())
async def event_handler(event):
    logger.debug("Handle event: %s", event)
    await send_data(event.to_dict())


if __name__ == "__main__":
    client.start(bot_token=settings.TELEGRAM_BOT_TOKEN)
    client.run_until_disconnected()
