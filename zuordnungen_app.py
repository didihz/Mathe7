"""
Zuordnungen Lern-App
Eine interaktive Anwendung zum Lernen von proportionalen und antiproportionalen Zuordnungen
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
from typing import Tuple, List, Dict
import json
from datetime import datetime


class ZuordnungenApp:
    """Hauptanwendung für das Lernen von Zuordnungen"""

    def __init__(self, root):
        self.root = root
        self.root.title("Zuordnungen Lern-App 📚")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")

        # Fortschrittsverfolgung
        self.progress = {
            "level": 1,
            "correct_answers": 0,
            "total_attempts": 0,
            "quiz_score": 0,
            "exercises_completed": 0
        }

        # Style konfigurieren
        self.setup_styles()

        # Hauptcontainer
        self.main_container = ttk.Frame(root, padding="10")
        self.main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Konfiguriere Grid
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Zeige Hauptmenü
        self.show_main_menu()

    def setup_styles(self):
        """Konfiguriere Styles für die GUI"""
        style = ttk.Style()
        style.theme_use('clam')

        # Button Styles
        style.configure('Menu.TButton',
                       font=('Arial', 14, 'bold'),
                       padding=15,
                       background='#4CAF50',
                       foreground='white')

        style.configure('Action.TButton',
                       font=('Arial', 12),
                       padding=10,
                       background='#2196F3')

        style.configure('Title.TLabel',
                       font=('Arial', 24, 'bold'),
                       background='#f0f0f0',
                       foreground='#333')

        style.configure('Subtitle.TLabel',
                       font=('Arial', 16),
                       background='#f0f0f0',
                       foreground='#666')

    def clear_frame(self):
        """Lösche alle Widgets im Hauptcontainer"""
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        """Zeige das Hauptmenü"""
        self.clear_frame()

        # Titel
        title = ttk.Label(self.main_container,
                         text="📐 Zuordnungen Lern-App 📐",
                         style='Title.TLabel')
        title.grid(row=0, column=0, pady=30, columnspan=2)

        # Fortschrittsanzeige
        progress_text = f"Level: {self.progress['level']} | Richtig: {self.progress['correct_answers']} | Übungen: {self.progress['exercises_completed']}"
        progress_label = ttk.Label(self.main_container,
                                   text=progress_text,
                                   style='Subtitle.TLabel')
        progress_label.grid(row=1, column=0, pady=10, columnspan=2)

        # Menü-Buttons
        buttons_frame = ttk.Frame(self.main_container)
        buttons_frame.grid(row=2, column=0, pady=20, columnspan=2)

        ttk.Button(buttons_frame,
                  text="📖 Theorie lernen",
                  style='Menu.TButton',
                  command=self.show_theory,
                  width=25).pack(pady=10)

        ttk.Button(buttons_frame,
                  text="🎯 Quiz: Zuordnungen erkennen",
                  style='Menu.TButton',
                  command=self.show_quiz,
                  width=25).pack(pady=10)

        ttk.Button(buttons_frame,
                  text="✏️ Übungen rechnen",
                  style='Menu.TButton',
                  command=self.show_exercises,
                  width=25).pack(pady=10)

        ttk.Button(buttons_frame,
                  text="📊 Fortschritt anzeigen",
                  style='Menu.TButton',
                  command=self.show_progress,
                  width=25).pack(pady=10)

    def show_theory(self):
        """Zeige Theorie-Sektion"""
        self.clear_frame()

        # Titel
        ttk.Label(self.main_container,
                 text="📖 Theorie: Zuordnungen",
                 style='Title.TLabel').grid(row=0, column=0, pady=20)

        # Notebook für verschiedene Theorie-Abschnitte
        notebook = ttk.Notebook(self.main_container)
        notebook.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)

        # Tab 1: Grundlagen
        tab1 = self.create_theory_grundlagen()
        notebook.add(tab1, text="1. Was ist eine Zuordnung?")

        # Tab 2: Proportionale Zuordnungen
        tab2 = self.create_theory_proportional()
        notebook.add(tab2, text="2. Proportionale Zuordnungen")

        # Tab 3: Antiproportionale Zuordnungen
        tab3 = self.create_theory_antiproportional()
        notebook.add(tab3, text="3. Antiproportionale Zuordnungen")

        # Tab 4: Erkennungsmerkmale
        tab4 = self.create_theory_erkennung()
        notebook.add(tab4, text="4. Wie erkenne ich den Typ?")

        # Zurück-Button
        ttk.Button(self.main_container,
                  text="↩️ Zurück zum Menü",
                  command=self.show_main_menu).grid(row=2, column=0, pady=20)

    def create_theory_grundlagen(self):
        """Erstelle Tab für Grundlagen"""
        frame = ttk.Frame()

        text = scrolledtext.ScrolledText(frame, wrap=tk.WORD,
                                         font=('Arial', 12),
                                         width=80, height=30)
        text.pack(padx=10, pady=10)

        content = """
📌 WAS IST EINE ZUORDNUNG?

Eine Zuordnung beschreibt einen Zusammenhang zwischen zwei Größen.
Einer Ausgangsgröße wird eine Zielgröße zugeordnet.

Beispiele aus dem Alltag:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Anzahl Eier → Preis
  5 Eier kosten 2,50 €

• Arbeitszeit → Lohn
  2 Stunden Arbeit → 24 € Lohn

• Geschwindigkeit → Fahrzeit
  Mit 60 km/h braucht man 2 Stunden

• Anzahl Arbeiter → Zeit für eine Aufgabe
  2 Arbeiter brauchen 6 Stunden


📊 DARSTELLUNG VON ZUORDNUNGEN:

1. Als Tabelle:
   ┌─────────┬───────┐
   │ Anzahl  │  Preis │
   ├─────────┼───────┤
   │    1    │ 0,50€ │
   │    2    │ 1,00€ │
   │    3    │ 1,50€ │
   └─────────┴───────┘

2. Als Pfeildiagramm:
   1 → 0,50€
   2 → 1,00€
   3 → 1,50€

3. Als Graph:
   Eine Linie im Koordinatensystem


💡 WICHTIG:

Es gibt zwei Haupttypen von Zuordnungen:

1. PROPORTIONALE Zuordnungen
   → Je mehr, desto mehr!
   → Beide Größen ändern sich in die gleiche Richtung

2. ANTIPROPORTIONALE Zuordnungen
   → Je mehr, desto weniger!
   → Die Größen ändern sich in entgegengesetzte Richtungen
"""

        text.insert('1.0', content)
        text.config(state='disabled')

        return frame

    def create_theory_proportional(self):
        """Erstelle Tab für proportionale Zuordnungen"""
        frame = ttk.Frame()

        text = scrolledtext.ScrolledText(frame, wrap=tk.WORD,
                                         font=('Arial', 12),
                                         width=80, height=30)
        text.pack(padx=10, pady=10)

        content = """
📈 PROPORTIONALE ZUORDNUNGEN

Definition:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bei einer proportionalen Zuordnung gilt:
→ Verdoppelt sich die eine Größe, verdoppelt sich auch die andere
→ Verdreifacht sich die eine Größe, verdreifacht sich auch die andere
→ usw.


🎯 ERKENNUNGSMERKMALE:

✓ JE MEHR, DESTO MEHR!
✓ Beide Größen ändern sich in die GLEICHE Richtung
✓ Der Quotient (Verhältnis) bleibt KONSTANT
✓ Der Graph ist eine GERADE durch den Ursprung (0,0)


📝 BEISPIEL 1: EIER KAUFEN

┌─────────┬────────┬─────────────┐
│ Anzahl  │  Preis │ Preis/Stück │
├─────────┼────────┼─────────────┤
│    2    │ 1,00€  │   0,50€     │
│    4    │ 2,00€  │   0,50€     │
│    6    │ 3,00€  │   0,50€     │
│   10    │ 5,00€  │   0,50€     │
└─────────┴────────┴─────────────┘

→ Doppelte Anzahl = doppelter Preis
→ Der Preis pro Stück bleibt gleich (0,50€)


📝 BEISPIEL 2: ARBEITSLOHN

┌──────────┬──────────┐
│ Stunden  │   Lohn   │
├──────────┼──────────┤
│    1     │   12 €   │
│    2     │   24 €   │
│    3     │   36 €   │
│    5     │   60 €   │
└──────────┴──────────┘

→ Doppelte Zeit = doppelter Lohn
→ Der Stundenlohn bleibt konstant (12€/h)


🧮 RECHENWEG: Der Dreisatz

Aufgabe: 5 Eier kosten 2,50€. Was kosten 7 Eier?

Schritt 1: Berechne den Wert für 1 (Einheit)
   5 Eier → 2,50€
   1 Ei   → 2,50€ ÷ 5 = 0,50€

Schritt 2: Multipliziere mit der gesuchten Anzahl
   1 Ei  → 0,50€
   7 Eier → 0,50€ × 7 = 3,50€

Antwort: 7 Eier kosten 3,50€


📐 FORMEL:

y = k · x

wobei:
  y = Zielgröße
  x = Ausgangsgröße
  k = Proportionalitätsfaktor (konstant!)

Beispiel: Preis = 0,50€ · Anzahl


🎓 WEITERE BEISPIELE:

• Fahrstrecke und Benzinverbrauch
  mehr Kilometer → mehr Benzin

• Gewicht und Preis (z.B. Obst)
  mehr Kilogramm → höherer Preis

• Rezept verdoppeln
  doppelte Menge → doppelte Zutaten
"""

        text.insert('1.0', content)
        text.config(state='disabled')

        return frame

    def create_theory_antiproportional(self):
        """Erstelle Tab für antiproportionale Zuordnungen"""
        frame = ttk.Frame()

        text = scrolledtext.ScrolledText(frame, wrap=tk.WORD,
                                         font=('Arial', 12),
                                         width=80, height=30)
        text.pack(padx=10, pady=10)

        content = """
📉 ANTIPROPORTIONALE ZUORDNUNGEN

Definition:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bei einer antiproportionalen Zuordnung gilt:
→ Verdoppelt sich die eine Größe, halbiert sich die andere
→ Verdreifacht sich die eine Größe, drittelt sich die andere
→ usw.


🎯 ERKENNUNGSMERKMALE:

✓ JE MEHR, DESTO WENIGER!
✓ Die Größen ändern sich in ENTGEGENGESETZTE Richtungen
✓ Das Produkt bleibt KONSTANT
✓ Der Graph ist eine HYPERBEL (gebogene Kurve)


📝 BEISPIEL 1: ARBEITER UND BAUZEIT

┌──────────┬──────────┬─────────────────┐
│ Arbeiter │   Zeit   │ Arbeiter × Zeit │
├──────────┼──────────┼─────────────────┤
│    1     │ 12 Tage  │       12        │
│    2     │  6 Tage  │       12        │
│    3     │  4 Tage  │       12        │
│    4     │  3 Tage  │       12        │
│    6     │  2 Tage  │       12        │
└──────────┴──────────┴─────────────────┘

→ Doppelte Arbeiter = halbe Zeit
→ Das Produkt (Arbeiter × Zeit) bleibt konstant!


📝 BEISPIEL 2: GESCHWINDIGKEIT UND FAHRZEIT

Strecke: 120 km

┌──────────────┬──────────┬─────────────────┐
│ Geschwindig. │   Zeit   │  Geschw. × Zeit │
├──────────────┼──────────┼─────────────────┤
│   30 km/h    │  4 h     │      120        │
│   40 km/h    │  3 h     │      120        │
│   60 km/h    │  2 h     │      120        │
│   80 km/h    │ 1,5 h    │      120        │
└──────────────┴──────────┴─────────────────┘

→ Doppelte Geschwindigkeit = halbe Zeit
→ Das Produkt bleibt konstant (= Strecke)


🧮 RECHENWEG: Der antiproportionale Dreisatz

Aufgabe: 3 Arbeiter brauchen 8 Tage.
         Wie lange brauchen 4 Arbeiter?

Schritt 1: Berechne das konstante Produkt
   3 Arbeiter × 8 Tage = 24

Schritt 2: Teile durch die neue Anzahl
   24 ÷ 4 Arbeiter = 6 Tage

Antwort: 4 Arbeiter brauchen 6 Tage


📐 FORMEL:

x · y = k (konstant)

oder umgeformt:

y = k ÷ x

wobei:
  y = Zielgröße
  x = Ausgangsgröße
  k = Konstantes Produkt

Beispiel: Zeit = 24 ÷ Anzahl Arbeiter


⚠️ WICHTIGER UNTERSCHIED:

PROPORTIONAL:
→ Mehr → Mehr (gleiche Richtung)
→ Quotient konstant: y/x = k
→ Rechnung: durch x teilen, dann mal neue Anzahl

ANTIPROPORTIONAL:
→ Mehr → Weniger (entgegengesetzte Richtung)
→ Produkt konstant: x · y = k
→ Rechnung: Produkt bilden, dann durch neue Anzahl teilen


🎓 WEITERE BEISPIELE:

• Schriftgröße und Zeilen auf einer Seite
  größere Schrift → weniger Zeilen

• Anzahl Pumpen und Zeit zum Befüllen
  mehr Pumpen → weniger Zeit

• Zahnradübersetzung
  mehr Zähne → langsamere Drehung
"""

        text.insert('1.0', content)
        text.config(state='disabled')

        return frame

    def create_theory_erkennung(self):
        """Erstelle Tab für Erkennungsmerkmale"""
        frame = ttk.Frame()

        text = scrolledtext.ScrolledText(frame, wrap=tk.WORD,
                                         font=('Arial', 12),
                                         width=80, height=30)
        text.pack(padx=10, pady=10)

        content = """
🔍 WIE ERKENNE ICH DEN TYP DER ZUORDNUNG?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 METHODE 1: Die Frage "Je mehr, desto...?"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Stelle dir die Frage:
"Wenn die erste Größe größer wird, wird dann auch die zweite größer?"

✓ JA, beide werden größer
  → PROPORTIONAL

✓ NEIN, die zweite wird kleiner
  → ANTIPROPORTIONAL


Beispiele:
───────────

Mehr Eier kaufen → höherer Preis
→ Beide größer → PROPORTIONAL ✓

Mehr Arbeiter → weniger Zeit
→ Eine größer, andere kleiner → ANTIPROPORTIONAL ✓


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 METHODE 2: Tabelle prüfen
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Prüfe in der Tabelle:

PROPORTIONAL:
→ Quotient bilden: Zweiter Wert ÷ Erster Wert
→ Ist der Quotient immer gleich? → PROPORTIONAL

ANTIPROPORTIONAL:
→ Produkt bilden: Erster Wert × Zweiter Wert
→ Ist das Produkt immer gleich? → ANTIPROPORTIONAL


Beispiel 1:
┌─────────┬────────┐
│ Anzahl  │  Preis │
├─────────┼────────┤
│    2    │ 1,00€  │
│    4    │ 2,00€  │
│    8    │ 4,00€  │
└─────────┴────────┘

Quotient prüfen:
  1,00 ÷ 2 = 0,50
  2,00 ÷ 4 = 0,50
  4,00 ÷ 8 = 0,50

→ Quotient konstant → PROPORTIONAL ✓


Beispiel 2:
┌──────────┬────────┐
│ Arbeiter │  Zeit  │
├──────────┼────────┤
│    2     │ 12 Tg. │
│    3     │  8 Tg. │
│    4     │  6 Tg. │
└──────────┴────────┘

Produkt prüfen:
  2 × 12 = 24
  3 × 8  = 24
  4 × 6  = 24

→ Produkt konstant → ANTIPROPORTIONAL ✓


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 METHODE 3: Verdoppelungstest
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Verdopple die erste Größe und schau, was passiert:

✓ Zweite Größe verdoppelt sich auch
  → PROPORTIONAL

✓ Zweite Größe halbiert sich
  → ANTIPROPORTIONAL


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 METHODE 4: Graph ansehen
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROPORTIONAL:
→ Gerade Linie durch den Ursprung (0,0)
→ Gleichmäßiger Anstieg

ANTIPROPORTIONAL:
→ Gebogene Kurve (Hyperbel)
→ Kommt nie auf die Achsen


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚨 HÄUFIGE FEHLER vermeiden!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ FEHLER 1: Nur auf Zahlen schauen
   Achte auf die BEDEUTUNG der Größen!

❌ FEHLER 2: "Beide werden größer" mit Addieren verwechseln
   Bei proportional: 2× die Menge → 2× der Preis
   NICHT: 2 mehr → 2€ mehr!

❌ FEHLER 3: Denken, dass immer eine Zuordnung vorliegt
   Manchmal gibt es gar keine proportionale/antiproportionale Zuordnung!


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ CHECKLISTE ZUM ERKENNEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Stelle folgende Fragen:

1️⃣ Werden beide Größen größer?
   → JA: wahrscheinlich PROPORTIONAL
   → NEIN: weiter prüfen

2️⃣ Wird eine größer, die andere kleiner?
   → JA: wahrscheinlich ANTIPROPORTIONAL
   → NEIN: keine dieser Zuordnungen

3️⃣ Teste mit Zahlen:
   → Quotient konstant? → PROPORTIONAL
   → Produkt konstant? → ANTIPROPORTIONAL

4️⃣ Verdoppelungstest durchführen

5️⃣ Bei Unsicherheit: Tabelle erstellen und prüfen!


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎓 ÜBUNGSTIPP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Überlege bei Alltagssituationen:
"Ist das proportional oder antiproportional?"

Das hilft dir, ein Gefühl für Zuordnungen zu entwickeln!
"""

        text.insert('1.0', content)
        text.config(state='disabled')

        return frame

    def show_quiz(self):
        """Zeige Quiz-Sektion"""
        self.clear_frame()
        self.quiz_score = 0
        self.quiz_question_number = 0
        self.total_quiz_questions = 10

        self.next_quiz_question()

    def next_quiz_question(self):
        """Zeige nächste Quiz-Frage"""
        if self.quiz_question_number >= self.total_quiz_questions:
            self.show_quiz_results()
            return

        self.clear_frame()
        self.quiz_question_number += 1

        # Titel
        title_text = f"🎯 Quiz: Frage {self.quiz_question_number}/{self.total_quiz_questions}"
        ttk.Label(self.main_container,
                 text=title_text,
                 style='Title.TLabel').grid(row=0, column=0, pady=20, columnspan=2)

        # Score
        score_text = f"Punktzahl: {self.quiz_score}/{self.quiz_question_number-1}"
        ttk.Label(self.main_container,
                 text=score_text,
                 style='Subtitle.TLabel').grid(row=1, column=0, pady=10, columnspan=2)

        # Generiere Frage
        question, correct_answer, explanation = self.generate_quiz_question()

        # Speichere richtige Antwort
        self.current_quiz_answer = correct_answer
        self.current_quiz_explanation = explanation

        # Frage anzeigen
        question_frame = ttk.LabelFrame(self.main_container, text="Aufgabe", padding=20)
        question_frame.grid(row=2, column=0, pady=20, padx=20, columnspan=2, sticky=(tk.W, tk.E))

        question_label = tk.Label(question_frame,
                                 text=question,
                                 font=('Arial', 13),
                                 wraplength=700,
                                 justify=tk.LEFT,
                                 bg='white',
                                 padx=20,
                                 pady=20)
        question_label.pack(fill=tk.BOTH, expand=True)

        # Antwort-Buttons
        answer_frame = ttk.Frame(self.main_container)
        answer_frame.grid(row=3, column=0, pady=20, columnspan=2)

        ttk.Button(answer_frame,
                  text="📈 Proportional",
                  command=lambda: self.check_quiz_answer("proportional"),
                  width=25).pack(side=tk.LEFT, padx=10)

        ttk.Button(answer_frame,
                  text="📉 Antiproportional",
                  command=lambda: self.check_quiz_answer("antiproportional"),
                  width=25).pack(side=tk.LEFT, padx=10)

        ttk.Button(answer_frame,
                  text="❌ Weder noch",
                  command=lambda: self.check_quiz_answer("keine"),
                  width=25).pack(side=tk.LEFT, padx=10)

    def generate_quiz_question(self) -> Tuple[str, str, str]:
        """Generiere eine Quiz-Frage"""
        questions = [
            # Proportionale Fragen
            (
                "🛒 Je mehr Äpfel ich kaufe, desto mehr Geld muss ich bezahlen.\n"
                "2 kg kosten 4€, 4 kg kosten 8€.\n\n"
                "Welche Art von Zuordnung liegt vor?",
                "proportional",
                "✓ Richtig! Je mehr Kilogramm, desto höher der Preis.\n"
                "Das Doppelte an Äpfeln kostet das Doppelte.\n"
                "Der Quotient (Preis ÷ kg) bleibt konstant: 4€÷2kg = 2€/kg"
            ),
            (
                "⏱️ Ein Auto fährt mit konstanter Geschwindigkeit.\n"
                "In 2 Stunden legt es 120 km zurück, in 4 Stunden 240 km.\n\n"
                "Welche Zuordnung beschreibt Zeit → Strecke?",
                "proportional",
                "✓ Richtig! Bei konstanter Geschwindigkeit gilt:\n"
                "Doppelte Zeit = doppelte Strecke.\n"
                "Der Quotient (Strecke ÷ Zeit) ist konstant: die Geschwindigkeit!"
            ),
            (
                "🍪 Ein Rezept für 4 Personen benötigt 200g Mehl.\n"
                "Für 8 Personen benötigt man 400g Mehl.\n\n"
                "Was für eine Zuordnung ist: Anzahl Personen → Mehlmenge?",
                "proportional",
                "✓ Richtig! Doppelte Personenzahl = doppelte Zutaten.\n"
                "Das ist eine klassische proportionale Zuordnung."
            ),
            # Antiproportionale Fragen
            (
                "👷 3 Arbeiter brauchen 12 Tage für eine Aufgabe.\n"
                "6 Arbeiter brauchen nur 6 Tage.\n\n"
                "Welche Zuordnung: Anzahl Arbeiter → Zeit?",
                "antiproportional",
                "✓ Richtig! Mehr Arbeiter = weniger Zeit.\n"
                "Das Doppelte an Arbeitern = die halbe Zeit.\n"
                "Das Produkt bleibt konstant: 3×12 = 6×6 = 36"
            ),
            (
                "🚗 Eine 180 km lange Strecke wird zurückgelegt.\n"
                "Mit 60 km/h braucht man 3h, mit 90 km/h nur 2h.\n\n"
                "Welche Zuordnung: Geschwindigkeit → Zeit?",
                "antiproportional",
                "✓ Richtig! Höhere Geschwindigkeit = kürzere Zeit.\n"
                "Das Produkt (Geschwindigkeit × Zeit) bleibt konstant: die Strecke!\n"
                "60×3 = 90×2 = 180 km"
            ),
            (
                "⚙️ Ein Zahnrad mit 20 Zähnen dreht sich 12 mal pro Minute.\n"
                "Ein Zahnrad mit 40 Zähnen dreht sich nur 6 mal pro Minute.\n\n"
                "Welche Zuordnung: Anzahl Zähne → Drehzahl?",
                "antiproportional",
                "✓ Richtig! Mehr Zähne = langsamere Drehung.\n"
                "Das Produkt bleibt konstant: 20×12 = 40×6 = 240"
            ),
            # Weder-noch Fragen
            (
                "🌡️ Die Temperatur in Celsius wird in Fahrenheit umgerechnet.\n"
                "0°C = 32°F, 10°C = 50°F, 20°C = 68°F\n\n"
                "Welche Zuordnung liegt vor?",
                "keine",
                "✓ Richtig! Dies ist weder proportional noch antiproportional.\n"
                "Proportional würde bedeuten: 0°C → 0°F (geht durch Ursprung)\n"
                "Die Umrechnung ist linear, aber nicht proportional."
            ),
            (
                "📏 Quadrate mit verschiedenen Seitenlängen:\n"
                "Seite 2cm → Fläche 4cm², Seite 3cm → Fläche 9cm²\n\n"
                "Welche Zuordnung: Seitenlänge → Flächeninhalt?",
                "keine",
                "✓ Richtig! Keine proportionale Zuordnung!\n"
                "Bei proportional würde gelten: doppelte Seite = doppelte Fläche.\n"
                "Aber: doppelte Seite = vierfache Fläche (quadratisch!)"
            ),
            (
                "💰 Eine Firma hat Grundgebühr + Preis pro Stück:\n"
                "1 Stück: 15€ (10€ + 5€), 2 Stück: 20€ (10€ + 2×5€)\n\n"
                "Welche Zuordnung: Anzahl → Preis?",
                "keine",
                "✓ Richtig! Wegen der Grundgebühr ist es nicht proportional.\n"
                "Bei proportional müsste gelten: 0 Stück = 0€.\n"
                "Aber hier: 0 Stück = 10€ (Grundgebühr)"
            ),
            (
                "📊 In einer Tabelle werden Größen zugeordnet:\n"
                "1→3, 2→6, 3→11, 4→18\n\n"
                "Prüfe: Ist der Quotient oder das Produkt konstant?",
                "keine",
                "✓ Richtig! Weder Quotient noch Produkt sind konstant.\n"
                "Quotient: 3/1=3, 6/2=3, 11/3=3.67, 18/4=4.5\n"
                "Produkt: 1×3=3, 2×6=12, 3×11=33, 4×18=72"
            ),
        ]

        return random.choice(questions)

    def check_quiz_answer(self, answer: str):
        """Prüfe Quiz-Antwort"""
        if answer == self.current_quiz_answer:
            self.quiz_score += 1
            result_title = "✅ Richtig!"
            result_color = "green"
        else:
            result_title = "❌ Leider falsch"
            result_color = "red"

        # Zeige Ergebnis-Dialog
        result_window = tk.Toplevel(self.root)
        result_window.title(result_title)
        result_window.geometry("600x400")
        result_window.configure(bg='white')

        # Titel
        title_label = tk.Label(result_window,
                              text=result_title,
                              font=('Arial', 20, 'bold'),
                              fg=result_color,
                              bg='white')
        title_label.pack(pady=20)

        # Erklärung
        explanation_frame = ttk.LabelFrame(result_window, text="Erklärung", padding=20)
        explanation_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        explanation_text = scrolledtext.ScrolledText(explanation_frame,
                                                     wrap=tk.WORD,
                                                     font=('Arial', 11),
                                                     height=10)
        explanation_text.pack(fill=tk.BOTH, expand=True)
        explanation_text.insert('1.0', self.current_quiz_explanation)
        explanation_text.config(state='disabled')

        # Weiter-Button
        ttk.Button(result_window,
                  text="➡️ Nächste Frage",
                  command=lambda: [result_window.destroy(), self.next_quiz_question()]).pack(pady=20)

        # Zentriere Fenster
        result_window.transient(self.root)
        result_window.grab_set()

    def show_quiz_results(self):
        """Zeige Quiz-Endergebnis"""
        self.clear_frame()

        # Update Fortschritt
        self.progress['quiz_score'] = self.quiz_score

        percentage = (self.quiz_score / self.total_quiz_questions) * 100

        # Titel
        ttk.Label(self.main_container,
                 text="🎯 Quiz Ergebnis",
                 style='Title.TLabel').grid(row=0, column=0, pady=20)

        # Ergebnis
        result_frame = ttk.LabelFrame(self.main_container, text="Deine Leistung", padding=30)
        result_frame.grid(row=1, column=0, pady=20, padx=20)

        score_text = f"{self.quiz_score} von {self.total_quiz_questions} richtig"
        ttk.Label(result_frame,
                 text=score_text,
                 font=('Arial', 24, 'bold')).pack(pady=10)

        percentage_text = f"{percentage:.0f}%"
        ttk.Label(result_frame,
                 text=percentage_text,
                 font=('Arial', 20)).pack(pady=10)

        # Bewertung
        if percentage >= 90:
            bewertung = "🌟 Ausgezeichnet! Du bist ein Profi!"
            color = "green"
        elif percentage >= 70:
            bewertung = "👍 Sehr gut! Du hast es verstanden!"
            color = "blue"
        elif percentage >= 50:
            bewertung = "✓ Gut! Übe noch ein bisschen!"
            color = "orange"
        else:
            bewertung = "💪 Nicht aufgeben! Lies nochmal die Theorie!"
            color = "red"

        bewertung_label = tk.Label(result_frame,
                                  text=bewertung,
                                  font=('Arial', 14),
                                  fg=color)
        bewertung_label.pack(pady=20)

        # Buttons
        button_frame = ttk.Frame(self.main_container)
        button_frame.grid(row=2, column=0, pady=30)

        ttk.Button(button_frame,
                  text="🔄 Quiz wiederholen",
                  command=self.show_quiz).pack(side=tk.LEFT, padx=10)

        ttk.Button(button_frame,
                  text="↩️ Zurück zum Menü",
                  command=self.show_main_menu).pack(side=tk.LEFT, padx=10)

    def show_exercises(self):
        """Zeige Übungssektion"""
        self.clear_frame()

        # Titel
        ttk.Label(self.main_container,
                 text="✏️ Rechenübungen",
                 style='Title.TLabel').grid(row=0, column=0, pady=20, columnspan=2)

        # Level-Info
        level_text = f"Aktuelles Level: {self.progress['level']}"
        ttk.Label(self.main_container,
                 text=level_text,
                 style='Subtitle.TLabel').grid(row=1, column=0, pady=10, columnspan=2)

        # Generiere Aufgabe basierend auf Level
        self.current_exercise = self.generate_exercise(self.progress['level'])

        # Aufgabe anzeigen
        exercise_frame = ttk.LabelFrame(self.main_container, text="Aufgabe", padding=20)
        exercise_frame.grid(row=2, column=0, pady=20, padx=20, columnspan=2, sticky=(tk.W, tk.E))

        exercise_label = tk.Label(exercise_frame,
                                 text=self.current_exercise['question'],
                                 font=('Arial', 13),
                                 wraplength=700,
                                 justify=tk.LEFT,
                                 bg='white',
                                 padx=20,
                                 pady=20)
        exercise_label.pack(fill=tk.BOTH, expand=True)

        # Eingabefeld
        input_frame = ttk.Frame(self.main_container)
        input_frame.grid(row=3, column=0, pady=20, columnspan=2)

        ttk.Label(input_frame,
                 text="Deine Antwort:",
                 font=('Arial', 12)).pack(side=tk.LEFT, padx=10)

        self.exercise_entry = ttk.Entry(input_frame, font=('Arial', 14), width=20)
        self.exercise_entry.pack(side=tk.LEFT, padx=10)
        self.exercise_entry.focus()

        # Einheit anzeigen
        if 'unit' in self.current_exercise:
            ttk.Label(input_frame,
                     text=self.current_exercise['unit'],
                     font=('Arial', 12)).pack(side=tk.LEFT, padx=5)

        # Enter-Taste binden
        self.exercise_entry.bind('<Return>', lambda e: self.check_exercise())

        # Buttons
        button_frame = ttk.Frame(self.main_container)
        button_frame.grid(row=4, column=0, pady=20, columnspan=2)

        ttk.Button(button_frame,
                  text="✓ Prüfen",
                  command=self.check_exercise).pack(side=tk.LEFT, padx=10)

        ttk.Button(button_frame,
                  text="💡 Tipp anzeigen",
                  command=self.show_hint).pack(side=tk.LEFT, padx=10)

        ttk.Button(button_frame,
                  text="⏭️ Überspringen",
                  command=self.show_exercises).pack(side=tk.LEFT, padx=10)

        ttk.Button(button_frame,
                  text="↩️ Zurück",
                  command=self.show_main_menu).pack(side=tk.LEFT, padx=10)

    def generate_exercise(self, level: int) -> Dict:
        """Generiere Übungsaufgabe basierend auf Level"""
        exercises = []

        # Level 1: Einfache proportionale Aufgaben (ganzzahlig)
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

        # Level 3: Antiproportionale Aufgaben (einfach)
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

        return random.choice(exercises)

    def check_exercise(self):
        """Prüfe die Übungsantwort"""
        try:
            user_answer = float(self.exercise_entry.get().replace(',', '.'))
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gib eine Zahl ein!")
            return

        correct_answer = self.current_exercise['answer']
        tolerance = self.current_exercise.get('tolerance', 0.01)

        self.progress['total_attempts'] += 1

        if abs(user_answer - correct_answer) <= tolerance:
            # Richtig!
            self.progress['correct_answers'] += 1
            self.progress['exercises_completed'] += 1

            # Level erhöhen bei Erfolg
            success_rate = self.progress['correct_answers'] / self.progress['total_attempts']
            if success_rate > 0.7 and self.progress['exercises_completed'] % 3 == 0:
                if self.progress['level'] < 5:
                    self.progress['level'] += 1
                    messagebox.showinfo("Level Up! 🎉",
                                      f"Glückwunsch! Du bist jetzt Level {self.progress['level']}!\n"
                                      f"Die Aufgaben werden etwas schwieriger.")

            result_window = tk.Toplevel(self.root)
            result_window.title("Richtig!")
            result_window.geometry("500x300")

            tk.Label(result_window,
                    text="✅ Richtig!",
                    font=('Arial', 24, 'bold'),
                    fg='green').pack(pady=20)

            solution_text = scrolledtext.ScrolledText(result_window,
                                                     wrap=tk.WORD,
                                                     font=('Arial', 11),
                                                     height=8,
                                                     width=50)
            solution_text.pack(pady=10, padx=20)
            solution_text.insert('1.0', self.current_exercise['solution'])
            solution_text.config(state='disabled')

            ttk.Button(result_window,
                      text="➡️ Nächste Aufgabe",
                      command=lambda: [result_window.destroy(), self.show_exercises()]).pack(pady=20)

            result_window.transient(self.root)
            result_window.grab_set()
        else:
            # Falsch
            # Level senken bei zu vielen Fehlern
            success_rate = self.progress['correct_answers'] / self.progress['total_attempts']
            if success_rate < 0.4 and self.progress['total_attempts'] > 5:
                if self.progress['level'] > 1:
                    self.progress['level'] -= 1
                    messagebox.showinfo("Level angepasst",
                                      f"Kein Problem! Wir üben erst mal mit etwas einfacheren Aufgaben.\n"
                                      f"Neues Level: {self.progress['level']}")

            result_window = tk.Toplevel(self.root)
            result_window.title("Nicht ganz richtig")
            result_window.geometry("500x350")

            tk.Label(result_window,
                    text="❌ Leider nicht richtig",
                    font=('Arial', 20, 'bold'),
                    fg='red').pack(pady=20)

            tk.Label(result_window,
                    text=f"Deine Antwort: {user_answer}\nRichtige Antwort: {correct_answer}",
                    font=('Arial', 12)).pack(pady=10)

            solution_text = scrolledtext.ScrolledText(result_window,
                                                     wrap=tk.WORD,
                                                     font=('Arial', 11),
                                                     height=8,
                                                     width=50)
            solution_text.pack(pady=10, padx=20)
            solution_text.insert('1.0', self.current_exercise['solution'])
            solution_text.config(state='disabled')

            button_frame = ttk.Frame(result_window)
            button_frame.pack(pady=20)

            ttk.Button(button_frame,
                      text="🔄 Nochmal versuchen",
                      command=lambda: [result_window.destroy()]).pack(side=tk.LEFT, padx=5)

            ttk.Button(button_frame,
                      text="➡️ Nächste Aufgabe",
                      command=lambda: [result_window.destroy(), self.show_exercises()]).pack(side=tk.LEFT, padx=5)

            result_window.transient(self.root)
            result_window.grab_set()

    def show_hint(self):
        """Zeige Hinweis zur aktuellen Aufgabe"""
        messagebox.showinfo("💡 Tipp", self.current_exercise['hint'])

    def show_progress(self):
        """Zeige Fortschrittsübersicht"""
        self.clear_frame()

        ttk.Label(self.main_container,
                 text="📊 Dein Fortschritt",
                 style='Title.TLabel').grid(row=0, column=0, pady=20, columnspan=2)

        # Fortschritts-Frame
        progress_frame = ttk.LabelFrame(self.main_container, text="Statistiken", padding=30)
        progress_frame.grid(row=1, column=0, pady=20, padx=40, columnspan=2)

        stats = [
            ("🎯 Aktuelles Level:", f"{self.progress['level']}/5"),
            ("✅ Richtige Antworten:", str(self.progress['correct_answers'])),
            ("📝 Gesamte Versuche:", str(self.progress['total_attempts'])),
            ("📋 Abgeschlossene Übungen:", str(self.progress['exercises_completed'])),
            ("🎯 Quiz Punktzahl:", f"{self.progress['quiz_score']}/10"),
        ]

        if self.progress['total_attempts'] > 0:
            success_rate = (self.progress['correct_answers'] / self.progress['total_attempts']) * 100
            stats.append(("📈 Erfolgsquote:", f"{success_rate:.1f}%"))

        for i, (label, value) in enumerate(stats):
            ttk.Label(progress_frame,
                     text=label,
                     font=('Arial', 14, 'bold')).grid(row=i, column=0, sticky=tk.W, pady=10, padx=10)
            ttk.Label(progress_frame,
                     text=value,
                     font=('Arial', 14)).grid(row=i, column=1, sticky=tk.W, pady=10, padx=20)

        # Motivationstext
        if self.progress['level'] == 5 and self.progress['exercises_completed'] > 10:
            motivation = "🌟 Fantastisch! Du bist ein Zuordnungs-Experte!"
        elif self.progress['level'] >= 3:
            motivation = "👍 Super! Du machst große Fortschritte!"
        elif self.progress['exercises_completed'] > 5:
            motivation = "✨ Weiter so! Übung macht den Meister!"
        else:
            motivation = "💪 Gut gestartet! Bleib dran!"

        ttk.Label(self.main_container,
                 text=motivation,
                 font=('Arial', 16),
                 foreground='blue').grid(row=2, column=0, pady=30, columnspan=2)

        # Zurück-Button
        ttk.Button(self.main_container,
                  text="↩️ Zurück zum Menü",
                  command=self.show_main_menu).grid(row=3, column=0, pady=20, columnspan=2)


def main():
    """Hauptfunktion zum Starten der App"""
    root = tk.Tk()
    app = ZuordnungenApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
