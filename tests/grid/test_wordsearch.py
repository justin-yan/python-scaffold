import unittest
from hypothesis import given, settings, Verbosity
import hypothesis.strategies as st
from string import ascii_uppercase

from scaffold.grid import wordsearch

@unittest.skip("")
class TestModule(unittest.TestCase):

    @given(
        st.integers(min_value=1, max_value=20).flatmap(
            lambda rowlen: st.lists(st.lists(st.characters(min_codepoint=65, max_codepoint=90), min_size=rowlen, max_size=rowlen), min_size=1, max_size=20)
        ),
        st.text(ascii_uppercase, min_size=1, max_size=5)
        # st.text("ABCDE"", min_size=1, max_size=5)
    )
    @settings(verbosity=Verbosity.verbose)
    def test_equivalence(self, board, word):
        result = wordsearch.wordsearch_recursive(board, word)
        # print(board, word, result)
        assert result == wordsearch.wordsearch_explicit_stack(board, word)

if __name__ == '__main__':
    unittest.main()