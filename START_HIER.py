#!/usr/bin/env python3
"""
DOPPELKLICK AUF DIESE DATEI ZUM STARTEN!

Einfacher Starter für die Zuordnungen Lern-App
"""

import sys
import os

# Wechsle ins richtige Verzeichnis
os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    # Versuche tkinter zu importieren
    import tkinter as tk
    from tkinter import messagebox

    # Teste ob tkinter funktioniert
    root = tk.Tk()
    root.withdraw()

    # Starte die Hauptapp
    import zuordnungen_app

except ImportError as e:
    print("=" * 60)
    print("FEHLER: tkinter ist nicht installiert!")
    print("=" * 60)
    print()
    print("Installation:")
    print("  Ubuntu/Debian: sudo apt-get install python3-tk")
    print("  Fedora: sudo dnf install python3-tkinter")
    print("  macOS/Windows: Normalerweise schon installiert")
    print()
    input("Drücke Enter zum Beenden...")
    sys.exit(1)

except Exception as e:
    print("=" * 60)
    print("FEHLER beim Starten der App:")
    print("=" * 60)
    print(str(e))
    print()
    input("Drücke Enter zum Beenden...")
    sys.exit(1)
