import imp
from typing import List

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from fibonacci import fibonacci
from models import (
    RequestedNumber, RequestedNumber_Pydantic, RequestedNumberIn_Pydantic
)


app = FastAPI()


@app.get('/', response_model=List[RequestedNumber_Pydantic])
async def get_fibonacci():
    return await RequestedNumber_Pydantic.from_queryset(RequestedNumber.all())


@app.post('/', response_model=RequestedNumber_Pydantic)
async def get_fibonacci(requested_number: RequestedNumberIn_Pydantic):
    requested_number_obj = await RequestedNumber.create(
      result=fibonacci(requested_number.number),
      **requested_number.dict(exclude_unset=True))

    return await RequestedNumber_Pydantic.from_tortoise_orm(requested_number_obj)


register_tortoise(app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models']},
    generate_schemas=True)
