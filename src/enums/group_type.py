from enum import StrEnum


class GroupType(StrEnum):
    month = 'month'
    day = 'day'
    hour = 'hour'


class GroupTypeFormat(StrEnum):
    month = '%Y-%m'
    day = '%Y-%m-%d'
    hour = '%Y-%m-%dT%H'
