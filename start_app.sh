#!/bin/bash
# Starter-Script für die Zuordnungen Lern-App

echo "🚀 Starte Zuordnungen Lern-App..."
echo ""

# Prüfe ob Python3 installiert ist
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 ist nicht installiert!"
    echo "Bitte installiere Python 3 von https://www.python.org"
    exit 1
fi

# Zeige Python-Version
echo "✓ Python Version: $(python3 --version)"

# Prüfe ob tkinter verfügbar ist
python3 -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ tkinter ist nicht installiert!"
    echo ""
    echo "Installation:"
    echo "  Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "  Fedora: sudo dnf install python3-tkinter"
    exit 1
fi

echo "✓ tkinter ist verfügbar"
echo ""
echo "📚 Viel Erfolg beim Lernen!"
echo ""

# Starte die App
python3 zuordnungen_app.py
