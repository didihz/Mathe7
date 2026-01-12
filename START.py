#!/usr/bin/env python3
"""
🎓 ZUORDNUNGEN LERN-APP - BROWSER VERSION 🎓

Einfach diese Datei starten!
Der Browser öffnet sich automatisch.
"""

import sys
import os

# Wechsle ins richtige Verzeichnis
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("=" * 60)
print("🎓 ZUORDNUNGEN LERN-APP")
print("=" * 60)
print()

# Prüfe Python-Version
if sys.version_info < (3, 6):
    print("❌ FEHLER: Python 3.6 oder höher erforderlich!")
    print(f"   Aktuelle Version: {sys.version}")
    print()
    input("Drücke Enter zum Beenden...")
    sys.exit(1)

print(f"✓ Python {sys.version.split()[0]} gefunden")

# Prüfe Flask
try:
    import flask
    print("✓ Flask ist installiert")
except ImportError:
    print("❌ Flask ist nicht installiert!")
    print()
    print("Installation mit:")
    print("  pip install flask")
    print()
    print("oder:")
    print("  pip3 install flask")
    print()
    input("Drücke Enter zum Beenden...")
    sys.exit(1)

print()
print("🚀 Starte Server...")
print("📱 Browser öffnet sich gleich automatisch...")
print()
print("=" * 60)
print()

# Starte die Web-App
try:
    import web_app
except KeyboardInterrupt:
    print()
    print()
    print("=" * 60)
    print("👋 App wurde beendet. Bis bald!")
    print("=" * 60)
    sys.exit(0)
except Exception as e:
    print()
    print("=" * 60)
    print("❌ FEHLER beim Starten:")
    print("=" * 60)
    print(str(e))
    print()
    input("Drücke Enter zum Beenden...")
    sys.exit(1)
