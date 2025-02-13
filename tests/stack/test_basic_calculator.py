import pytest
from solutions.stack.basic_calculator import Solution

@pytest.mark.parametrize("expression, expected", [
    ("1 + 1", 2),
    ("2-1 + 2", 3),
    ("(1+(4+5+2)-3)+(6+8)", 23),
    (" 6-4 / 2 ", 4),
    ("3+2*2", 7),
    (" 3/2 ", 1),
    (" 3+5 / 2 ", 5),
    (" 3+5*2-4/2 ", 11),
    (" (3+5) / 2 ", 4),
    ("(2+6* 3+5- (3*14/7+2)*5)+3", -12),
    ("2*(5+5*2)/3+(6/2+8)", 21)
])
def test_calculate(expression, expected):
    calculator = Solution()
    assert calculator.calculate(expression) == expected