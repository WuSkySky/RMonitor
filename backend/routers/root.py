from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

# 陆游
router = APIRouter()

# 加载html
templates = Jinja2Templates(directory="frontend/templates")

# 根页面
@router.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="main.html"
    )