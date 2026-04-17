from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from sqlmodel import Session, select
from typing import List

from database import *
from models import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

#Page functions
@app.get("/")
def index(req: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={"request": req}
    )

@app.get("/register")
def register(req: Request):
    return templates.TemplateResponse(
        name="register.html",
        context={"request": req}
    )

@app.get("/home")
def home(req: Request):
    return templates.TemplateResponse(
        name="home.html",
        context={"request": req}
    )

@app.get("/algorithms/{alg_name}")
async def algorithm_page(req: Request, alg_name: str):
    return templates.TemplateResponse(
        f"algorithms/{alg_name}.html",
        {"request": req}
    )

@app.get("/favorites")
def favorites_page(req: Request):
    user_id = req.cookies.get("user_id")

    if not user_id:
        return RedirectResponse(url="/", status_code=303)

    with Session(engine) as session:
        favorites = session.exec(
            select(Favorite).where(Favorite.user_id == int(user_id))
        ).all()

    return templates.TemplateResponse(
        "favorites.html",
        {
            "request": req,
            "favorites": favorites
        }
    )

#Database functions
@app.post("/register/")
def create_user(
    username: str = Form(...),
    password: str = Form(...)
):
    with Session(engine) as session:
        existing_user = session.exec(
            select(User).where(User.username == username)
        ).first()

        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)   # important

        response = RedirectResponse(url="/home", status_code=303)
        response.set_cookie(key="user_id", value=str(user.id))
        return response
    
@app.get("/users/", response_model=List[User])
def get_users():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users
    
@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        user = session.exec(statement).first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        if user.password != password:
            raise HTTPException(status_code=401, detail="Incorrect password")
        
        response = RedirectResponse(url="/home", status_code=303)
        response.set_cookie(key="user_id", value=str(user.id))
        return response
    
@app.post("/favorite/{alg_name}")
def add_favorite(alg_name: str, req: Request):
    user_id = req.cookies.get("user_id")

    if not user_id:
        raise HTTPException(status_code=401, detail="Not logged in")

    with Session(engine) as session:
        existing_favorite = session.exec(
            select(Favorite).where(
                Favorite.user_id == int(user_id),
                Favorite.alg_name == alg_name
            )
        ).first()

        if existing_favorite:
            return RedirectResponse(url=f"/algorithms/{alg_name}", status_code=303)

        favorite = Favorite(user_id=int(user_id), alg_name=alg_name)
        session.add(favorite)
        session.commit()

        return RedirectResponse(url=f"/algorithms/{alg_name}", status_code=303)
    
@app.get("/favorites")
def favorites_page(req: Request):
    user_id = req.cookies.get("user_id")

    if not user_id:
        return RedirectResponse(url="/", status_code=303)

    with Session(engine) as session:
        favorites = session.exec(
            select(Favorite).where(Favorite.user_id == int(user_id))
        ).all()

        return templates.TemplateResponse(
            "favorites.html",
            {
                "request": req,
                "favorites": favorites
            }
        )