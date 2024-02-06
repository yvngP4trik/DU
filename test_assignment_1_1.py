import pytest

from assignment_1_1 import is_older


@pytest.mark.parametrize(
    ("my_age", "brother_age", "sister_age", "sol_a", "sol_b", "sol_c", "sol_d", "sol_e"),
    [
        (20, 32, 18, True, True, True, True, True),
        (10, 15, 20, True, False, False, True, True),
        (20, 10, 15, False, False, False, False, True),
        (20, 15, 10, False, True, True, False, True),
        (10, 20, 5, True, True, True, True, False),
        (10, 10, 10, False, False, False, False, True),
     ]
)
def test_is_older(my_age, brother_age, sister_age, sol_a, sol_b, sol_c, sol_d, sol_e):
    is_older_a, is_older_b, is_older_c, is_older_d, is_older_e = is_older(my_age, brother_age, sister_age)
    assert is_older_a == sol_a
    assert is_older_b == sol_b
    assert is_older_c == sol_c
    assert is_older_d == sol_d
    assert is_older_e == sol_e
