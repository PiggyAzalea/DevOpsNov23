import unittest
from python_katas.kata_1 import questions
from python_katas.utils import unittest_runner


testers = ['']


class TestSumOfElements(unittest.TestCase):
    """
    1 Katas
    """

    def sum_of_element(elements):
        return sum(elements)

    def test_empty_list(self):
        lst = []
        self.assertEqual(questions.sum_of_element(lst), 0)


    def test_integers_list(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(questions.sum_of_element(lst), 15)

    def test_negative_numbers(self):
        lst = [1, -6, 7, 0, 99]
        self.assertEqual(questions.sum_of_element(lst), 101)

    def test_all_zeros(self):
        lst = [0] * 50000
        self.assertEqual(questions.sum_of_element(lst), 0)


class TestVerbing(unittest.TestCase):
    """
    1 Katas
    """
    pass


class TestWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """
    pass




class TestReverseWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """
    pass


class TestIsUniqueString(unittest.TestCase):
    """
    2 Katas
    """
    pass




class TestListDiff(unittest.TestCase):
    """
    1 Katas
    """
    pass

class TestPrimeNumber(unittest.TestCase):
    """
    1 Katas
    """
    pass


class TestPalindromeNum(unittest.TestCase):
    """
    1 Katas
    """
    pass

class TestPairMatch(unittest.TestCase):
    """
    3 Katas
    """
    pass


class TestBadAverage(unittest.TestCase):
    """
    1 Katas
    """
    pass

class TestBestStudent(unittest.TestCase):
    """
    1 Katas
    """
    pass


class TestPrintDictAsTable(unittest.TestCase):
    """
    1 Katas
    """
    pass


class TestMergeDicts(unittest.TestCase):
    """
    1 Katas
    """
    pass

class TestSevenBoom(unittest.TestCase):
    """
    1 Katas
    """
    pass


class TestCaesarCipher(unittest.TestCase):
    """
    1 Katas
    """
    pass


class TestSumOfDigits(unittest.TestCase):
    """
    1 Katas
    """
    pass


if __name__ == '__main__':
    import inspect
    import sys
    unittest_runner(inspect.getmembers(sys.modules[__name__], inspect.isclass))