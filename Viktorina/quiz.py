import random

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def ask(self):
        print(self.text)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
        
        while True:
            user_answer = input("Введите номер вашего ответа: ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(self.options):
                return int(user_answer) == self.correct_answer
            else:
                print("Пожалуйста, введите корректный номер ответа.")

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions, 1):
            print(f"\nВопрос {i} из {len(self.questions)}:")
            if question.ask():
                print("Правильно!")
                self.score += 1
            else:
                print(f"Неправильно. Правильный ответ: {question.options[question.correct_answer - 1]}")

        print(f"\nВикторина завершена! Ваш счет: {self.score}/{len(self.questions)}")
        percentage = (self.score / len(self.questions)) * 100
        print(f"Вы ответили правильно на {percentage:.2f}% вопросов.")

# Создаем вопросы
questions = [
    Question("Какая планета известна как 'Красная планета'?", 
             ["Венера", "Марс", "Юпитер", "Сатурн"], 2),
    Question("Кто написал 'Ромео и Джульетта'?", 
             ["Чарльз Диккенс", "Уильям Шекспир", "Джейн Остин", "Марк Твен"], 2),
    Question("Сколько континентов на Земле?", 
             ["5", "6", "7", "8"], 3),
    Question("Какой элемент имеет химический символ 'O'?", 
             ["Осмий", "Кислород", "Золото", "Олово"], 2),
    Question("Какая страна является родиной суши?", 
             ["Китай", "Таиланд", "Япония", "Корея"], 3)
]

# Создаем и запускаем викторину
if __name__ == "__main__":
    print("Добро пожаловать в викторину!")
    print("Отвечайте на вопросы, выбирая номер правильного ответа.")
    input("Нажмите Enter, чтобы начать...")
    
    quiz = Quiz(questions)
    quiz.run()
    
    print("\nСпасибо за участие в викторине!")