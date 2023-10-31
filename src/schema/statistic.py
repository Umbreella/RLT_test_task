from datetime import datetime

from pydantic import BaseModel, Field


class StatisticSchema(BaseModel):
    dataset: list[int]
    labels: list[datetime]


class PaymentStatisticSchema(BaseModel):
    date: str = Field(alias="_id")
    sum: float
