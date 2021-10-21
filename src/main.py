from model.awaiting import AwaitingModel
from time import time
from asyncio import gather, run
import numpy as np


async def main():
    # sample times from a simulation
    times = np.random.exponential(scale=1.5, size=10)
    total_await_time = times.sum()

    # create tasks and collect results
    start = time()
    elapsed_times = await gather(*[AwaitingModel(seconds=t)() for t in times])
    total_elapsed_time = time() - start
    # print results
    for i, e in enumerate(elapsed_times):
        print(f"task: {i}, elapsed: {e:.3f}")
    print(
        f"concurrent execution time: {total_elapsed_time:.3f} s\nsequential execution time: {total_await_time:.3f} s")

if __name__ == "__main__":
    run(main())
