
const quizzes = [
    {
        question: "Python에서 화면에 글자를 출력하는 함수는?",
        options: [
            "input()",
            "print()",
            "len()",
            "type()"
        ],
        answer: 2,
        hint: "파이썬에서 화면에 메시지를 보여줄 때 사용하는 함수를 떠올려 보세요."
    },
    {
        question: "Python에서 사용자 입력을 받는 함수는?",
        options: [
            "print()",
            "len()",
            "input()",
            "type()"
        ],
        answer: 3,
        hint: "사용자에게 질문하고 키보드 입력을 받을 때 사용하는 함수를 생각해 보세요."
    },
    {
        question: "Python에서 문자열의 길이를 구하는 함수는?",
        options: [
            "print()",
            "input()",
            "type()",
            "len()"
        ],
        answer: 4,
        hint: "문자열에 글자가 몇 개 들어 있는지 확인하는 상황을 생각해 보세요."
    },
    {
        question: "Python에서 정수를 나타내는 자료형은?",
        options: [
            "str",
            "float",
            "int",
            "bool"
        ],
        answer: 3,
        hint: "소수점이 없는 숫자를 저장하는 자료형을 생각해 보세요."
    },
    {
        question: "Python에서 반복 작업을 수행할 때 사용하는 키워드는?",
        options: [
            "if",
            "for",
            "def",
            "return"
        ],
        answer: 2,
        hint: "같은 작업을 여러 번 반복할 때 사용하는 세 글자 키워드를 생각해 보세요."
    }
];

const storedQuizzes = JSON.parse(
    localStorage.getItem("pinkPandaSavedQuizzes") || "[]"
);

quizzes.push(...storedQuizzes);


document.getElementById("start-button").addEventListener("click", function() {
    quizzes.sort(() => Math.random() - 0.5);
    currentQuestion = 0;
    score = 0;

document.getElementById("next-button").style.display = "block";
document.getElementById("score-display").textContent = "🏆 현재 점수: 0점";

    document.getElementById("main-menu").style.display = "none";
    document.getElementById("quiz-screen").style.display = "block";

    document.getElementById("quiz-result").textContent = "";
    document.getElementById("quiz-hint").style.display = "none";

    showQuestion();
});



let currentQuestion = 0;
let score = 0;
let highScore = Number(localStorage.getItem("pinkPandaHighScore")) || 0;
let answered = false;
function showQuestion() {
    answered = false;
    const question = quizzes[currentQuestion];

    document.getElementById("question-number").textContent =
        "📝 " + (currentQuestion + 1) + "번 문제";

    document.getElementById("question-text").textContent =
        question.question;

    const optionsElement =
        document.getElementById("answer-options");

    optionsElement.innerHTML = "";

    question.options.forEach(function(option, index) {
        const button = document.createElement("button");

        button.textContent = (index + 1) + ". " + option;

button.addEventListener("click", function() {
    if (answered) {
        retuern;
    }

    answered = true;
    const resultElement = document.getElementById("quiz-result");

    if (index + 1 === question.answer) {
        score += 10;

if (score > highScore) {
    highScore = score;
    localStorage.setItem("pinkPandaHighScore", highScore);
}

document.getElementById("score-display").textContent =
    "🏆 현재 점수: " + score + "점";
        resultElement.textContent = "🎉 정답입니다!";
        resultElement.style.color = "green";
    } else {
        resultElement.textContent = "❌ 오답입니다!";
        resultElement.style.color = "red";
    }
});

        optionsElement.appendChild(button);
    });
}

showQuestion();

document.getElementById("hint-button").addEventListener("click", function() {
    const question = quizzes[currentQuestion];
    const hintElement = document.getElementById("quiz-hint");

    hintElement.textContent = "💡 힌트: " + question.hint;
    hintElement.style.display = "block";
});

document.getElementById("next-button").addEventListener("click", function() {
    if (currentQuestion < quizzes.length - 1) {
        currentQuestion++;

        showQuestion();

        document.getElementById("quiz-result").textContent = "";
        document.getElementById("quiz-hint").style.display = "none";
   
} else {
    document.getElementById("quiz-result").textContent =
        "🎉 모든 퀴즈를 완료했습니다! 최종 점수: " + score + "점";
        document.getElementById("next-button").style.display = "none";
}

});

document.getElementById("home-button").addEventListener("click", function() {
    document.getElementById("quiz-screen").style.display = "none";
    document.getElementById("main-menu").style.display = "block";

    currentQuestion = 0;
    score = 0;
    document.getElementById("score-display").textContent =
        "🏆 현재 점수: 0점";
    document.getElementById("quiz-result").textContent = "";
    document.getElementById("quiz-hint").style.display = "none";
});
document.getElementById("high-score-button").addEventListener("click", function() {
    highScore = Number(localStorage.getItem("pinkPandaHighScore")) || 0;

    document.getElementById("main-menu").style.display = "none";
    document.getElementById("high-score-screen").style.display = "block";

    document.getElementById("high-score-display").textContent =
        highScore + "점";
});

document.getElementById("high-score-home-button").addEventListener("click", function() {
    document.getElementById("high-score-screen").style.display = "none";
    document.getElementById("main-menu").style.display = "block";
});

document.getElementById("add-quiz-button").addEventListener("click", function() {
    document.getElementById("main-menu").style.display = "none";
    document.getElementById("add-quiz-screen").style.display = "block";
});

document.getElementById("add-quiz-home-button").addEventListener("click", function() {
    document.getElementById("add-quiz-screen").style.display = "none";
    document.getElementById("main-menu").style.display = "block";
});

document.getElementById("save-quiz-button").addEventListener("click", function() {
    const newQuestion = document.getElementById("new-question").value.trim();

const newOptions = [
    document.getElementById("new-option1").value.trim(),
    document.getElementById("new-option2").value.trim(),
    document.getElementById("new-option3").value.trim(),
    document.getElementById("new-option4").value.trim()
];

const newAnswer = Number(document.getElementById("new-answer").value);

const newHint = document.getElementById("new-hint").value.trim();



    
if (!newQuestion || newOptions.some(option => option === "") || !newHint) {
    document.getElementById("add-quiz-message").textContent =
        "⚠️ 문제, 보기 4개, 힌트를 모두 입력해 주세요!";
    return;
}

if (!Number.isInteger(newAnswer) || newAnswer < 1 || newAnswer > 4) {
    document.getElementById("add-quiz-message").textContent =
        "⚠️ 정답 번호는 1부터 4까지 입력해 주세요!";
    return;
}

quizzes.push({
    question: newQuestion,
    options: newOptions,
    answer: newAnswer,
    hint: newHint
});

const savedQuizzes = JSON.parse(
    localStorage.getItem("pinkPandaSavedQuizzes") || "[]"
);

savedQuizzes.push({
    question: newQuestion,
    options: newOptions,
    answer: newAnswer,
    hint: newHint
});

localStorage.setItem(
    "pinkPandaSavedQuizzes",
    JSON.stringify(savedQuizzes)
);

console.log("🐼 퀴즈 저장 완료:", savedQuizzes);


document.getElementById("add-quiz-message").textContent =
    "🎉 새로운 퀴즈가 성공적으로 추가되었어요!";

 });

document.getElementById("quiz-list-button").addEventListener("click", function() {
    document.getElementById("main-menu").style.display = "none";
    document.getElementById("quiz-list-screen").style.display = "block";

    showQuizList();

});

function showQuizList() {

    const quizCount = document.getElementById("quiz-count");
    quizCount.textContent = "📚 전체 퀴즈: " + quizzes.length + "문제";

    const listContainer = document.getElementById("quiz-list-container");

    listContainer.innerHTML = "";

    quizzes.forEach(function(quiz, index) {
        const questionElement = document.createElement("p");

        questionElement.style.backgroundColor = "#ffe4ef";
        questionElement.style.padding = "15px";
        questionElement.style.borderRadius = "12px";
        questionElement.style.marginBottom = "12px";

        questionElement.textContent =
            "📝 " + (index + 1) + "번. " + quiz.question;

        listContainer.appendChild(questionElement);

const optionsElement = document.createElement("div");

quiz.options.forEach(function(option, optionIndex) {
    const optionElement = document.createElement("p");

    optionElement.textContent =
        (optionIndex + 1) + ". " + option;

    optionElement.style.marginLeft = "20px";
    optionElement.style.marginBottom = "8px";

    optionsElement.appendChild(optionElement);
});

listContainer.appendChild(optionsElement);

    });
}

document.getElementById("quiz-list-home-button").addEventListener("click", function() {
    document.getElementById("quiz-list-screen").style.display = "none";
    document.getElementById("main-menu").style.display = "block";
});

