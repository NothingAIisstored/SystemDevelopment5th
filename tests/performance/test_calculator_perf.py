from calculator.calculator import Calculator


def test_add_performance(benchmark):
    calc = Calculator()
    benchmark(calc.add, 100, 200)


def test_subtract_performance(benchmark):
    calc = Calculator()
    benchmark(calc.subtract, 300, 100)


def test_multiply_performance(benchmark):
    calc = Calculator()
    benchmark(calc.multiply, 20, 30)
