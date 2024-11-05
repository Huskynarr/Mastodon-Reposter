# Mastodon-Reposter

## Beschreibung
Dieses Python-Skript ermöglicht das Rebloggen und Liken von Mastodon-Posts von verschiedenen Accounts.
Es verwendet die `mastodon.py` Bibliothek, um auf die Mastodon API zuzugreifen und die Aktionen durchzuführen.

## Voraussetzungen
- Python 3.x
- Mastodon.py Bibliothek (siehe `requirements.txt`)

## Installation
1. Klone dieses Repository:
   ```
   git clone git@github.com:Huskynarr/Mastodon-Reposter.git
   ```

2. Erstelle eine virtuelle Umgebung (optional, aber empfohlen):
   ```
   python -m venv venv
   source venv/bin/activate  # Für Windows: venv\Scripts\activate
   ```

3. Installiere die Abhängigkeiten:
   ```
   pip install -r requirements.txt
   ```

4. Erstelle eine `.env` Datei (optional), um Zugangsdaten sicher zu speichern.
   ```
   MASTODON_URL=https://social.xboxdev.com
   ACCESS_TOKEN=zamUreZ5FLbMpg3mJ3Ng6RGYxnFkZLS45n4ZzVNro7A
   ACCOUNTS="@xboxdev@toad.social,@example1@mastodon.social,@example2@mastodon.social"
   ```

## Verwendung
1. Passe die URL, das Token und die Accounts in der Skript-Datei oder `.env` Datei an.
2. Führe das Skript aus:
   ```
   python Mastodon.py
   ```
3. Das Skript rebloggt und liked die neuesten Posts der angegebenen Accounts.

## To-Do
- Unterstützung für eine `.env` Datei hinzufügen, um sensible Daten besser zu schützen.
- Fehlerbehandlung verbessern, um spezifischere Fehlermeldungen auszugeben.
- Tests für das Skript hinzufügen.
- Logging-Funktionalität integrieren, um die Aktivitäten besser nachverfolgen zu können.
