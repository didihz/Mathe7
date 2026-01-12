"""
Zuordnungen Lern-App - Web Version
Eine interaktive Browser-Anwendung zum Lernen von Zuordnungen
"""

from flask import Flask, render_template, jsonify, request, session
import random
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'mathe7_zuordnungen_secret_key_2024'


# Datenbank-Ersatz: Fortschritt in Session speichern
def get_progress():
    """Hole Fortschritt aus Session"""
    if 'progress' not in session:
        session['progress'] = {
            'level': 1,
            'correct_answers': 0,
            'total_attempts': 0,
            'quiz_score': 0,
            'exercises_completed': 0,
            'quiz_completed': False
        }
    return session['progress']


def save_progress(progress):
    """Speichere Fortschritt in Session"""
    session['progress'] = progress
    session.modified = True


# Routen
@app.route('/')
def index():
    """Hauptseite / Menü"""
    progress = get_progress()
    return render_template('index.html', progress=progress)


@app.route('/theorie')
def theorie():
    """Theorie-Seite"""
    return render_template('theorie.html')


@app.route('/quiz')
def quiz():
    """Quiz-Seite"""
    return render_template('quiz.html')


@app.route('/uebungen')
def uebungen():
    """Übungs-Seite"""
    progress = get_progress()
    return render_template('uebungen.html', level=progress['level'])


@app.route('/fortschritt')
def fortschritt():
    """Fortschritts-Seite"""
    progress = get_progress()
    return render_template('fortschritt.html', progress=progress)


# API Endpoints
@app.route('/api/quiz_question', methods=['GET'])
def get_quiz_question():
    """Generiere eine Quiz-Frage"""
    questions = [
        {
            'question': '🛒 Je mehr Äpfel ich kaufe, desto mehr Geld muss ich bezahlen.\n2 kg kosten 4€, 4 kg kosten 8€.\n\nWelche Art von Zuordnung liegt vor?',
            'answer': 'proportional',
            'explanation': '✓ Richtig! Je mehr Kilogramm, desto höher der Preis.\nDas Doppelte an Äpfeln kostet das Doppelte.\nDer Quotient (Preis ÷ kg) bleibt konstant: 4€÷2kg = 2€/kg'
        },
        {
            'question': '⏱️ Ein Auto fährt mit konstanter Geschwindigkeit.\nIn 2 Stunden legt es 120 km zurück, in 4 Stunden 240 km.\n\nWelche Zuordnung beschreibt Zeit → Strecke?',
            'answer': 'proportional',
            'explanation': '✓ Richtig! Bei konstanter Geschwindigkeit gilt:\nDoppelte Zeit = doppelte Strecke.\nDer Quotient (Strecke ÷ Zeit) ist konstant: die Geschwindigkeit!'
        },
        {
            'question': '🍪 Ein Rezept für 4 Personen benötigt 200g Mehl.\nFür 8 Personen benötigt man 400g Mehl.\n\nWas für eine Zuordnung ist: Anzahl Personen → Mehlmenge?',
            'answer': 'proportional',
            'explanation': '✓ Richtig! Doppelte Personenzahl = doppelte Zutaten.\nDas ist eine klassische proportionale Zuordnung.'
        },
        {
            'question': '👷 3 Arbeiter brauchen 12 Tage für eine Aufgabe.\n6 Arbeiter brauchen nur 6 Tage.\n\nWelche Zuordnung: Anzahl Arbeiter → Zeit?',
            'answer': 'antiproportional',
            'explanation': '✓ Richtig! Mehr Arbeiter = weniger Zeit.\nDas Doppelte an Arbeitern = die halbe Zeit.\nDas Produkt bleibt konstant: 3×12 = 6×6 = 36'
        },
        {
            'question': '🚗 Eine 180 km lange Strecke wird zurückgelegt.\nMit 60 km/h braucht man 3h, mit 90 km/h nur 2h.\n\nWelche Zuordnung: Geschwindigkeit → Zeit?',
            'answer': 'antiproportional',
            'explanation': '✓ Richtig! Höhere Geschwindigkeit = kürzere Zeit.\nDas Produkt (Geschwindigkeit × Zeit) bleibt konstant: die Strecke!\n60×3 = 90×2 = 180 km'
        },
        {
            'question': '⚙️ Ein Zahnrad mit 20 Zähnen dreht sich 12 mal pro Minute.\nEin Zahnrad mit 40 Zähnen dreht sich nur 6 mal pro Minute.\n\nWelche Zuordnung: Anzahl Zähne → Drehzahl?',
            'answer': 'antiproportional',
            'explanation': '✓ Richtig! Mehr Zähne = langsamere Drehung.\nDas Produkt bleibt konstant: 20×12 = 40×6 = 240'
        },
        {
            'question': '🌡️ Die Temperatur in Celsius wird in Fahrenheit umgerechnet.\n0°C = 32°F, 10°C = 50°F, 20°C = 68°F\n\nWelche Zuordnung liegt vor?',
            'answer': 'keine',
            'explanation': '✓ Richtig! Dies ist weder proportional noch antiproportional.\nProportional würde bedeuten: 0°C → 0°F (geht durch Ursprung)\nDie Umrechnung ist linear, aber nicht proportional.'
        },
        {
            'question': '📏 Quadrate mit verschiedenen Seitenlängen:\nSeite 2cm → Fläche 4cm², Seite 3cm → Fläche 9cm²\n\nWelche Zuordnung: Seitenlänge → Flächeninhalt?',
            'answer': 'keine',
            'explanation': '✓ Richtig! Keine proportionale Zuordnung!\nBei proportional würde gelten: doppelte Seite = doppelte Fläche.\nAber: doppelte Seite = vierfache Fläche (quadratisch!)'
        },
        {
            'question': '💰 Eine Firma hat Grundgebühr + Preis pro Stück:\n1 Stück: 15€ (10€ + 5€), 2 Stück: 20€ (10€ + 2×5€)\n\nWelche Zuordnung: Anzahl → Preis?',
            'answer': 'keine',
            'explanation': '✓ Richtig! Wegen der Grundgebühr ist es nicht proportional.\nBei proportional müsste gelten: 0 Stück = 0€.\nAber hier: 0 Stück = 10€ (Grundgebühr)'
        },
        {
            'question': '📊 In einer Tabelle werden Größen zugeordnet:\n1→3, 2→6, 3→11, 4→18\n\nIst der Quotient oder das Produkt konstant?',
            'answer': 'keine',
            'explanation': '✓ Richtig! Weder Quotient noch Produkt sind konstant.\nQuotient: 3/1=3, 6/2=3, 11/3≈3.67, 18/4=4.5\nProdukt: 1×3=3, 2×6=12, 3×11=33, 4×18=72'
        },
    ]

    return jsonify(random.choice(questions))


@app.route('/api/check_quiz_answer', methods=['POST'])
def check_quiz_answer():
    """Prüfe Quiz-Antwort"""
    data = request.json
    user_answer = data.get('answer')
    correct_answer = data.get('correct_answer')

    is_correct = (user_answer == correct_answer)

    # Update Fortschritt
    progress = get_progress()
    if is_correct:
        progress['quiz_score'] += 1

    save_progress(progress)

    return jsonify({'correct': is_correct})


@app.route('/api/finish_quiz', methods=['POST'])
def finish_quiz():
    """Beende Quiz"""
    progress = get_progress()
    progress['quiz_completed'] = True
    save_progress(progress)
    return jsonify({'success': True, 'score': progress['quiz_score']})


@app.route('/api/reset_quiz', methods=['POST'])
def reset_quiz():
    """Setze Quiz zurück"""
    progress = get_progress()
    progress['quiz_score'] = 0
    progress['quiz_completed'] = False
    save_progress(progress)
    return jsonify({'success': True})


@app.route('/api/exercise', methods=['GET'])
def get_exercise():
    """Generiere Übungsaufgabe basierend auf Level"""
    progress = get_progress()
    level = progress['level']

    exercises = []

    # Level 1: Einfache proportionale Aufgaben
    if level >= 1:
        exercises.extend([
            {
                'question': '🥚 5 Eier kosten 2,50€.\nWie viel kosten 7 Eier?',
                'answer': 3.50,
                'unit': '€',
                'tolerance': 0.01,
                'hint': '1. Rechne aus, was 1 Ei kostet: 2,50€ ÷ 5\n2. Multipliziere mit 7',
                'solution': 'Lösung:\n1 Ei kostet: 2,50€ ÷ 5 = 0,50€\n7 Eier kosten: 0,50€ × 7 = 3,50€'
            },
            {
                'question': '🍎 3 kg Äpfel kosten 6,00€.\nWie viel kosten 5 kg?',
                'answer': 10.00,
                'unit': '€',
                'tolerance': 0.01,
                'hint': '1. Berechne den Preis für 1 kg\n2. Multipliziere mit 5',
                'solution': 'Lösung:\n1 kg kostet: 6,00€ ÷ 3 = 2,00€\n5 kg kosten: 2,00€ × 5 = 10,00€'
            },
            {
                'question': '⏱️ In 3 Stunden werden 180 km zurückgelegt.\nWie viele km in 5 Stunden (bei gleicher Geschwindigkeit)?',
                'answer': 300,
                'unit': 'km',
                'tolerance': 1,
                'hint': '1. Berechne die km pro Stunde\n2. Multipliziere mit 5',
                'solution': 'Lösung:\nPro Stunde: 180 km ÷ 3 = 60 km/h\nIn 5 Stunden: 60 km/h × 5 = 300 km'
            }
        ])

    # Level 2: Schwierigere proportionale Aufgaben
    if level >= 2:
        exercises.extend([
            {
                'question': '📦 8 Pakete wiegen zusammen 12 kg.\nWie viel wiegen 13 Pakete?',
                'answer': 19.5,
                'unit': 'kg',
                'tolerance': 0.1,
                'hint': '1. Berechne das Gewicht von 1 Paket\n2. Multipliziere mit 13',
                'solution': 'Lösung:\n1 Paket wiegt: 12 kg ÷ 8 = 1,5 kg\n13 Pakete wiegen: 1,5 kg × 13 = 19,5 kg'
            },
            {
                'question': '💶 Für 6 Arbeitsstunden erhält man 78€.\nWie viel erhält man für 9 Stunden?',
                'answer': 117,
                'unit': '€',
                'tolerance': 0.5,
                'hint': 'Berechne erst den Stundenlohn',
                'solution': 'Lösung:\nStundenlohn: 78€ ÷ 6 = 13€/h\nFür 9 Stunden: 13€ × 9 = 117€'
            }
        ])

    # Level 3: Antiproportionale Aufgaben
    if level >= 3:
        exercises.extend([
            {
                'question': '👷 4 Arbeiter brauchen 6 Tage für eine Aufgabe.\nWie lange brauchen 8 Arbeiter?',
                'answer': 3,
                'unit': 'Tage',
                'tolerance': 0.1,
                'hint': '1. Berechne das Produkt: 4 × 6\n2. Teile durch 8',
                'solution': 'Lösung:\nProdukt: 4 Arbeiter × 6 Tage = 24\nZeit für 8 Arbeiter: 24 ÷ 8 = 3 Tage'
            },
            {
                'question': '🚗 Mit 60 km/h dauert eine Fahrt 4 Stunden.\nWie lange dauert sie mit 80 km/h?',
                'answer': 3,
                'unit': 'Stunden',
                'tolerance': 0.1,
                'hint': 'Das Produkt Geschwindigkeit × Zeit ist die Strecke (konstant)',
                'solution': 'Lösung:\nStrecke: 60 km/h × 4 h = 240 km\nZeit: 240 km ÷ 80 km/h = 3 Stunden'
            }
        ])

    # Level 4: Gemischte schwierige Aufgaben
    if level >= 4:
        exercises.extend([
            {
                'question': '⚙️ 3 Pumpen füllen einen Pool in 12 Stunden.\nWie lange brauchen 9 Pumpen?',
                'answer': 4,
                'unit': 'Stunden',
                'tolerance': 0.1,
                'hint': 'Mehr Pumpen → weniger Zeit (antiproportional)',
                'solution': 'Lösung:\nProdukt: 3 × 12 = 36\nZeit: 36 ÷ 9 = 4 Stunden'
            },
            {
                'question': '🍰 Ein Rezept für 6 Personen benötigt 450g Zucker.\nWie viel Zucker für 10 Personen?',
                'answer': 750,
                'unit': 'g',
                'tolerance': 5,
                'hint': 'Mehr Personen → mehr Zutaten (proportional)',
                'solution': 'Lösung:\nPro Person: 450g ÷ 6 = 75g\nFür 10 Personen: 75g × 10 = 750g'
            }
        ])

    # Level 5: Sehr schwierige Aufgaben
    if level >= 5:
        exercises.extend([
            {
                'question': '🏭 6 Maschinen produzieren in 8 Stunden 1440 Teile.\nWie viele Teile produzieren 4 Maschinen in 12 Stunden?',
                'answer': 1440,
                'unit': 'Teile',
                'tolerance': 10,
                'hint': 'Rechne erst aus, wie viele Teile 1 Maschine in 1 Stunde macht',
                'solution': 'Lösung:\n1 Maschine in 1 Stunde: 1440 ÷ 6 ÷ 8 = 30 Teile/h\n4 Maschinen in 12 Stunden: 30 × 4 × 12 = 1440 Teile'
            },
            {
                'question': '📏 Eine Karte hat den Maßstab 1:50000.\nWie lang ist eine Strecke in Wirklichkeit, die auf der Karte 7,5 cm misst?',
                'answer': 3.75,
                'unit': 'km',
                'tolerance': 0.1,
                'hint': '1 cm auf der Karte = 50000 cm in Wirklichkeit',
                'solution': 'Lösung:\n7,5 cm × 50000 = 375000 cm = 3750 m = 3,75 km'
            }
        ])

    return jsonify(random.choice(exercises))


@app.route('/api/check_exercise', methods=['POST'])
def check_exercise():
    """Prüfe Übungsantwort"""
    data = request.json
    user_answer = float(data.get('user_answer', 0))
    correct_answer = float(data.get('correct_answer', 0))
    tolerance = float(data.get('tolerance', 0.01))

    progress = get_progress()
    progress['total_attempts'] += 1

    is_correct = abs(user_answer - correct_answer) <= tolerance

    if is_correct:
        progress['correct_answers'] += 1
        progress['exercises_completed'] += 1

        # Level erhöhen bei Erfolg
        if progress['total_attempts'] > 0:
            success_rate = progress['correct_answers'] / progress['total_attempts']
            if success_rate > 0.7 and progress['exercises_completed'] % 3 == 0:
                if progress['level'] < 5:
                    old_level = progress['level']
                    progress['level'] += 1
                    save_progress(progress)
                    return jsonify({
                        'correct': True,
                        'level_up': True,
                        'new_level': progress['level'],
                        'message': f'Level Up! Du bist jetzt Level {progress["level"]}! 🎉'
                    })
    else:
        # Level senken bei zu vielen Fehlern
        if progress['total_attempts'] > 5:
            success_rate = progress['correct_answers'] / progress['total_attempts']
            if success_rate < 0.4 and progress['level'] > 1:
                old_level = progress['level']
                progress['level'] -= 1
                save_progress(progress)
                return jsonify({
                    'correct': False,
                    'level_down': True,
                    'new_level': progress['level'],
                    'message': f'Kein Problem! Wir üben mit einfacheren Aufgaben. Level {progress["level"]}'
                })

    save_progress(progress)
    return jsonify({'correct': is_correct, 'level_up': False, 'level_down': False})


@app.route('/api/progress', methods=['GET'])
def get_progress_api():
    """Hole aktuellen Fortschritt"""
    progress = get_progress()
    if progress['total_attempts'] > 0:
        progress['success_rate'] = round((progress['correct_answers'] / progress['total_attempts']) * 100, 1)
    else:
        progress['success_rate'] = 0
    return jsonify(progress)


@app.route('/api/reset_progress', methods=['POST'])
def reset_progress():
    """Setze Fortschritt zurück"""
    session.clear()
    return jsonify({'success': True})


if __name__ == '__main__':
    import webbrowser
    from threading import Timer

    def open_browser():
        webbrowser.open('http://127.0.0.1:5000')

    # Öffne Browser nach 1 Sekunde
    Timer(1, open_browser).start()

    print("=" * 60)
    print("🎓 ZUORDNUNGEN LERN-APP")
    print("=" * 60)
    print()
    print("✓ Server startet...")
    print("✓ Browser öffnet sich automatisch...")
    print()
    print("Falls der Browser sich nicht öffnet, gehe zu:")
    print("👉 http://127.0.0.1:5000")
    print()
    print("Zum Beenden: Strg+C drücken")
    print("=" * 60)
    print()

    app.run(debug=True, use_reloader=False)
