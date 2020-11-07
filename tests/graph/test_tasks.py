import unittest

from hypothesis import given, strategies as st

from scaffold.graph.tasks import Task, simple_timecalc


@unittest.skip("")
class TestModule(unittest.TestCase):

    def setUp(self) -> None:
        self.simple_task_battery = [
            Task(1, 5, []),
            Task(2, 5, []),
            Task(3, 5, []),
            Task(4, 5, [])
        ]

        self.cycle_task_battery = [
            Task(1, 5, [2]),
            Task(2, 5, [3]),
            Task(3, 5, [4]),
            Task(4, 5, [1])
        ]

    @given(st.integers(1, 4))
    def test_simple_graph(self, n):
        assert simple_timecalc(n, self.simple_task_battery) == 5

    @given(st.integers(1, 4))
    def test_cycle_graph(self, n):
        assert simple_timecalc(n, self.cycle_task_battery) == 20


if __name__ == '__main__':
    unittest.main()
