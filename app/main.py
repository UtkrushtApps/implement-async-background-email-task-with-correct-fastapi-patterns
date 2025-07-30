from fastapi import FastAPI, BackgroundTasks, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import UserCreate, UserRead
from app.database import get_async_session
from app.models import Base

app = FastAPI()

@app.post("/register", response_model=UserRead)
async def register_user(user: UserCreate, background_tasks: BackgroundTasks, session: AsyncSession = Depends(get_async_session)):
    pass
