from datetime import datetime

from pydantic import BaseModel, model_validator

from src.enums.group_type import GroupType, GroupTypeFormat


class FilterSchema(BaseModel):
    dt_from: datetime = datetime.now()
    dt_upto: datetime = datetime.now()
    group_type: GroupType = GroupType.month


class FilterCreateSchema(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: GroupType
    group_format: str | None = None

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'FilterCreateSchema':
        self.group_format = getattr(GroupTypeFormat, self.group_type)

        return self
