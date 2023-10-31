from datetime import datetime

from beanie import Document


class Payment(Document):
    value: float
    dt: datetime

    class Settings:
        name = 'sample_collection'
