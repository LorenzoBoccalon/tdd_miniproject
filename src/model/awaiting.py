from pydantic import BaseModel, Field, ValidationError, validator
from time import time
from asyncio import sleep

class AwaitingModel(BaseModel):
    """
    Silly class to await some time. Used for exercise with asyncio.
    """
    hours: int = Field(0, ge=0)
    minutes: int = Field(0, ge=0, le=59)
    seconds: float = Field(0., ge=0, le=59)

    # @validator('*')
    # def ge_zero(cls, v):
    #     if v < 0:
    #         raise ValidationError('must be greater than or equal to zero!')
    #     return v

    # @validator('minutes', 'seconds')
    # def lt_sixty(cls, v):
    #     if v > 59:
    #         raise ValidationError('must be less than 60!')
    #     return v

    async def __call__(self) -> float:
        start = time()
        total_await_time = self.hours * 60 ** 2 + self.minutes * 60 + self.seconds
        await sleep(total_await_time)
        elapsed = time() - start
        return elapsed