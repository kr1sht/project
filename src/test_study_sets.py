import unittest

from study_sets import StudySet


class TestStudySet(unittest.TestCase):

    def setUp(self):
        self.study_set = StudySet("Python", "Основы Python")
        self.card = {
            "question": "Что такое Python?",
            "answer": "Язык программирования"
        }

    def test_create_study_set(self):
        self.assertEqual(self.study_set.title, "Python")
        self.assertEqual(self.study_set.description, "Основы Python")

    def test_add_card(self):
        self.study_set.add_card(self.card)
        self.assertEqual(len(self.study_set.cards), 1)

    def test_remove_card(self):
        self.study_set.add_card(self.card)
        removed = self.study_set.remove_card(0)
        self.assertEqual(removed["question"], "Что такое Python?")
        self.assertEqual(len(self.study_set.cards), 0)

    def test_rename(self):
        self.study_set.rename("Java")
        self.assertEqual(self.study_set.title, "Java")

    def test_empty_title(self):
        with self.assertRaises(ValueError):
            StudySet(" ")

    def test_invalid_card(self):
        with self.assertRaises(ValueError):
            self.study_set.add_card({"question": "Вопрос"})

    def test_invalid_index(self):
        with self.assertRaises(IndexError):
            self.study_set.remove_card(0)


if __name__ == "__main__":
    unittest.main()
