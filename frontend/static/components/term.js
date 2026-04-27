// 创建终端实例
const term = new Terminal();

// 创建ws
const ws_term = new WebSocket("ws://localhost:8000/ws/term");

// 挂载到 div
term.open(document.getElementById('terminal'));

// 设置为二进制类型
ws_term.binaryType = "arraybuffer";

// ws接收回调
ws_term.onmessage = (event) => {
    const data_uint8 = new Uint8Array(event.data);
    term.write(data_uint8);
};

// terminal 输入回调
term.onData((data) => {
    console.log('用户输入:', data);
    ws_term.send(data);
});

