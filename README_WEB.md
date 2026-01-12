# 🌐 Zuordnungen Lern-App - Browser Version

Eine moderne, interaktive **Web-Anwendung** zum Lernen von proportionalen und antiproportionalen Zuordnungen - **läuft im Browser**!

## ✨ NEU: Browser-Version!

Die App läuft jetzt **im Browser** - viel einfacher und moderner!
- 🌐 Keine Desktop-Installation nötig
- 📱 Funktioniert auf allen Geräten
- 🎨 Schönes, modernes Design
- ⚡ Schnelle Ladezeiten

## 🚀 SO EINFACH GEHT'S:

### 1. Voraussetzungen

Installiere **Flask** (nur einmal):

```bash
pip install flask
```

oder:

```bash
pip3 install flask
```

### 2. App starten

**Am einfachsten: Doppelklick auf `START.py`**

Oder in der Kommandozeile:

```bash
python3 START.py
```

oder:

```bash
python START.py
```

### 3. Fertig!

- Der Browser öffnet sich **automatisch**
- Die App läuft auf: `http://127.0.0.1:5000`
- Zum Beenden: `Strg+C` in der Kommandozeile drücken

## 📚 Features

### 📖 Theorie lernen
- 4 interaktive Kapitel mit Tabs
- Was sind Zuordnungen?
- Proportionale Zuordnungen (je mehr → desto mehr)
- Antiproportionale Zuordnungen (je mehr → desto weniger)
- Erkennungsmerkmale und Methoden

### 🎯 Quiz (10 Fragen)
- Erkenne proportional vs. antiproportional vs. weder-noch
- Sofortige Rückmeldung
- Ausführliche Erklärungen
- Score-Tracking

### ✏️ Interaktive Übungen
- **5 Schwierigkeitslevel** (1-5)
- **Adaptive Schwierigkeit:**
  - Automatisches Level-Up bei guter Leistung (>70%)
  - Automatisches Level-Down bei Schwierigkeiten (<40%)
  - Perfekt für jeden Schüler!

- **Beispielaufgaben:**
  - Level 1: "5 Eier kosten 2,50€. Was kosten 7 Eier?"
  - Level 3: "4 Arbeiter brauchen 6 Tage. Wie lange brauchen 8 Arbeiter?"
  - Level 5: Komplexe Mehrschritt-Aufgaben

- **Hilfe-System:**
  - Tipp-Button für Hinweise
  - Detaillierte Lösungswege
  - Schritt-für-Schritt Erklärungen

### 📊 Fortschrittsverfolgung
- Aktuelles Level
- Erfolgsquote in Prozent
- Anzahl gelöster Aufgaben
- Quiz-Score
- Motivierende Rückmeldungen
- Level-Übersicht mit Fortschritt

## 🎨 Design

- 🎨 **Modernes, farbenfrohes Design**
- 📱 **Responsive** - funktioniert auf Handy, Tablet, Desktop
- ⚡ **Schnell und flüssig**
- 💫 **Animationen und Übergänge**
- 🎯 **Klare, übersichtliche Navigation**

## 📁 Projektstruktur

```
Mathe7/
├── START.py                  ⭐ HIER STARTEN!
├── web_app.py               # Flask-Server
│
├── templates/               # HTML-Dateien
│   ├── base.html
│   ├── index.html          # Hauptmenü
│   ├── theorie.html        # Theorie-Seite
│   ├── quiz.html           # Quiz-Seite
│   ├── uebungen.html       # Übungs-Seite
│   └── fortschritt.html    # Fortschritts-Seite
│
└── static/                  # CSS & JavaScript
    ├── css/
    │   └── style.css       # Komplettes Design
    └── js/
        └── main.js         # JavaScript-Funktionen
```

## 💡 Tipps

### Für Schüler:
1. **Lies zuerst die Theorie** (alle 4 Kapitel)
2. **Mache das Quiz** zum Üben
3. **Löse täglich 5-10 Übungen**
4. Nutze den **Tipp-Button** bei Problemen
5. Lies die **Lösungswege** genau durch

### Für Lehrer:
- Die App speichert den Fortschritt in der **Session**
- Mehrere Schüler = mehrere Browser-Tabs oder verschiedene Browser
- Fortschritt kann zurückgesetzt werden
- Ideal für Hausaufgaben und Übungsphasen

## 🔧 Technische Details

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Keine Datenbank:** Session-basiert
- **Port:** 5000 (lokal)
- **Python-Version:** 3.6+

## ❓ Probleme?

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip install flask
```

### "Port 5000 already in use"
Schließe andere Programme die Port 5000 nutzen, oder ändere den Port in `web_app.py`:
```python
app.run(debug=True, use_reloader=False, port=5001)
```

### Browser öffnet sich nicht automatisch
Öffne manuell: `http://127.0.0.1:5000`

### Fortschritt geht verloren
Das ist normal bei Session-basiertem Speicher. Für dauerhaften Speicher müsste eine Datenbank integriert werden.

## 🆚 Desktop-Version vs. Web-Version

| Feature | Desktop (tkinter) | Web (Browser) |
|---------|------------------|---------------|
| Installation | tkinter | Flask |
| Start | `python zuordnungen_app.py` | `python START.py` |
| Aussehen | System-Style | Modern, colorful |
| Geräte | Nur Desktop | Alle Geräte |
| Empfehlung | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**Empfehlung:** Nutze die **Web-Version** (Browser) - sie ist moderner und läuft überall!

## 🎓 Viel Erfolg beim Lernen!

Die App macht das Lernen von Zuordnungen einfach und macht Spaß! 🚀

Bei Fragen oder Problemen, erstelle ein Issue im Repository.

---

**Quick Start:**
```bash
pip install flask
python3 START.py
```

**Das war's!** Der Browser öffnet sich automatisch. 🎉
