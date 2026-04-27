from fastapi import APIRouter
from fastapi import WebSocket
import asyncio
from backend.services.Bash import Bash

# 陆游
router = APIRouter()

# websocket
@router.websocket("/ws/term")
async def websocket_endpoint(ws: WebSocket):
    bash = Bash()

    # bash.create_bash_process()

    # 等待websocket连接建立
    await ws.accept()

    # 前端输入发送到bash
    async def frontend_to_bash():
        while True:
            data = await ws.receive_text()
            print("RECV:\t ", repr(data))
            bash.send(data.encode())

    task_frontend_to_bash = asyncio.create_task(frontend_to_bash())

    # bash输出发送到前端
    async def bash_to_frontend():
        while True:
            data = (await bash.read())
            print("BASH:\t ", data.decode())
            await ws.send_bytes(data)

    task_bash_to_frontend = asyncio.create_task(bash_to_frontend())

    # 等待两个任务完成(永远不会完成, 保持函数不返回)
    await asyncio.wait([task_frontend_to_bash, task_bash_to_frontend])