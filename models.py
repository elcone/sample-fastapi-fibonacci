from tortoise import fields, Model
from tortoise.contrib.pydantic import (
    pydantic_model_creator, pydantic_queryset_creator
)


class RequestedNumber(Model):
    id = fields.IntField(pk=True)
    number = fields.IntField()
    result = fields.IntField()

    def __str__(self):
        return f'{self.number} = {self.result}'


RequestedNumber_Pydantic = pydantic_model_creator(RequestedNumber,
    name='RequestedNumber')
RequestedNumberIn_Pydantic = pydantic_model_creator(RequestedNumber,
    name='RequestedNumberIn',
    exclude_readonly=True,
    exclude=['id', 'result'])
RequestedNumber_Pydantic_List = pydantic_queryset_creator(RequestedNumber)
