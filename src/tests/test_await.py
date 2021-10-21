import pytest 
from asyncio import gather
from src.model.awaiting import AwaitingModel

def test_validate_model_ge_zero():
    with pytest.raises(Exception) as e_info:
        AwaitingModel(seconds=-1)


def test_validate_model_lt_sixty():
    with pytest.raises(Exception) as e_info:
        AwaitingModel(seconds=61)

@pytest.mark.asyncio
async def test_zero_waiting():
    res = await AwaitingModel()()
    assert res < 1e-3

@pytest.mark.asyncio
async def test_waitings_sum():
    tasks = [AwaitingModel(seconds=1), AwaitingModel(seconds=2), AwaitingModel(seconds=3)]
    results = await gather(*[a() for a in tasks])
    res = sum(results)
    assert res - 6 < 1e-1