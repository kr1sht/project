def edit_card(cards, card_index, question=None, answer=None):
    """Редактирует вопрос и/или ответ существующей карточки."""
    if not isinstance(card_index, int) or not 0 <= card_index < len(cards):
        raise IndexError("Карточка с таким номером не найдена.")

    if question is not None:
        if not question.strip():
            raise ValueError("Вопрос не может быть пустым.")
        cards[card_index]["question"] = question.strip()

    if answer is not None:
        if not answer.strip():
            raise ValueError("Ответ не может быть пустым.")
        cards[card_index]["answer"] = answer.strip()

    return cards[card_index]


def delete_card(cards, card_index):
    """Удаляет карточку по её индексу."""
    if not isinstance(card_index, int) or not 0 <= card_index < len(cards):
        raise IndexError("Карточка с таким номером не найдена.")

    return cards.pop(card_index)
