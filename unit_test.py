import unittest
import functions


class TestFunctions(unittest.TestCase):

    def test_add_week(self):
        date = '2021-10-14-2021-10-20'
        date1 = functions.add_week(date)

        self.assertEqual(date1, '2021-10-21-2021-10-27')

    def test_verify_format_regex(self):
        string = '123456'
        reg = '^[0-9]{6}'
        self.assertTrue(functions.verify_format_regex(reg, string))

    def test_switcher(self):
        def switch(argument):
            switcher = {
                0: "zero",
                1: "one",
                2: "two",
            }
            return switcher.get(argument, "nothing")

        self.assertEqual(switch(0), "zero")

    def test_replace(self):
        word1 = 'chocolate'
        word2 = 'fruits'
        sentence = 'I love ' + word1
        test = sentence.replace(word1, word2)
        self.assertEqual(test, 'I love ' + word2)


if __name__ == '__main__':
    unittest.main()
