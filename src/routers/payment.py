from datetime import datetime

from aiogram import Router
from aiogram.types import Message
from dateutil.relativedelta import relativedelta
from pydantic import ValidationError

from src.db.models import Payment
from src.schema.filter import FilterCreateSchema, FilterSchema
from src.schema.statistic import PaymentStatisticSchema, StatisticSchema

router = Router()


@router.message()
async def get_statistic(message: Message) -> None:
    try:
        data: FilterCreateSchema = FilterCreateSchema.model_validate_json(
            json_data=message.text,
        )
    except ValidationError:
        await message.answer(
            text=f'Невалидный запрос.\n\n{FilterSchema().model_dump_json()}',
        )
        return

    payment_stats: list[PaymentStatisticSchema] = await Payment.find(
        Payment.dt >= data.dt_from,
        Payment.dt <= data.dt_upto,
    ).aggregate(
        aggregation_pipeline=[
            {
                '$group': {
                    '_id': {
                        '$dateToString': {
                            'format': data.group_format,
                            'date': '$dt',
                        },
                    },
                    'sum': {
                        '$sum': '$value',
                    },
                },
            },
            {
                '$sort': {
                    '_id': 1,
                },
            },
        ],
        projection_model=PaymentStatisticSchema,
    ).to_list()

    labels: list = []
    dataset: list = []
    index: int = 0
    step: relativedelta = relativedelta(**{f'{data.group_type}s': 1})

    current_date: datetime = datetime.strptime(
        data.dt_from.strftime(data.group_format),
        data.group_format,
    ) - step

    while current_date <= (data.dt_upto - step):
        current_date += step

        if index < len(payment_stats):
            payment_stat: PaymentStatisticSchema = payment_stats[index]
            payment_date = datetime.strptime(
                payment_stat.date,
                data.group_format,
            )

            if current_date == payment_date:
                labels.append(payment_date)
                dataset.append(payment_stat.sum)
                index += 1

                continue

        labels.append(current_date)
        dataset.append(0)

    await message.answer(
        StatisticSchema(
            labels=labels,
            dataset=dataset,
        ).model_dump_json(),
    )
