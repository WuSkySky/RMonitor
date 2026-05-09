### 介绍
ros2监视器

### 功能
- 终端功能

### 启动
1. 后端 根目录执行
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

2. 前端 根目录执行
```bash
npm --prefix ./frontend run dev
```

2. 浏览器访问 http://127.0.0.1:8000
