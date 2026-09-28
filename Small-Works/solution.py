from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import select
from typing import List

DATABASE_URL = "sqlite+aiosqlite:///./burgers.db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class BurgerModel(Base):
    __tablename__ = "burgers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
    status: Mapped[str] = mapped_column(default="cooked")


app = FastAPI()


async def get_db():
    async with async_session() as session:
        yield session


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    async with async_session() as session:
        result = await session.execute(select(BurgerModel))
        existing = result.scalars().all()
        if not existing:
            session.add_all([
                BurgerModel(name="Classic Cheeseburger", price=8.99),
                BurgerModel(name="Double Bacon Smash", price=11.99),
                BurgerModel(name="Veggie Delight", price=9.50),
                BurgerModel(name="Spicy Chicken Burger", price=10.25),
            ])
            await session.commit()


async def get_burgers(number: int, db: AsyncSession) -> List[BurgerModel]:
    """
    Executes an asynchronous SQL query to fetch burgers from the database.
    """

    query = select(BurgerModel).limit(number)

    result = await db.execute(query)
 
    burgers = result.scalars().all()
    return burgers


@app.get("/burgers/{number}")
async def read_burgers(number: int, db: AsyncSession = Depends(get_db)):
    burgers = await get_burgers(number=number, db=db)
    
    return {
        "requested_count": number,
        "retrieved_count": len(burgers),
        "burgers": burgers
    }

@app.get("/")
async def root():
    return {"message": "Welcome to the Burger API! Go to /burgers/2 to fetch burgers."}