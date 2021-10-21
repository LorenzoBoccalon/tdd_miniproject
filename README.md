# Test Driven Development mini-project

A class `Awaiting` is implemented using TDD. The class uses a coroutine dunder method to wait a certain amount of time. 

The `main.py` module runs a simulation of $10$ waiting times (in seconds). The simulation compares the total waiting time of a concurrent processing versus a sequential processing. The times are sampled from an exponential distribution with $\lambda = 1.5$.