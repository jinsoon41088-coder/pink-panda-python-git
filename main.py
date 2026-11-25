import json
import os

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")
POINTS_PER_QUIZ = 20
LINE = "=" * 40

DEFAULT_QUIZZES = [
    {
        "question": "Python에서 화면에 글자를 출력하는 함수는?",
        "options": ["input()", "print()", "len()", "type()"],
        "answer": 2,
    },
    {
        "question": "Python에서 사용자 입력을 받는 함수는?",
        "options": ["print()", "len()", "input()", "type()"],
        "answer": 3,
    },
    {
        "question": "문자열의 길이를 구하는 함수는?",
        "options": ["print()", "input()", "type()", "len()"],
        "answer": 4,
    },
    {
        "question": "Python에서 정수를 나타내는 자료형은?",
        "options": ["str", "float", "int", "bool"],
        "answer": 3,
    },
    {
        "question": "반복 작업에 사용하는 키워드는?",
        "options": ["if", "for", "def", "return"],
        "answer": 2,
    },
]


class Quiz:
    """퀴즈 한 문제를 표현하는 클래스"""

    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer  # 1~4 중 정답 번호

    def display(self, number):
        """문제와 보기를 화면에 출력한다."""
        print(f"\n[문제 {number}]")
        print(self.question)
        print()
        for option_number, option in enumerate(self.options, start=1):
            print(f"{option_number}. {option}")

    def is_correct(self, user_answer):
        """사용자가 고른 번호가 정답인지 확인한다."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 저장용 딕셔너리로 바꾼다."""
        return {
            "question": self.question,
            "options": self.options,
            "answer": self.answer,
        }

    @staticmethod
    def from_dict(data):
        """딕셔너리를 Quiz 객체로 바꾼다. 형식이 잘못되면 ValueError."""
        options = data["options"]
        answer = data["answer"]
        if not isinstance(data["question"], str) or not data["question"].strip():
            raise ValueError("문제가 비어 있습니다.")
        if not isinstance(options, list) or len(options) != 4:
            raise ValueError("선택지는 4개여야 합니다.")
        if not isinstance(answer, int) or not 1 <= answer <= 4:
            raise ValueError("정답은 1~4 사이 숫자여야 합니다.")
        return Quiz(data["question"], options, answer)


class QuizGame:
    """게임 전체(메뉴, 퀴즈, 점수, 저장)를 관리하는 클래스"""

    def __init__(self, state_file=STATE_FILE):
        self.state_file = state_file
        self.quizzes = []
        self.high_score = 0
        self.has_played = False

    # ---------- 저장 / 불러오기 ----------
    def load_state(self):
        """state.json을 읽는다. 없거나 손상되면 기본 데이터를 사용한다."""
        if not os.path.exists(self.state_file):
            print("📂 저장 파일이 없어 기본 퀴즈로 시작합니다.")
            self.use_default_data()
            return

        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                state = json.load(file)
            quizzes = [Quiz.from_dict(item) for item in state["quizzes"]]
            high_score = state["high_score"]
            if not isinstance(high_score, int):
                raise ValueError("최고 점수가 숫자가 아닙니다.")
            self.quizzes = quizzes
            self.high_score = high_score
            self.has_played = state.get("has_played", high_score > 0)
            print(
                f"📂 저장된 데이터를 불러왔습니다. "
                f"(퀴즈 {len(self.quizzes)}개, 최고점수 {self.high_score}점)"
            )
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"⚠️ 저장 파일이 손상되어 기본 데이터로 초기화합니다. ({error})")
            self.use_default_data()
        except OSError as error:
            print(f"⚠️ 파일을 읽을 수 없어 기본 데이터를 사용합니다. ({error})")
            self.quizzes = [Quiz.from_dict(item) for item in DEFAULT_QUIZZES]
            self.high_score = 0

    def use_default_data(self):
        """기본 퀴즈로 초기화하고 파일에 저장한다."""
        self.quizzes = [Quiz.from_dict(item) for item in DEFAULT_QUIZZES]
        self.high_score = 0
        self.has_played = False
        self.save_state()

    def save_state(self):
        """퀴즈와 최고 점수를 state.json에 저장한다."""
        state = {
            "high_score": self.high_score,
            "has_played": self.has_played,
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
        }
           
        try:
            with open(self.state_file, "w", encoding="utf-8") as file:
                json.dump(state, file, ensure_ascii=False, indent=4)
        except OSError as error:
            print(f"⚠️ 파일 저장에 실패했습니다. ({error})")

    # ---------- 입력 처리 ----------
    def read_text(self, prompt):
        """빈 입력이 아닌 글자를 받을 때까지 반복해서 묻는다."""
        while True:
            text = input(prompt).strip()
            if text:
                return text
            print("⚠️ 빈 입력입니다. 내용을 입력해 주세요.")

    def read_number(self, prompt, low, high):
        """low~high 사이의 숫자를 받을 때까지 반복해서 묻는다."""
        while True:
            text = input(prompt).strip()
            if not text:
                print("⚠️ 빈 입력입니다. 숫자를 입력해 주세요.")
                continue
            try:
                number = int(text)
            except ValueError:
                print(f"⚠️ 숫자가 아닙니다. {low}-{high} 사이의 숫자를 입력하세요.")
                continue
            if not low <= number <= high:
                print(f"⚠️ 범위를 벗어났습니다. {low}-{high} 사이의 숫자를 입력하세요.")
                continue
            return number

    # ---------- 메뉴 기능 ----------
    def show_menu(self):
        print("\n" + LINE)
        print("        🐼 핑크판다 파이썬 퀴즈 게임 🐼")
        print(LINE)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print(LINE)

    def play_quiz(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        total = len(self.quizzes)
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")
        correct = 0

        for number, quiz in enumerate(self.quizzes, start=1):
            print("-" * 40)
            quiz.display(number)
            answer = self.read_number("\n정답 입력: ", 1, 4)
            if quiz.is_correct(answer):
                print("✅ 정답입니다!")
                correct += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")

        score = correct * POINTS_PER_QUIZ
        self.has_played = True
        print("\n" + LINE)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")
        if score > self.high_score:
            self.high_score = score
            self.save_state()
            print("🎉 새로운 최고 점수입니다!")
        print(LINE)

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.\n")
        question = self.read_text("문제를 입력하세요: ")
        options = [
            self.read_text(f"선택지 {i}: ") for i in range(1, 5)
        ]
        answer = self.read_number("정답 번호 (1-4): ", 1, 4)

        self.quizzes.append(Quiz(question, options, answer))
        self.save_state()
        print("\n✅ 퀴즈가 추가되었습니다!")

    def list_quizzes(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print("-" * 40)

    def show_high_score(self):
        if not self.has_played and self.high_score == 0:
            print("⚠️ 아직 퀴즈를 풀지 않았습니다. 퀴즈를 먼저 풀어 보세요!")
            return
        total = len(self.quizzes)
        print(f"\n🏆 최고 점수: {self.high_score}점 (만점 {total * POINTS_PER_QUIZ}점 기준)")

    # ---------- 실행 ----------
    def run(self):
        self.load_state()
        try:
            while True:
                self.show_menu()
                choice = self.read_number("선택: ", 1, 5)
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.list_quizzes()
                elif choice == 4:
                    self.show_high_score()
                else:
                    print("🐼 핑크판다 퀴즈 게임을 종료합니다. 안녕히 가세요!")
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ 입력이 중단되었습니다. 데이터를 저장하고 안전하게 종료합니다.")
        finally:
            self.save_state()


def main():
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()