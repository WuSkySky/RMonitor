from fastapi import APIRouter
import base64
import asyncio
from backend.services.Bash import Bash
from backend.services.WebSocketManger import on_ws_message, ws_send

# 陆游
router = APIRouter()

bash = Bash() 

@on_ws_message('1')
async def msg_callback(data):
    data_bytes=base64.b64decode(data)
    bash.send(data_bytes)

async def bash_to_frontend():
    while True:
        data = (await bash.read())
        data_str=base64.b64encode(data).decode("utf-8")
        await ws_send('1', data_str)

task_bash_to_frontend = asyncio.create_task(bash_to_frontend())