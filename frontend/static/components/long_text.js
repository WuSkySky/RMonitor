

const MAX_LINES = 100; // 日志行数

const RENDER_INTERVAL = 10; // 日志渲染频率 ms

// 用于缓存最新的一条数据
let latestData = null;

// WebSocket
const ws_text = new WebSocket("ws://localhost:8000/ws/text");

// 获取日志
const log = document.getElementById("log");

// WebSocket接收回调
ws_text.onmessage = (event) => {
    latestData = event.data;
};

// 定时器定时渲染
setInterval(() => {
    // 如果没有新数据，直接跳过
    if (!latestData) {
        return;
    }

    const lastRenderTime = Date.now();

    appendLog(latestData);

    if (Date.now() - lastRenderTime > RENDER_INTERVAL) {
        appendLog(`[WARN] 刷新超时`);
    }

    latestData = null;
}, RENDER_INTERVAL);

// 日志输出
function appendLog(text) {
    const div = document.createElement("div");
    div.textContent = text;
    log.appendChild(div);

    while (log.childNodes.length > MAX_LINES) {
        log.removeChild(log.firstChild);
    }

    log.scrollTop = log.scrollHeight;
}





