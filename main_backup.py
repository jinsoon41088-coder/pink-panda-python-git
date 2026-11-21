import json
print("=" * 40)
print("🐼 핑크판다 파이썬 퀴즈 게임 🐼")
print("파이썬 공부를 시작합니다! 💗")
print("=" * 40)
question = {
    "question": "Python에서 화면에 글자를 출력하는 함수는?",
    "options": ["input()", "print()", "len()", "type()"],
    "answer": 2
}
question2 = {
    "question": "Python에서 사용자 입력을 받는 함수는?",
    "options": ["print()", "len()", "input()", "type()"],
    "answer": 3
}
question3 = {
    "question": "Python에서 문자열의 길이를 구하는 함수는?",
    "options": ["print()", "input()", "type()", "len()"],
    "answer": 4
}
question4 = {
    "question": "Python에서 정수를 나타내는 자료형은?",
    "options": ["str", "float", "int", "bool"],
    "answer": 3
}
question5 = {
    "question": "Python에서 반복 작업을 수행할 때 사용하는 키워드는?",
    "options": ["if", "for", "def", "return"],
    "answer": 2
}

questions = [question, question2, question3, question4, question5]

score = 0

try:
    with open("state.json", "r", encoding="utf-8") as file:
        state = json.load(file)
        high_score = state.get("high_score", 0)
except (FileNotFoundError, json.JSONDecodeError):
    high_score = 0
print(f"🐼 저장된 최고 점수: {high_score}점 💗")

for quiz_number, quiz in enumerate(questions, start=1):
    print(f"\n📝 {quiz_number}번째 퀴즈")
    print(quiz["question"])

    for number, option in enumerate(quiz["options"], start=1):
        print(f"{number}. {option}")

    user_answer = input("\n정답 번호를 입력하세요 (1~4): ")

    if user_answer == str(quiz["answer"]):
        score += 10
        print("🎉 정답입니다! 참 잘했어요! 🐼💗")
    else:
        print("❌ 아쉬워요! 오답입니다.")

print(f"\n🏆 최종 점수: {score}점")
if score > high_score:
    high_score = score
    with open("state.json", "w", encoding="utf-8") as file:
        json.dump({"high_score": high_score}, file, ensure_ascii=False, indent=4)
    print("🎉 새로운 최고 점수를 달성했어요! 🐼💗")
print("\n" + "=" * 40)
print("🐼 핑크판다 파이썬 퀴즈 게임 메뉴 🐼")
print("=" * 40)
print("1. 퀴즈 풀기")
print("2. 퀴즈 추가")
print("3. 퀴즈 목록")
print("4. 최고 점수 확인")
print("5. 종료")
print("=" * 40)
menu_choice = input("메뉴 번호를 입력하세요 (1~5): ")
if menu_choice == "3":
    print("📋 핑크판다 퀴즈 목록 🐼")
    for number, quiz in enumerate(questions, start=1):
        print(f"{number}. {quiz['question']}")
elif menu_choice == "4":
    print(f"🏆 최고 점수: {high_score}점")
elif menu_choice == "5":
    print("🐼 핑크판다 퀴즈 게임을 종료합니다. 다음에 또 만나요! 💗")
else:
    print("선택한 메뉴 번호:", menu_choice)