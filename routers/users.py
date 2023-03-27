import sys

from starlette.responses import HTMLResponse

sys.path.append("..")

from fastapi import APIRouter, Depends, Request, Response, status, Form
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal
from pydantic import BaseModel
from .auth import get_current_user, verify_password, get_password_hash
from starlette.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


@router.get("/change-password", response_class=HTMLResponse)
async def change_password_view(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse("change-password.html", {"request": request, "user": user})


@router.post("/change-password", response_class=HTMLResponse)
async def change_password(request: Request, username: str = Form(),
                          password: str = Form(), password2: str = Form(),
                          db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    user_data = db.query(models.Users).filter(models.Users.username == username).first()
    msg = "Invalid username or password"
    if user_data is not None:
        if username == user_data.username and verify_password(password, user_data.hashed_password):
            user_data.hashed_password = get_password_hash(password2)
            db.add(user_data)
            db.commit()
            msg = "Password updated"
    return templates.TemplateResponse("change-password.html", {"request": request, "msg": msg, "user": user})



