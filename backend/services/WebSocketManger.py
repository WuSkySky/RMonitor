from fastapi import APIRouter, WebSocket
import asyncio

router = APIRouter()

listeners = {}

send_data = asyncio.Queue()

# 提供的接口 注册接收到数据后调用的回调函数 装饰器
def on_ws_message(id: str):
    def decorator(func):
        listeners[id] = func
        return func
    return decorator

# 提供的接口 发送数据 coroutine function
async def ws_send(id: str, data):
    await send_data.put({'id': id, 'data': data})

@router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()

    # 前端发送到后端
    async def frontend_to_backend():
        while True:
            msg = await ws.receive_json()

            id = msg.get("id")
            data = msg.get("data")

            await listeners.get(id)(data)
            print('aaa')

    task_frontend_to_backend = asyncio.create_task(frontend_to_backend())

    # 后端发送到前端
    async def backend_to_frontend():
        while True:
            msg = await send_data.get()
            await ws.send_json(msg)
        
    task_backend_to_frontend = asyncio.create_task(backend_to_frontend())

    # 等待两个任务完成(永远不会完成, 保持函数不返回)
    await asyncio.wait([task_frontend_to_backend, task_backend_to_frontend])