import unittest

from card_manager import edit_card, delete_card


class TestCardManager(unittest.TestCase):

    def setUp(self):
        self.cards = [
            {"question": "Что такое Python?", "answer": "Язык программирования"},
            {"question": "Что такое Git?", "answer": "Система контроля версий"}
        ]

    def test_edit_question(self):
        edit_card(self.cards, 0, question="Что такое Java?")
        self.assertEqual(self.cards[0]["question"], "Что такое Java?")

    def test_edit_answer(self):
        edit_card(self.cards, 0, answer="Другой ответ")
        self.assertEqual(self.cards[0]["answer"], "Другой ответ")

    def test_delete_card(self):
        deleted = delete_card(self.cards, 0)
        self.assertEqual(deleted["question"], "Что такое Python?")
        self.assertEqual(len(self.cards), 1)

    def test_invalid_index(self):
        with self.assertRaises(IndexError):
            delete_card(self.cards, 5)

    def test_empty_question(self):
        with self.assertRaises(ValueError):
            edit_card(self.cards, 0, question=" ")

if __name__ == "__main__":
    unittest.main()
