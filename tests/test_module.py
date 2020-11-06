import unittest
from hypothesis import given
import hypothesis.strategies as st

from scaffold.module import test


class TestModule(unittest.TestCase):

    @given(st.integers())
    def test_hypothesis(self, n):
        assert test(n) == n + 2

    def test_add(self):
        self.assertEqual(test(0), 2)
        self.assertNotEqual(test(1), 2)

if __name__ == '__main__':
    unittest.main()