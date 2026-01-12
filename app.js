/**
 * Zuordnungen Lern-App - Standalone Version
 * Komplett im Browser, ohne Server!
 */

// ========== PROGRESS MANAGEMENT ==========
let progress = JSON.parse(localStorage.getItem('mathe7_progress')) || {
    level: 1,
    correct_answers: 0,
    total_attempts: 0,
    quiz_score: 0,
    exercises_completed: 0,
    quiz_completed: false
};

function saveProgress() {
    localStorage.setItem('mathe7_progress', JSON.stringify(progress));
    updateHomeDisplay();
}

function updateHomeDisplay() {
    document.getElementById('home-level').textContent = progress.level;
    document.getElementById('home-level-2').textContent = progress.level;
    document.getElementById('home-correct').textContent = progress.correct_answers;
    document.getElementById('home-exercises').textContent = progress.exercises_completed;

    if (progress.quiz_completed) {
        document.getElementById('quiz-badge').style.display = 'block';
        document.getElementById('quiz-score-badge').textContent = progress.quiz_score;
    }
}

// ========== PAGE NAVIGATION ==========
function showPage(pageId) {
    // Hide all pages
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
    });

    // Show selected page
    document.getElementById(pageId + '-page').classList.add('active');

    // Initialize page-specific content
    if (pageId === 'quiz') initQuiz();
    if (pageId === 'uebungen') initUebungen();
    if (pageId === 'fortschritt') initFortschritt();

    // Scroll to top
    window.scrollTo(0, 0);
}

// ========== TAB NAVIGATION (Theory) ==========
function openTab(evt, tabName) {
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    document.querySelectorAll('.tab-button').forEach(button => {
        button.classList.remove('active');
    });
    document.getElementById(tabName).classList.add('active');
    evt.currentTarget.classList.add('active');
}

// ========== QUIZ LOGIC ==========
let currentQuizQuestion = 0;
let quizScore = 0;
const totalQuizQuestions = 10;
let currentQuestion = null;

const quizQuestions = [
    {
        question: '🛒 Je mehr Äpfel ich kaufe, desto mehr Geld muss ich bezahlen.\\n2 kg kosten 4€, 4 kg kosten 8€.\\n\\nWelche Art von Zuordnung liegt vor?',
        answer: 'proportional',
        explanation: '✓ Richtig! Je mehr Kilogramm, desto höher der Preis.\\nDas Doppelte an Äpfeln kostet das Doppelte.\\nDer Quotient (Preis ÷ kg) bleibt konstant: 4€÷2kg = 2€/kg'
    },
    {
        question: '⏱️ Ein Auto fährt mit konstanter Geschwindigkeit.\\nIn 2 Stunden legt es 120 km zurück, in 4 Stunden 240 km.\\n\\nWelche Zuordnung beschreibt Zeit → Strecke?',
        answer: 'proportional',
        explanation: '✓ Richtig! Bei konstanter Geschwindigkeit gilt:\\nDoppelte Zeit = doppelte Strecke.\\nDer Quotient (Strecke ÷ Zeit) ist konstant: die Geschwindigkeit!'
    },
    {
        question: '🍪 Ein Rezept für 4 Personen benötigt 200g Mehl.\\nFür 8 Personen benötigt man 400g Mehl.\\n\\nWas für eine Zuordnung ist: Anzahl Personen → Mehlmenge?',
        answer: 'proportional',
        explanation: '✓ Richtig! Doppelte Personenzahl = doppelte Zutaten.\\nDas ist eine klassische proportionale Zuordnung.'
    },
    {
        question: '👷 3 Arbeiter brauchen 12 Tage für eine Aufgabe.\\n6 Arbeiter brauchen nur 6 Tage.\\n\\nWelche Zuordnung: Anzahl Arbeiter → Zeit?',
        answer: 'antiproportional',
        explanation: '✓ Richtig! Mehr Arbeiter = weniger Zeit.\\nDas Doppelte an Arbeitern = die halbe Zeit.\\nDas Produkt bleibt konstant: 3×12 = 6×6 = 36'
    },
    {
        question: '🚗 Eine 180 km lange Strecke wird zurückgelegt.\\nMit 60 km/h braucht man 3h, mit 90 km/h nur 2h.\\n\\nWelche Zuordnung: Geschwindigkeit → Zeit?',
        answer: 'antiproportional',
        explanation: '✓ Richtig! Höhere Geschwindigkeit = kürzere Zeit.\\nDas Produkt (Geschwindigkeit × Zeit) bleibt konstant: die Strecke!\\n60×3 = 90×2 = 180 km'
    },
    {
        question: '⚙️ Ein Zahnrad mit 20 Zähnen dreht sich 12 mal pro Minute.\\nEin Zahnrad mit 40 Zähnen dreht sich nur 6 mal pro Minute.\\n\\nWelche Zuordnung: Anzahl Zähne → Drehzahl?',
        answer: 'antiproportional',
        explanation: '✓ Richtig! Mehr Zähne = langsamere Drehung.\\nDas Produkt bleibt konstant: 20×12 = 40×6 = 240'
    },
    {
        question: '🌡️ Die Temperatur in Celsius wird in Fahrenheit umgerechnet.\\n0°C = 32°F, 10°C = 50°F, 20°C = 68°F\\n\\nWelche Zuordnung liegt vor?',
        answer: 'keine',
        explanation: '✓ Richtig! Dies ist weder proportional noch antiproportional.\\nProportional würde bedeuten: 0°C → 0°F (geht durch Ursprung)\\nDie Umrechnung ist linear, aber nicht proportional.'
    },
    {
        question: '📏 Quadrate mit verschiedenen Seitenlängen:\\nSeite 2cm → Fläche 4cm², Seite 3cm → Fläche 9cm²\\n\\nWelche Zuordnung: Seitenlänge → Flächeninhalt?',
        answer: 'keine',
        explanation: '✓ Richtig! Keine proportionale Zuordnung!\\nBei proportional würde gelten: doppelte Seite = doppelte Fläche.\\nAber: doppelte Seite = vierfache Fläche (quadratisch!)'
    },
    {
        question: '💰 Eine Firma hat Grundgebühr + Preis pro Stück:\\n1 Stück: 15€ (10€ + 5€), 2 Stück: 20€ (10€ + 2×5€)\\n\\nWelche Zuordnung: Anzahl → Preis?',
        answer: 'keine',
        explanation: '✓ Richtig! Wegen der Grundgebühr ist es nicht proportional.\\nBei proportional müsste gelten: 0 Stück = 0€.\\nAber hier: 0 Stück = 10€ (Grundgebühr)'
    },
    {
        question: '📊 In einer Tabelle werden Größen zugeordnet:\\n1→3, 2→6, 3→11, 4→18\\n\\nIst der Quotient oder das Produkt konstant?',
        answer: 'keine',
        explanation: '✓ Richtig! Weder Quotient noch Produkt sind konstant.\\nQuotient: 3/1=3, 6/2=3, 11/3≈3.67, 18/4=4.5\\nProdukt: 1×3=3, 2×6=12, 3×11=33, 4×18=72'
    }
];

function initQuiz() {
    currentQuizQuestion = 0;
    quizScore = 0;

    const quizPage = document.getElementById('quiz-page');
    quizPage.innerHTML = `
        <div class="page-header">
            <h1>🎯 Quiz: Zuordnungen erkennen</h1>
            <p>Teste dein Wissen! Erkenne, welche Art von Zuordnung vorliegt.</p>
        </div>

        <div id="quiz-container">
            <div class="quiz-header">
                <div class="quiz-progress">
                    Frage <span id="question-number">1</span> von 10
                </div>
                <div class="quiz-score">
                    Punktzahl: <span id="current-score">0</span>
                </div>
            </div>

            <div id="question-container" class="question-box">
                <p id="question-text"></p>
            </div>

            <div id="answer-buttons" class="answer-buttons">
                <button class="btn btn-answer btn-primary" onclick="submitQuizAnswer('proportional')">
                    📈 Proportional
                </button>
                <button class="btn btn-answer btn-info" onclick="submitQuizAnswer('antiproportional')">
                    📉 Antiproportional
                </button>
                <button class="btn btn-answer btn-secondary" onclick="submitQuizAnswer('keine')">
                    ❌ Weder noch
                </button>
            </div>

            <div id="quiz-result-container" class="result-container" style="display: none;">
                <div id="quiz-result-message" class="result-message"></div>
                <div id="quiz-explanation" class="explanation"></div>
                <button class="btn btn-primary" onclick="nextQuizQuestion()">
                    ➡️ Nächste Frage
                </button>
            </div>

            <div id="quiz-final-result" class="final-result" style="display: none;">
                <h2>🎓 Quiz beendet!</h2>
                <div class="score-display">
                    <div class="score-number" id="final-quiz-score">0</div>
                    <div class="score-label">von 10 Punkten</div>
                </div>
                <div id="quiz-rating" class="rating"></div>
                <div class="action-buttons">
                    <button class="btn btn-primary" onclick="initQuiz()">
                        🔄 Quiz wiederholen
                    </button>
                    <button class="btn btn-success" onclick="showPage('uebungen')">
                        ✏️ Jetzt Übungen machen
                    </button>
                    <button class="btn btn-secondary" onclick="showPage('home')">
                        🏠 Zurück zum Menü
                    </button>
                </div>
            </div>
        </div>
    `;

    loadQuizQuestion();
}

function loadQuizQuestion() {
    if (currentQuizQuestion >= totalQuizQuestions) return;

    currentQuestion = quizQuestions[currentQuizQuestion];
    document.getElementById('question-text').innerHTML = currentQuestion.question.replace(/\\n/g, '<br>');
    document.getElementById('answer-buttons').style.display = 'flex';
    document.getElementById('quiz-result-container').style.display = 'none';
}

function submitQuizAnswer(userAnswer) {
    const isCorrect = (userAnswer === currentQuestion.answer);

    if (isCorrect) {
        quizScore++;
        document.getElementById('current-score').textContent = quizScore;
    }

    showQuizResult(isCorrect);
}

function showQuizResult(isCorrect) {
    document.getElementById('answer-buttons').style.display = 'none';
    document.getElementById('quiz-result-container').style.display = 'block';

    const resultMessage = document.getElementById('quiz-result-message');
    const explanation = document.getElementById('quiz-explanation');

    if (isCorrect) {
        resultMessage.innerHTML = '✅ <strong>Richtig!</strong>';
        resultMessage.className = 'result-message correct';
    } else {
        resultMessage.innerHTML = '❌ <strong>Leider falsch</strong>';
        resultMessage.className = 'result-message incorrect';
    }

    explanation.innerHTML = currentQuestion.explanation.replace(/\\n/g, '<br>');
}

function nextQuizQuestion() {
    currentQuizQuestion++;
    document.getElementById('question-number').textContent = currentQuizQuestion + 1;

    if (currentQuizQuestion >= totalQuizQuestions) {
        finishQuiz();
    } else {
        loadQuizQuestion();
    }
}

function finishQuiz() {
    progress.quiz_score = quizScore;
    progress.quiz_completed = true;
    saveProgress();

    document.getElementById('quiz-container').querySelector('.quiz-header').style.display = 'none';
    document.getElementById('question-container').style.display = 'none';
    document.getElementById('answer-buttons').style.display = 'none';
    document.getElementById('quiz-result-container').style.display = 'none';
    document.getElementById('quiz-final-result').style.display = 'block';

    document.getElementById('final-quiz-score').textContent = quizScore;

    const percentage = (quizScore / totalQuizQuestions) * 100;
    const rating = document.getElementById('quiz-rating');

    if (percentage >= 90) {
        rating.innerHTML = '<p class="rating-excellent">🌟 Ausgezeichnet! Du bist ein Profi!</p>';
    } else if (percentage >= 70) {
        rating.innerHTML = '<p class="rating-good">👍 Sehr gut! Du hast es verstanden!</p>';
    } else if (percentage >= 50) {
        rating.innerHTML = '<p class="rating-ok">✓ Gut! Übe noch ein bisschen!</p>';
    } else {
        rating.innerHTML = '<p class="rating-practice">💪 Nicht aufgeben! Lies nochmal die Theorie!</p>';
    }
}

// ========== EXERCISES LOGIC ==========
let currentExercise = null;

const exercises = {
    1: [
        {
            question: '🥚 5 Eier kosten 2,50€.\\nWie viel kosten 7 Eier?',
            answer: 3.50,
            unit: '€',
            tolerance: 0.01,
            hint: '1. Rechne aus, was 1 Ei kostet: 2,50€ ÷ 5\\n2. Multipliziere mit 7',
            solution: 'Lösung:\\n1 Ei kostet: 2,50€ ÷ 5 = 0,50€\\n7 Eier kosten: 0,50€ × 7 = 3,50€'
        },
        {
            question: '🍎 3 kg Äpfel kosten 6,00€.\\nWie viel kosten 5 kg?',
            answer: 10.00,
            unit: '€',
            tolerance: 0.01,
            hint: '1. Berechne den Preis für 1 kg\\n2. Multipliziere mit 5',
            solution: 'Lösung:\\n1 kg kostet: 6,00€ ÷ 3 = 2,00€\\n5 kg kosten: 2,00€ × 5 = 10,00€'
        },
        {
            question: '⏱️ In 3 Stunden werden 180 km zurückgelegt.\\nWie viele km in 5 Stunden (bei gleicher Geschwindigkeit)?',
            answer: 300,
            unit: 'km',
            tolerance: 1,
            hint: '1. Berechne die km pro Stunde\\n2. Multipliziere mit 5',
            solution: 'Lösung:\\nPro Stunde: 180 km ÷ 3 = 60 km/h\\nIn 5 Stunden: 60 km/h × 5 = 300 km'
        }
    ],
    2: [
        {
            question: '📦 8 Pakete wiegen zusammen 12 kg.\\nWie viel wiegen 13 Pakete?',
            answer: 19.5,
            unit: 'kg',
            tolerance: 0.1,
            hint: '1. Berechne das Gewicht von 1 Paket\\n2. Multipliziere mit 13',
            solution: 'Lösung:\\n1 Paket wiegt: 12 kg ÷ 8 = 1,5 kg\\n13 Pakete wiegen: 1,5 kg × 13 = 19,5 kg'
        },
        {
            question: '💶 Für 6 Arbeitsstunden erhält man 78€.\\nWie viel erhält man für 9 Stunden?',
            answer: 117,
            unit: '€',
            tolerance: 0.5,
            hint: 'Berechne erst den Stundenlohn',
            solution: 'Lösung:\\nStundenlohn: 78€ ÷ 6 = 13€/h\\nFür 9 Stunden: 13€ × 9 = 117€'
        }
    ],
    3: [
        {
            question: '👷 4 Arbeiter brauchen 6 Tage für eine Aufgabe.\\nWie lange brauchen 8 Arbeiter?',
            answer: 3,
            unit: 'Tage',
            tolerance: 0.1,
            hint: '1. Berechne das Produkt: 4 × 6\\n2. Teile durch 8',
            solution: 'Lösung:\\nProdukt: 4 Arbeiter × 6 Tage = 24\\nZeit für 8 Arbeiter: 24 ÷ 8 = 3 Tage'
        },
        {
            question: '🚗 Mit 60 km/h dauert eine Fahrt 4 Stunden.\\nWie lange dauert sie mit 80 km/h?',
            answer: 3,
            unit: 'Stunden',
            tolerance: 0.1,
            hint: 'Das Produkt Geschwindigkeit × Zeit ist die Strecke (konstant)',
            solution: 'Lösung:\\nStrecke: 60 km/h × 4 h = 240 km\\nZeit: 240 km ÷ 80 km/h = 3 Stunden'
        }
    ],
    4: [
        {
            question: '⚙️ 3 Pumpen füllen einen Pool in 12 Stunden.\\nWie lange brauchen 9 Pumpen?',
            answer: 4,
            unit: 'Stunden',
            tolerance: 0.1,
            hint: 'Mehr Pumpen → weniger Zeit (antiproportional)',
            solution: 'Lösung:\\nProdukt: 3 × 12 = 36\\nZeit: 36 ÷ 9 = 4 Stunden'
        },
        {
            question: '🍰 Ein Rezept für 6 Personen benötigt 450g Zucker.\\nWie viel Zucker für 10 Personen?',
            answer: 750,
            unit: 'g',
            tolerance: 5,
            hint: 'Mehr Personen → mehr Zutaten (proportional)',
            solution: 'Lösung:\\nPro Person: 450g ÷ 6 = 75g\\nFür 10 Personen: 75g × 10 = 750g'
        }
    ],
    5: [
        {
            question: '🏭 6 Maschinen produzieren in 8 Stunden 1440 Teile.\\nWie viele Teile produzieren 4 Maschinen in 12 Stunden?',
            answer: 1440,
            unit: 'Teile',
            tolerance: 10,
            hint: 'Rechne erst aus, wie viele Teile 1 Maschine in 1 Stunde macht',
            solution: 'Lösung:\\n1 Maschine in 1 Stunde: 1440 ÷ 6 ÷ 8 = 30 Teile/h\\n4 Maschinen in 12 Stunden: 30 × 4 × 12 = 1440 Teile'
        },
        {
            question: '📏 Eine Karte hat den Maßstab 1:50000.\\nWie lang ist eine Strecke in Wirklichkeit, die auf der Karte 7,5 cm misst?',
            answer: 3.75,
            unit: 'km',
            tolerance: 0.1,
            hint: '1 cm auf der Karte = 50000 cm in Wirklichkeit',
            solution: 'Lösung:\\n7,5 cm × 50000 = 375000 cm = 3750 m = 3,75 km'
        }
    ]
};

function initUebungen() {
    const uebungenPage = document.getElementById('uebungen-page');
    uebungenPage.innerHTML = `
        <div class="page-header">
            <h1>✏️ Rechenübungen</h1>
            <p>Übe mit dem Dreisatz - die Aufgaben passen sich deinem Level an!</p>
        </div>

        <div class="level-display">
            <span class="level-badge">Level <span id="current-exercise-level">${progress.level}</span></span>
            <span class="level-info">Die Schwierigkeit passt sich automatisch an deine Leistung an</span>
        </div>

        <div id="exercise-container">
            <div id="exercise-question-container" class="exercise-box">
                <p id="exercise-question"></p>
            </div>

            <div id="exercise-answer-form" class="answer-form">
                <label for="exercise-answer-input">Deine Antwort:</label>
                <div class="input-group">
                    <input type="number" id="exercise-answer-input" step="0.01" placeholder="Ergebnis eingeben">
                    <span id="exercise-unit-display"></span>
                </div>
                <div class="button-group">
                    <button class="btn btn-primary" onclick="checkExerciseAnswer()">
                        ✓ Prüfen
                    </button>
                    <button class="btn btn-info" onclick="showExerciseHint()">
                        💡 Tipp
                    </button>
                    <button class="btn btn-secondary" onclick="loadNewExercise()">
                        ⏭️ Überspringen
                    </button>
                </div>
            </div>

            <div id="exercise-result-container" class="result-container" style="display: none;">
                <div id="exercise-result-message" class="result-message"></div>
                <div id="exercise-solution-display" class="solution-display"></div>
                <div id="exercise-level-change" class="level-change-message" style="display: none;"></div>
                <div class="button-group">
                    <button class="btn btn-primary" onclick="loadNewExercise()">
                        ➡️ Nächste Aufgabe
                    </button>
                    <button class="btn btn-secondary" onclick="tryAgainExercise()">
                        🔄 Nochmal versuchen
                    </button>
                </div>
            </div>
        </div>

        <div class="action-buttons">
            <button class="btn btn-info" onclick="showPage('fortschritt')">📊 Fortschritt ansehen</button>
            <button class="btn btn-secondary" onclick="showPage('home')">🏠 Zurück zum Menü</button>
        </div>
    `;

    loadNewExercise();

    // Enter key support
    document.getElementById('exercise-answer-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') checkExerciseAnswer();
    });
}

function loadNewExercise() {
    const level = progress.level;
    const levelExercises = exercises[level] || exercises[1];
    currentExercise = levelExercises[Math.floor(Math.random() * levelExercises.length)];

    document.getElementById('exercise-question').innerHTML = currentExercise.question.replace(/\\n/g, '<br>');
    document.getElementById('exercise-unit-display').textContent = currentExercise.unit || '';
    document.getElementById('exercise-answer-input').value = '';
    document.getElementById('exercise-answer-input').focus();
    document.getElementById('exercise-answer-form').style.display = 'block';
    document.getElementById('exercise-result-container').style.display = 'none';
}

function checkExerciseAnswer() {
    const userAnswerStr = document.getElementById('exercise-answer-input').value;

    if (!userAnswerStr) {
        alert('Bitte gib eine Antwort ein!');
        return;
    }

    const userAnswer = parseFloat(userAnswerStr.replace(',', '.'));
    const isCorrect = Math.abs(userAnswer - currentExercise.answer) <= currentExercise.tolerance;

    progress.total_attempts++;

    if (isCorrect) {
        progress.correct_answers++;
        progress.exercises_completed++;
    }

    // Level adjustment
    let levelChange = null;
    if (progress.total_attempts > 0) {
        const successRate = progress.correct_answers / progress.total_attempts;

        if (isCorrect && successRate > 0.7 && progress.exercises_completed % 3 === 0 && progress.level < 5) {
            progress.level++;
            levelChange = {type: 'up', message: `Level Up! Du bist jetzt Level ${progress.level}! 🎉`};
            document.getElementById('current-exercise-level').textContent = progress.level;
        } else if (!isCorrect && progress.total_attempts > 5 && successRate < 0.4 && progress.level > 1) {
            progress.level--;
            levelChange = {type: 'down', message: `Kein Problem! Wir üben mit einfacheren Aufgaben. Level ${progress.level}`};
            document.getElementById('current-exercise-level').textContent = progress.level;
        }
    }

    saveProgress();
    showExerciseResult(isCorrect, userAnswer, levelChange);
}

function showExerciseResult(isCorrect, userAnswer, levelChange) {
    document.getElementById('exercise-answer-form').style.display = 'none';
    document.getElementById('exercise-result-container').style.display = 'block';

    const resultMessage = document.getElementById('exercise-result-message');
    const solutionDisplay = document.getElementById('exercise-solution-display');
    const levelChangeEl = document.getElementById('exercise-level-change');

    if (isCorrect) {
        resultMessage.innerHTML = '✅ <strong>Richtig! Sehr gut!</strong>';
        resultMessage.className = 'result-message correct';
    } else {
        resultMessage.innerHTML = `❌ <strong>Leider nicht richtig</strong><br>
            Deine Antwort: ${userAnswer}<br>
            Richtige Antwort: ${currentExercise.answer}`;
        resultMessage.className = 'result-message incorrect';
    }

    solutionDisplay.innerHTML = '<h3>📝 Lösungsweg:</h3>' +
        currentExercise.solution.replace(/\\n/g, '<br>');

    if (levelChange) {
        levelChangeEl.innerHTML = levelChange.type === 'up'
            ? `🎉 <strong>${levelChange.message}</strong>`
            : `ℹ️ <strong>${levelChange.message}</strong>`;
        levelChangeEl.className = 'level-change-message level-' + levelChange.type;
        levelChangeEl.style.display = 'block';
    } else {
        levelChangeEl.style.display = 'none';
    }
}

function showExerciseHint() {
    alert('💡 Tipp:\\n\\n' + currentExercise.hint.replace(/\\n/g, '\\n'));
}

function tryAgainExercise() {
    document.getElementById('exercise-answer-form').style.display = 'block';
    document.getElementById('exercise-result-container').style.display = 'none';
    document.getElementById('exercise-answer-input').value = '';
    document.getElementById('exercise-answer-input').focus();
}

// ========== PROGRESS PAGE ==========
function initFortschritt() {
    const fortschrittPage = document.getElementById('fortschritt-page');

    const successRate = progress.total_attempts > 0
        ? ((progress.correct_answers / progress.total_attempts) * 100).toFixed(1)
        : 0;

    let motivation = '';
    let motivationClass = '';

    if (progress.level === 5 && progress.exercises_completed > 10) {
        motivation = '🌟 Fantastisch! Du bist ein Zuordnungs-Experte!';
        motivationClass = 'excellent';
    } else if (progress.level >= 3) {
        motivation = '👍 Super! Du machst große Fortschritte!';
        motivationClass = 'good';
    } else if (progress.exercises_completed > 5) {
        motivation = '✨ Weiter so! Übung macht den Meister!';
        motivationClass = 'ok';
    } else {
        motivation = '💪 Gut gestartet! Bleib dran!';
        motivationClass = 'start';
    }

    fortschrittPage.innerHTML = `
        <div class="page-header">
            <h1>📊 Dein Fortschritt</h1>
            <p>Sieh dir deine Leistungen und Erfolge an!</p>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-icon">🎯</div>
                <div class="stat-value">${progress.level}</div>
                <div class="stat-label">Aktuelles Level</div>
                <div class="stat-sublabel">von 5</div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">✅</div>
                <div class="stat-value">${progress.correct_answers}</div>
                <div class="stat-label">Richtige Antworten</div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">📝</div>
                <div class="stat-value">${progress.total_attempts}</div>
                <div class="stat-label">Gesamte Versuche</div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">📋</div>
                <div class="stat-value">${progress.exercises_completed}</div>
                <div class="stat-label">Abgeschlossene Übungen</div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">🎯</div>
                <div class="stat-value">${progress.quiz_score}/10</div>
                <div class="stat-label">Quiz Punktzahl</div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">📈</div>
                <div class="stat-value">${successRate}%</div>
                <div class="stat-label">Erfolgsquote</div>
            </div>
        </div>

        <div class="motivation-message ${motivationClass}">${motivation}</div>

        <div class="progress-details">
            <h2>🎓 Level-Übersicht</h2>
            <div class="level-progress">
                <div class="level-item ${progress.level >= 1 ? 'completed' : ''}">
                    <div class="level-number">1</div>
                    <div class="level-description">
                        <strong>Level 1 - Einfach</strong>
                        <p>Einfache proportionale Aufgaben</p>
                    </div>
                </div>
                <div class="level-item ${progress.level >= 2 ? 'completed' : ''}">
                    <div class="level-number">2</div>
                    <div class="level-description">
                        <strong>Level 2 - Mittel</strong>
                        <p>Schwierigere Zahlen und Dezimalstellen</p>
                    </div>
                </div>
                <div class="level-item ${progress.level >= 3 ? 'completed' : ''}">
                    <div class="level-number">3</div>
                    <div class="level-description">
                        <strong>Level 3 - Fortgeschritten</strong>
                        <p>Antiproportionale Zuordnungen</p>
                    </div>
                </div>
                <div class="level-item ${progress.level >= 4 ? 'completed' : ''}">
                    <div class="level-number">4</div>
                    <div class="level-description">
                        <strong>Level 4 - Schwer</strong>
                        <p>Gemischte Aufgaben</p>
                    </div>
                </div>
                <div class="level-item ${progress.level >= 5 ? 'completed' : ''}">
                    <div class="level-number">5</div>
                    <div class="level-description">
                        <strong>Level 5 - Experte</strong>
                        <p>Komplexe Mehrschritt-Aufgaben</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="action-buttons">
            <button class="btn btn-danger" onclick="resetProgress()">
                🔄 Fortschritt zurücksetzen
            </button>
            <button class="btn btn-success" onclick="showPage('uebungen')">
                ✏️ Weiter üben
            </button>
            <button class="btn btn-secondary" onclick="showPage('home')">
                🏠 Zurück zum Menü
            </button>
        </div>
    `;
}

function resetProgress() {
    if (confirm('Möchtest du wirklich deinen gesamten Fortschritt zurücksetzen?')) {
        localStorage.removeItem('mathe7_progress');
        progress = {
            level: 1,
            correct_answers: 0,
            total_attempts: 0,
            quiz_score: 0,
            exercises_completed: 0,
            quiz_completed: false
        };
        saveProgress();
        alert('Fortschritt wurde zurückgesetzt!');
        showPage('home');
    }
}

// ========== INITIALIZATION ==========
document.addEventListener('DOMContentLoaded', function() {
    updateHomeDisplay();
});
