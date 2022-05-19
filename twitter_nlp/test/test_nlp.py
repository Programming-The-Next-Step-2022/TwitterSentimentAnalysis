import unittest

from twitter_nlp.core import nlp

class TestSum(unittest.TestCase):
    """Testing unit to determine if output remains the same.

    Basic unittest to determine if the outputs from the counting 
    function (simple_nlp) still match the original results.
    
    """
    def test_compute(self):
        """Tests whether output of class match the orignal ones."""
        obj = nlp()
        obj.simple_nlp()
        self.assertAlmostEqual(
            obj.counts,
            [13181, 6091, 2911]
        )

if __name__ == "__main__":
    unittest.main()