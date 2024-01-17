import random


def generate_math_question(a, b):
    a1 = random.randint(a, b)
    b1 = random.randint(a, b)
    c1 = random.choice(["+", "-", "/", "*"])
    quaschans = f'{a1} {c1} {b1} '
    return quaschans

def check_answer(quaschans, i):
    try:
        i = float(i)
        return i==eval(quaschans)
    except ValueError:
        return False


def math_quiz(number_of_questions=5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        question=generate_math_question(1,5)
        answer=input(f"{question} = ")
        if check_answer(question,answer):
            correct_answers += 1
    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    if correct_answers >= number_of_questions* 0.8 :
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers >= number_of_questions* 0.6:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


# Запуск теста
math_quiz(7)
