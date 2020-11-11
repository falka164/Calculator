import calculator


class TestCalculator:

    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_substract(self):
        assert 2 == calculator.substract(4, 2)