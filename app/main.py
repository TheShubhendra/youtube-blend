from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import User
from app.schemas import LoginRequest

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REDIRECT_URI = "http://localhost:5173"

@app.post("/auth/login-flow")
async def login(login_request: LoginRequest, db: AsyncSession = Depends(get_db)):
    flow = Flow.from_client_secrets_file(
        client_secrets_file="client_secrets.json",
        scopes=[
            "https://www.googleapis.com/auth/youtube.readonly",
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile",
            "openid",
        ],
        redirect_uri=REDIRECT_URI,
    )
    flow.fetch_token(code=login_request.code)

    credentials = flow.credentials
    profile = build("oauth2", "v2", credentials=credentials).userinfo().get().execute()
    async with db as session:
        res = await session.execute(
            select(User).filter(User.google_id == profile["id"])
        )
        user = res.scalars().first()
        if user is None:
            user = User(
                google_id=profile["id"],
                name=profile["name"],
                email=profile["email"],
                picture=profile["picture"],
                access_token=credentials.token,
                refresh_token=credentials.refresh_token,
            )
            session.add(user)
        else:
            user.access_token = credentials.token
            user.refresh_token = credentials.refresh_token
        await session.commit()
    return {
        "access_token": credentials.token,
        "token_type": "bearer",
        "profile": profile,
    }
