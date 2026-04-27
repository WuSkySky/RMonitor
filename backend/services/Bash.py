import asyncio
import fcntl
import pty
import os

class Bash:
    def __init__(self):
        self.pid, self.fd = pty.fork()
        self.reader = asyncio.StreamReader()

        # 子进程中变量 pid 为 0, 父进程中变量 pid 为子进程的 PID
        if self.pid == 0:
            os.execvp("bash", ["bash"])
        
        # 设置非阻塞
        fcntl.fcntl(self.fd, fcntl.F_SETFL, fcntl.fcntl(self.fd, fcntl.F_GETFL) | os.O_NONBLOCK)

        # 获取事件循环
        loop = asyncio.get_running_loop()

        # 创建 StreamReaderProtocol 并将其与 StreamReader 关联
        protocol = asyncio.StreamReaderProtocol(self.reader)

        # 回调函数，当文件描述符可读时将数据读入 StreamReader
        def on_readable():
            data = os.read(self.fd, 4096)
            protocol.data_received(data)
        loop.add_reader(self.fd, on_readable)

    def send(self, data):
        """
        向 bash 发送数据
        param
            data: bytes
        """
        os.write(self.fd, data)
    
    async def read(self):
        """
        从 bash 读取数据
        return
            bytes
        """
        return await self.reader.read(4096)
