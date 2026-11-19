
import json
import os
class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

class QuizGame:
    def __init__(self):
        self.questions = []
        self.high_score = 0
    def add_quiz(self, quiz):
                self.questions.append(quiz)
game = QuizGame()  
with open("state.json", "r", encoding="utf-8") as file:
    state = json.load(file)

high_score = state["high_score"]
game.high_score = high_score
print("=" * 40)
print("🐼 핑크판다 파이썬 퀴즈 게임 🐼")
print("파이썬 공부를 시작합니다!")

print(f"현재 최고 점수: {high_score}점")

print("=" * 40)
def add_question():
    print("\n🐼 새로운 퀴즈 추가")

    question_text = input("새로운 문제를 입력하세요: ")

    options = []

    for i in range(4):
        option = input(f"{i + 1}번 보기를 입력하세요: ")
        options.append(option)

    answer = int(input("정답 번호를 입력하세요 (1~4): "))

    new_question = {
        "question": question_text,
        "options": options,
        "answer": answer
    }

    questions.append(new_question)

    with open("questions.json", "w", encoding="utf-8") as file:
        json.dump(questions, file, ensure_ascii=False, indent=4)

    print("🎉 새로운 퀴즈가 추가되었습니다!")

questions = [
    {
        "question": "Python에서 화면에 글자를 출력하는 함수는?",
        "options": ["input()", "print()", "len()", "type()"],
        "answer": 2
    },
    {
        "question": "Python에서 사용자 입력을 받는 함수는?",
        "options": ["print()", "len()", "input()", "type()"],
        "answer": 3
    },
    {
        "question": "문자열의 길이를 구하는 함수는?",
        "options": ["print()", "input()", "type()", "len()"],
        "answer": 4
    },
    {
        "question": "Python에서 정수를 나타내는 자료형은?",
        "options": ["str", "float", "int", "bool"],
        "answer": 3
    },
    {
        "question": "반복 작업에 사용하는 키워드는?",
        "options": ["if", "for", "def", "return"],
        "answer": 2
    }
]

if os.path.exists("questions.json"):
    with open("questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)
else:
    with open("questions.json", "w", encoding="utf-8") as file:
        json.dump(questions, file, ensure_ascii=False, indent=4)

for question_data in questions:
    quiz = Quiz(
        question_data["question"],
        question_data["options"],
        question_data["answer"]
    )
    game.add_quiz(quiz)

print(f"🐼 클래스에 등록된 퀴즈: {len(game.questions)}문제")
def play_quiz():
    global high_score 
    # add_question()
    print("\n🐼 퀴즈 문제 확인")

    score = 0


    print("\n🐼 핑크판다 퀴즈 시작!")

    for number, question in enumerate(game.questions, start=1):
        print(f"\n{number}. {question.question}")

        for option_number, option in enumerate(question.options, start=1):
            print(f"{option_number}. {option}")

    

      
        answer = input("정답 번호를 입력하세요: ")

        if answer == str(question.answer):
            print("🎉 정답입니다!")
            score += 1
        else:
            print("❌ 오답입니다!")
            print(f"정답은 {question.answer}번입니다.")

    print("\n" + "=" * 40)
    print("🐼 퀴즈가 끝났습니다!")
    print(f"총 문제 수: {len(questions)}문제")
    print(f"맞힌 문제 수: {score}문제")
    print(f"최종 점수: {score * 20}점")

    final_score = score * 20

    if final_score > high_score:
        high_score = final_score

        state["high_score"] = high_score

        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(state, file, ensure_ascii=False, indent=4)

        print("🎉 새로운 최고 점수입니다!")

    print("=" * 40)
    
   
    print("\n" + "=" * 40)
while True:
    print("🐼 핑크판다 파이썬 퀴즈 게임 🐼")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 최고 점수 확인")
    print("5. 종료")
    print("=" * 40)

    choice = input("메뉴 번호를 입력하세요 (1~5): ")

    if choice == "1":
        play_quiz()

    elif choice == "2":
        add_question()

    elif choice == "3":
        for number, question in enumerate(questions, start=1):
            print(f"{number}. {question['question']}")

    elif choice == "4":
        print(f"🏆 현재 최고 점수: {high_score}점")

    elif choice == "5":
        print("🐼 핑크판다 퀴즈 게임을 종료합니다. 안녕히 가세요!")
        break

    else:
        print("⚠️ 1부터 5까지의 숫자를 입력해 주세요.")