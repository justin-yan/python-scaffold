import unittest
from hypothesis import given
import hypothesis.strategies as st

from scaffold.iv import add2

@unittest.skip("")
class TestIv(unittest.TestCase):

    @given(st.integers())
    def test_hypothesis(self, n):
        assert add2(n) == n + 2

    def test_add(self):
        self.assertEqual(add2(0), 2)
        self.assertNotEqual(add2(1), 2)

if __name__ == '__main__':
    unittest.main()