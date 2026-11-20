class StudySet:
    """Учебный набор карточек."""

    def __init__(self, title, description=""):
        if not title.strip():
            raise ValueError("Название набора не может быть пустым.")

        self.title = title.strip()
        self.description = description.strip()
        self.cards = []

    def add_card(self, card):
        """Добавляет карточку в набор."""
        if not isinstance(card, dict):
            raise TypeError("Карточка должна быть словарём.")

        if not card.get("question") or not card.get("answer"):
            raise ValueError("Карточка должна содержать вопрос и ответ.")

        self.cards.append(card.copy())

    def remove_card(self, card_index):
        """Удаляет карточку по индексу."""
        if not isinstance(card_index, int) or not 0 <= card_index < len(self.cards):
            raise IndexError("Карточка не найдена.")

        return self.cards.pop(card_index)

    def rename(self, new_title):
        """Изменяет название набора."""
        if not new_title.strip():
            raise ValueError("Название набора не может быть пустым.")

        self.title = new_title.strip()

    def get_cards(self):
        """Возвращает карточки набора."""
        return self.cards.copy()
