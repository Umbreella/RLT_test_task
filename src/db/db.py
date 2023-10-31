from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.config import settings
from src.db.models import Payment


async def init_db() -> None:
    database: AsyncIOMotorDatabase = AsyncIOMotorDatabase(
        client=AsyncIOMotorClient(
            'mongodb://{username}:{password}@{host}:{port}'.format(
                username=settings.MONGODB_USERNAME,
                password=settings.MONGODB_PASSWORD,
                host=settings.MONGODB_HOST,
                port=settings.MONGODB_PORT,
            ),
        ),
        name=settings.MONGODB_DATABASE,
    )

    await init_beanie(
        database=database,
        document_models=[
            Payment,
        ],
    )
