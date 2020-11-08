#! /usr/bin/env python

# Author: Manug-github
# License: GNU GPLv3

""" What is the maximum length of a non-empty substring that contains only one unique character? """

import unittest

def max_consecutive(s) -> int:
    pass # code here


class AllUniqueTests(unittest.TestCase):

    def test_all_unique(self):
        self.assertTrue (max_consecutive("a") == 1)
        self.assertTrue (max_consecutive("leetcode") == 2)
        self.assertTrue (max_consecutive("abbcccddddeeeeedcba") == 5)
        self.assertTrue (max_consecutive("triplepillooooow") == 5)
        self.assertTrue (max_consecutive("tourist") == 1)
        self.assertTrue (max_consecutive(10000*("qwerty")+"yellow") == 2)

if __name__ == "__main__":

    unittest.main()