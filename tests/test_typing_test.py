import unittest
from typing_test import score_typing


class ScoreTypingTests(unittest.TestCase):
    def test_perfect_text_accuracy_and_wpm(self):
        result = score_typing("hello world", "hello world", 60)
        self.assertEqual(result.wpm, 2.2)
        self.assertEqual(result.accuracy, 100.0)

    def test_mismatched_text_has_reduced_accuracy(self):
        result = score_typing("hello", "hallo!", 30)
        self.assertLess(result.accuracy, 100.0)
        self.assertEqual(result.wpm, 2.4)

    def test_zero_or_negative_elapsed_time_is_safe(self):
        self.assertEqual(score_typing("abc", "abc", 0).wpm, 0.0)
        self.assertEqual(score_typing("abc", "abc", -5).wpm, 0.0)

    def test_empty_input_is_safe(self):
        self.assertEqual(score_typing("abc", "", 20).wpm, 0.0)


if __name__ == "__main__":
    unittest.main()