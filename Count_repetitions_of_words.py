#!/usr/bin/env python

# Author: Manug-github
# License: GNU GPLv3

"""Count the number of words in "Zen_of_Python.txt"? 
Not case sensitive.
Words with apostrophe do not separate, "it's" is different from "it" or "is"
"""

import unittest

def number_of_repetitions(input_word) -> int:
    """Return repetitions of input_word"""

    # code here


class AllUniqueTests(unittest.TestCase):

    def test_all_unique(self):
        self.assertTrue (number_of_repetitions("idea") == 3)
        self.assertTrue (number_of_repetitions("is") == 10)
        self.assertTrue (number_of_repetitions("explain") == 2)
        self.assertTrue (number_of_repetitions("Complex") == 2)
        self.assertTrue (number_of_repetitions("Unless") == 2)
        self.assertTrue (number_of_repetitions("now") == 2)
        self.assertTrue (number_of_repetitions("Zen") == 0)

if __name__ == "__main__":

    unittest.main()
