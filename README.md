# Mathe7 - Mathematik Lern-Repository

Dieses Repository enthält Python-Projekte zum Lernen und Üben von Mathematik, mit Fokus auf **Fehlerbehandlung** und **interaktives Lernen**.

## 📂 Projekte

### 1. 📐 Zuordnungen Lern-App

Eine interaktive Desktop-Anwendung zum Lernen von proportionalen und antiproportionalen Zuordnungen.

**Features:**
- 📖 Ausführliche Theorie mit 4 Kapiteln
- 🎯 Quiz zum Erkennen von Zuordnungstypen (10 Fragen)
- ✏️ Rechenübungen mit adaptiver Schwierigkeit (Level 1-5)
- 📊 Fortschrittsverfolgung
- 💡 Hilfestellungen und Tipps
- 🎮 Intelligente Levelanpassung für jeden Schüler

**Start:**
```bash
# Linux/Mac
./start_app.sh

# oder direkt
python3 zuordnungen_app.py

# Windows
start_app.bat
```

**Dokumentation:** [README_APP.md](README_APP.md)

---

### 2. 🔧 Mathematical Utilities mit Error Handling

Eine Sammlung mathematischer Funktionen, die **best practices für Error Handling** demonstrieren.

**Features:**
- Benutzerdefinierte Exception-Hierarchie
- Umfassende Input-Validierung
- Klare, informative Fehlermeldungen
- 8 Funktionen mit robuster Fehlerbehandlung

**Funktionen:**
- `safe_divide()` - Sichere Division mit Zero-Check
- `calculate_average()` - Durchschnitt mit Validierung
- `calculate_square_root()` - Wurzel mit Domain-Check
- `calculate_factorial()` - Fakultät mit Constraints
- `calculate_power()` - Potenzierung mit Edge-Cases
- `find_nth_element()` - Sicheres List-Indexing
- `calculate_percentage()` - Prozentrechnung

**Tests ausführen:**
```bash
python3 test_math_utils.py
```

---

## 🚀 Schnellstart

### Voraussetzungen
- Python 3.6 oder höher
- tkinter (für die Zuordnungen-App)

### Installation prüfen
```bash
python3 --version
python3 -c "import tkinter"
```

Falls tkinter fehlt:
- **Ubuntu/Debian:** `sudo apt-get install python3-tk`
- **Fedora:** `sudo dnf install python3-tkinter`
- **macOS/Windows:** Normalerweise enthalten

### Projekte nutzen

**Zuordnungen-App starten:**
```bash
python3 zuordnungen_app.py
```

**Math Utils testen:**
```bash
python3 test_math_utils.py
```

**Math Utils verwenden:**
```python
import math_utils

# Beispiel
result = math_utils.safe_divide(10, 2)
print(result)  # 5.0
```

---

## 📚 Lernziele

### Für Schüler (Zuordnungen-App):
- ✅ Zuordnungen erkennen und unterscheiden
- ✅ Proportionale und antiproportionale Zuordnungen berechnen
- ✅ Dreisatz-Methode sicher anwenden
- ✅ Alltagsprobleme mit Mathematik lösen

### Für Entwickler (Math Utils):
- ✅ Robuste Fehlerbehandlung implementieren
- ✅ Custom Exceptions verwenden
- ✅ Input-Validierung durchführen
- ✅ Aussagekräftige Fehlermeldungen schreiben
- ✅ Edge-Cases behandeln

---

## 📖 Dokumentation

- **Zuordnungen App:** [README_APP.md](README_APP.md) - Ausführliche Anleitung
- **Math Utils:** Siehe Docstrings in `math_utils.py`
- **Error Handling Best Practices:** Siehe Code-Kommentare

---

## 🎯 Projektziele

Dieses Repository demonstriert zwei wichtige Aspekte der Software-Entwicklung:

1. **Bildung & Interaktivität**
   - Intuitive Benutzeroberflächen
   - Adaptive Lernsysteme
   - Sofortiges Feedback
   - Motivierende Elemente

2. **Code-Qualität & Robustheit**
   - Umfassende Fehlerbehandlung
   - Klare Fehlermeldungen
   - Input-Validierung
   - Testbarkeit

---

## 📂 Projektstruktur

```
Mathe7/
├── README.md                  # Diese Datei
├── README_APP.md             # Dokumentation Zuordnungen-App
│
├── zuordnungen_app.py        # Hauptanwendung
├── start_app.sh              # Starter für Linux/Mac
├── start_app.bat             # Starter für Windows
│
├── math_utils.py             # Math-Bibliothek mit Error Handling
├── test_math_utils.py        # Tests für Math-Bibliothek
│
├── requirements.txt          # Python-Abhängigkeiten
└── .gitignore               # Git-Konfiguration
```

---

## 🤝 Beitragen

Verbesserungsvorschläge sind willkommen! Besonders:
- Neue Übungsaufgaben für die Zuordnungen-App
- Weitere mathematische Funktionen mit Error Handling
- Übersetzungen in andere Sprachen
- UI-Verbesserungen

---

## 📝 Lizenz

Dieses Projekt wurde für Bildungszwecke erstellt und darf frei verwendet werden.

---

## 🎓 Viel Erfolg!

Egal ob du Mathematik lernst oder besseren Code schreiben möchtest - dieses Repository hilft dir weiter! 🚀

Bei Fragen oder Problemen, erstelle bitte ein Issue im Repository.
