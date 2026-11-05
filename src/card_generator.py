
import re
from pathlib import Path


def generate_cards(text):
    """Создаёт карточки из структурированного конспекта."""
    pattern = re.compile(
        r"Вопрос\s*\d*\s*\n(.*?)\nОтвет\s*\d*\s*\n(.*?)(?=\nВопрос\s*\d*\s*\n|\Z)",
        re.IGNORECASE | re.DOTALL
    )

    cards = []

    for question, answer in pattern.findall(text):
        question = question.strip()
        answer = answer.strip()

        if question and answer:
            cards.append({
                "question": question,
                "answer": answer
            })

    return cards


def load_notes(file_path):
    """Читает текстовый файл с конспектом."""
    return Path(file_path).read_text(encoding="utf-8")


if __name__ == "__main__":
    notes_path = Path(__file__).parent.parent / "examples" / "example_notes.md"

    notes = load_notes(notes_path)
    cards = generate_cards(notes)

    if not cards:
        print("Карточки не найдены. Проверьте формат конспекта.")
    else:
        print(f"Создано карточек: {len(cards)}")

        for number, card in enumerate(cards, start=1):
            print(f"\nКарточка {number}")
            print(f"Вопрос: {card['question']}")
            print(f"Ответ: {card['answer']}")
