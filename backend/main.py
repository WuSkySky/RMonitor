from fastapi import FastAPI
from backend.services.WebSocketManger import router as web_socket_manger_router
from backend.routers.bash import router as bash_router

app = FastAPI()

# 引入陆游
app.include_router(web_socket_manger_router) # web socket manger
app.include_router(bash_router) # bash

# @app.websocket("/ws/text")
# async def websocket_endpoint(ws: WebSocket):
#     await ws.accept()
#     while True:
#         await ws.send_text(f"[{datetime.datetime.now()}] Hello RMonitor!")
#         await asyncio.sleep(0.001)