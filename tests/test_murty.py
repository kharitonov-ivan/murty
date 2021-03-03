from murty import Murty
import numpy as np


def test_murty_small():
    cost_matrix = np.eye(2)
    mgen = Murty(cost_matrix)

    is_ok, cost, solution = mgen.draw()

    assert is_ok
    assert cost == 0.0
    assert (solution == np.array([1, 0])).all()


def test_murty_big():
    cost_matrix = np.eye(100)
    mgen = Murty(cost_matrix)
    is_ok, cost, solution = mgen.draw()
    assert cost == 0.0
    assert cost == 0.0
