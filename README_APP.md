# 📐 Zuordnungen Lern-App

Eine interaktive Desktop-Anwendung zum Lernen und Üben von **proportionalen** und **antiproportionalen Zuordnungen** für Schüler der Klasse 6-7.

## 🌟 Features

### 📖 Theorie lernen
- **Was ist eine Zuordnung?** - Grundlagen mit Alltagsbeispielen
- **Proportionale Zuordnungen** - Ausführliche Erklärung mit Beispielen
- **Antiproportionale Zuordnungen** - Verständliche Darstellung
- **Erkennungsmerkmale** - 4 Methoden zum Erkennen des Zuordnungstyps
- Übersichtliche Darstellung mit Tabs

### 🎯 Quiz: Zuordnungen erkennen
- 10 interaktive Fragen
- Unterscheide zwischen proportional, antiproportional und "weder noch"
- Sofortige Rückmeldung mit ausführlicher Erklärung
- Punktzahl-Tracking
- Bewertung der Leistung

### ✏️ Rechenübungen
- **Adaptives Levelsystem** (Level 1-5)
- Aufgaben von einfach bis schwer
- Klassischer Dreisatz-Ansatz
- Beispiele wie im Bild: "5 Eier kosten 2,60€, wie viel kosten 7 Eier?"
- **Intelligente Schwierigkeitsanpassung:**
  - Bei guter Leistung (>70% richtig) → Level steigt
  - Bei Schwierigkeiten (<40% richtig) → Level sinkt
  - Perfekt für schwächere Schüler, die langsam Fortschritte machen!

### 📊 Fortschrittsverfolgung
- Aktuelles Level
- Anzahl richtiger Antworten
- Erfolgsquote
- Abgeschlossene Übungen
- Motivierende Rückmeldungen

## 🚀 Installation und Start

### Voraussetzungen
- Python 3.6 oder höher
- tkinter (normalerweise in Python enthalten)

### Installation prüfen
```bash
python3 --version
```

Falls tkinter nicht installiert ist:
- **Ubuntu/Debian:** `sudo apt-get install python3-tk`
- **Fedora:** `sudo dnf install python3-tkinter`
- **macOS:** tkinter ist standardmäßig enthalten
- **Windows:** tkinter ist standardmäßig enthalten

### App starten
```bash
python3 zuordnungen_app.py
```

Oder mit Doppelklick auf die Datei (bei entsprechender System-Konfiguration).

## 📚 Verwendung

### 1. Theorie lernen
Beginne mit der Theorie, um die Grundlagen zu verstehen:
- Was sind Zuordnungen?
- Wie funktionieren proportionale Zuordnungen?
- Wie funktionieren antiproportionale Zuordnungen?
- Wie erkenne ich den Typ?

### 2. Quiz machen
Teste dein Wissen mit 10 Fragen:
- Erkenne, ob eine Zuordnung proportional, antiproportional oder keines von beiden ist
- Erhalte sofort Feedback mit Erklärungen
- Verbessere dein Verständnis

### 3. Übungen rechnen
Übe das Rechnen mit dem Dreisatz:

**Level 1 (Einfach):**
- Einfache proportionale Aufgaben
- Ganzzahlige Ergebnisse
- Beispiel: "5 Eier kosten 2,50€. Was kosten 7 Eier?"

**Level 2 (Mittel):**
- Schwierigere proportionale Aufgaben
- Dezimalzahlen

**Level 3 (Fortgeschritten):**
- Antiproportionale Aufgaben
- Beispiel: "4 Arbeiter brauchen 6 Tage. Wie lange brauchen 8 Arbeiter?"

**Level 4 (Schwer):**
- Gemischte Aufgaben
- Erkennen des Zuordnungstyps notwendig

**Level 5 (Experte):**
- Komplexe Aufgaben mit mehreren Schritten
- Maßstäbe und kombinierte Zuordnungen

### 4. Fortschritt verfolgen
Sieh dir deine Statistiken an:
- Wie viele Aufgaben hast du gelöst?
- Wie hoch ist deine Erfolgsquote?
- Welches Level hast du erreicht?

## 🎮 Besondere Features

### Adaptive Schwierigkeit
Die App passt sich deinem Können an:
- **Gute Leistung (>70% richtig):** Nach 3 erfolgreichen Übungen steigst du ein Level auf
- **Schwierigkeiten (<40% richtig):** Du gehst ein Level runter für einfachere Aufgaben
- **Perfekt für alle Leistungsniveaus:** Jeder kann in seinem Tempo lernen!

### Hilfestellungen
- 💡 **Tipp-Button:** Zeigt einen Hinweis zur Lösung
- ✅ **Detaillierte Lösungen:** Nach jeder Aufgabe wird der Lösungsweg erklärt
- 🔄 **Nochmal versuchen:** Bei falscher Antwort kannst du es erneut probieren

### Lernansatz
Die App verwendet den **klassischen Dreisatz-Ansatz:**

**Beispiel proportional:**
```
5 Eier kosten 2,50€
→ 1 Ei kostet: 2,50€ ÷ 5 = 0,50€
→ 7 Eier kosten: 0,50€ × 7 = 3,50€
```

**Beispiel antiproportional:**
```
3 Arbeiter brauchen 8 Tage
→ Produkt: 3 × 8 = 24
→ 6 Arbeiter brauchen: 24 ÷ 6 = 4 Tage
```

## 📋 Aufgabentypen

Die App enthält verschiedene Aufgabentypen wie im Schulbuch:

### Proportionale Zuordnungen
- 🥚 Einkaufen (Anzahl → Preis)
- 🍎 Gewicht → Preis
- ⏱️ Zeit → Strecke
- 📦 Rezepte vergrößern
- 💶 Arbeitslohn

### Antiproportionale Zuordnungen
- 👷 Arbeiter → Zeit
- 🚗 Geschwindigkeit → Fahrzeit
- ⚙️ Pumpen → Füllzeit
- 📏 Zahnräder

### Gemischte Aufgaben
- Erkennen des Typs notwendig
- Kombinierte Zuordnungen
- Maßstäbe

## 🎯 Lernziele

Nach der Nutzung dieser App kannst du:
- ✅ Zuordnungen erkennen und unterscheiden
- ✅ Proportionale Zuordnungen berechnen
- ✅ Antiproportionale Zuordnungen berechnen
- ✅ Den Dreisatz sicher anwenden
- ✅ Alltagsprobleme mit Zuordnungen lösen

## 💡 Tipps für Lehrkräfte und Eltern

### Für schwächere Schüler
- Beginnt mit Level 1 und arbeitet euch langsam hoch
- Nutzt den Tipp-Button bei Unsicherheit
- Lest gemeinsam die Theorie durch
- Lasst die App die Schwierigkeit automatisch anpassen

### Für stärkere Schüler
- Startet direkt mit dem Quiz
- Versucht, ohne Tipps auszukommen
- Setzt euch das Ziel, Level 5 zu erreichen
- Versucht eine 100% Erfolgsquote

### Empfohlene Lernreihenfolge
1. **Tag 1:** Theorie lesen (alle 4 Tabs)
2. **Tag 2:** Quiz machen (10 Fragen)
3. **Tag 3-5:** Täglich 5-10 Übungen rechnen
4. **Tag 6:** Fortschritt prüfen, Quiz wiederholen
5. **Tag 7:** Schwierige Übungen (Level 4-5)

## 🔧 Technische Details

- **Sprache:** Python 3
- **GUI-Framework:** tkinter
- **Keine zusätzlichen Pakete erforderlich**
- **Funktioniert auf:** Windows, macOS, Linux

## 📝 Lizenz

Diese App wurde für Bildungszwecke erstellt und darf frei verwendet werden.

## 🐛 Probleme melden

Falls du Fehler findest oder Verbesserungsvorschläge hast, erstelle bitte ein Issue im Repository.

## 🎓 Viel Erfolg beim Lernen!

Viel Spaß beim Üben von Zuordnungen! 🚀📚
