# tests/performance/test_calculator_perf.py
from calculator.calculator import add, sub, mul


def test_add_performance(benchmark):
    """Performance of add()"""
    benchmark(add, 100, 200)


def test_sub_performance(benchmark):
    """Performance of sub()"""
    benchmark(sub, 300, 100)


def test_mul_performance(benchmark):
    """Performance of mul()"""
    benchmark(mul, 20, 30)
