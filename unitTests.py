import unittest

from main import *


class TestBasicData(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.ex = App()

    def test_permute_using_prefixes_and_suffixes(self):
        self.ex.prefixes_and_suffixes = ["12", "asd"]
        word = "abc"
        result = self.ex.permute_password_using_prefixes_and_suffixes(word)
        self.assertTrue(len(result) == 8 and result.__contains__("12abc") and result.__contains__("12abc12") and result.__contains__("abc12") and result.__contains__("12abcasd") and result.__contains__("abcasd") and result.__contains__("asdabc") and result.__contains__("asdabc12") and result.__contains__("asdabcasd"))

    def test_special_characters_permutation(self):
        no_special_characters_word = "mnb"
        special_characters_word = "tas"
        mix_word = "something"
        result_no_special = self.ex.permute_password_using_special_symbols(no_special_characters_word)
        result_special = self.ex.permute_password_using_special_symbols(special_characters_word)
        result_mix = self.ex.permute_password_using_special_symbols(mix_word)
        self.assertTrue(result_no_special.__contains__(no_special_characters_word) and len(result_no_special) == 1)
        self.assertTrue(len(result_special) == 5 and result_special.__contains__("tas") and
                        result_special.__contains__("ta$") and result_special.__contains__("t@s") and
                        result_special.__contains__("7as") and result_special.__contains__("ta5"))

    def test_letter_permutation(self):
        word_with_space = "abc def"
        word = "xyz"
        result_with_space = self.ex.get_variaions_for_letters(word_with_space)
        result = self.ex.get_variaions_for_letters(word)
        self.assertTrue(len(result_with_space) == pow(2, len(word_with_space)-1))
        self.assertTrue(len(result) == pow(2, len(word)))
        self.assertTrue(result.__contains__("xyZ"), result.__contains__("xyz") and result.__contains__("xYz") and
                        result.__contains__("xYZ") and result.__contains__("Xyz") and result.__contains__("XyZ") and
                        result.__contains__("XYz") and result.__contains__("XYZ"))

    def test_change_first_letter_to_capital(self):
        lower_case_word = "abc"
        lower_upper_case_word = "xYz"
        upper_case_word = "POIU"
        result = self.ex.add_change_first_letter_to_capital([lower_case_word, lower_upper_case_word, upper_case_word])
        self.assertTrue(result.__contains__("Abc") and result.__contains__("XYz") and result.__contains__("POIU"))
        self.assertTrue(len(result) == 3)

    def test_change_last_letter_to_capital(self):
        lower_case_word = "abc"
        lower_upper_case_word = "xYz"
        upper_case_word = "POIU"
        result = self.ex.add_change_last_letter_to_capital([lower_case_word, lower_upper_case_word, upper_case_word])
        self.assertTrue(result.__contains__("abC") and result.__contains__("xYZ") and result.__contains__("POIU"))
        self.assertTrue(len(result) == 3)

    def test_change_to_camel_case(self):
        lower_case_word = "abc"
        lower_upper_case_word = "xYz"
        lower_upper_case_words = "poi uYt Rew QAS dFG"
        result = self.ex.add_change_to_camel_case([lower_case_word, lower_upper_case_word, lower_upper_case_words])
        self.assertTrue(result.__contains__("Abc") and result.__contains__("Xyz") and result.__contains__("Poi Uyt Rew Qas Dfg"))
        self.assertTrue(len(result) == 3)


if __name__ == '__main__':
    unittest.main()
