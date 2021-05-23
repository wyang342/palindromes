import unittest
from palindrome import palindrome


class TestPalindrome(unittest.TestCase):
    def test_racecar(self):
        self.assertEqual(palindrome('racecar'), True)

    def test_noon(self):
        self.assertEqual(palindrome('noon'), True)

    def test_civic(self):
        self.assertEqual(palindrome('civic'), True)

    def test_nice(self):
        self.assertEqual(palindrome('nice'), False)

    def test_434(self):
        self.assertEqual(palindrome('434'), True)

    def test_123(self):
        self.assertEqual(palindrome('123'), False)

    def test_bomb(self):
        self.assertEqual(palindrome('bomb'), False)

    def test_challenge_1(self):
        self.assertEqual(palindrome('Sore was I ere I saw Eros'), True)

    # def test_challenge_2(self):
    #     self.assertEqual(palindrome('racecar'), Tru

    # def test_challenge_3(self):
    #     self.assertEqual(palindrome('racecar'), Tru


# print(palindrome('racecar') == True)
# print(palindrome('Noon') == True)
# print(palindrome('ciVic') == True)
# print(palindrome('nice') == False)
# print(palindrome(434) == True)
# print(palindrome(123) == False)
# print(palindrome('bomb') == False)

# print("The following should be True if you're trying to do the extra portion of this challenge")
# print(palindrome('Sore was I ere I saw Eros.') == True)
# print(palindrome('A man, a plan, a canal -- Panama') == True)
