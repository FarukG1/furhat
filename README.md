# Furhat + ChatGPT (Maria Vogel)

In diesem Projekt verbinden wir ChatGPT mit dem Furhat-Roboter, sodass ChatGPT durch Furhat hören und mit Personen kommunizieren kann. Wir schlagen damit eine Brücke zwischen der virtuellen und der realen Welt und nutzen Furhat als Schnittstelle. Die Aufgabe besteht darin, ChatGPT in "Maria Vogel" zu verwandeln, wofür wir einen speziellen Prompt erstellt haben.

## Installation

Zunächst erstellt man eine virtuelle Python-Umgebung. Nach deren Aktivierung können die benötigten Python-Pakete installiert werden. Befolgen Sie dazu die folgenden Schritte:

Linux & MacOS:

1. ```python -m venv ./venv```
2. ```source ./venv/bin/activate```
3. ```pip install -r requirements.txt```

Windows:

1. ```python -m venv ./venv```
2. ```.\venv\Scripts\activate```
3. ```pip install -r requirements.txt```

## Configuration

Für die Konfiguration werden zwei Elemente benötigt:

1. **Prompt**: Dieser befindet sich in der Datei `prompt.txt`.
2. **OpenAI API Key**: Dieser muss in einer Datei namens `.env` hinterlegt werden, wobei der Schlüssel `OPENAI_API_KEY` lauten sollte (Beispiel: `OPENAI_API_KEY=XYZ`).

## Dokumentation

Dieses Skript dient der Erstellung eines deutschsprachigen Chatbots namens "Maria Vogel", der auf dem OpenAI GPT-4 Modell und der Furhat Remote API basiert.

### Abhängigkeiten

- `furhat_remote_api`: Ermöglicht die Verbindung zur Furhat Remote API, um den Furhat-Roboter zu steuern.
- `openai`: Stellt die Verbindung zur OpenAI API her, um das GPT-4 Modell zu nutzen.
- `atexit`: Registriert eine Funktion, die beim Beenden des Skripts aufgerufen wird, um den erstellten Assistenten zu löschen.

### Funktionen

- `delete_assistant(assistant_id)`: Diese Funktion löscht den Assistenten mit der angegebenen ID und wird beim Beenden des Skripts automatisch aufgerufen.

### Ausführung

1. Das Skript liest eine Eingabeaufforderung aus der Datei `prompt.txt`.
2. Es verbindet sich mit der Furhat Remote API und setzt die Stimme des Furhat-Roboters auf "Vicki".
3. Es stellt eine Verbindung zur OpenAI API her.
4. Ein Assistent namens "Maria Vogel" wird mittels der OpenAI API erstellt. Die Anweisungen für den Assistenten werden aus der Textdatei übernommen und das Modell "gpt-4o" wird verwendet.
5. Ein Thread wird gestartet, um den Chatverlauf zu verwalten.
6. Die Funktion `delete_assistant` wird registriert und beim Skriptende aufgerufen, um den Assistenten zu löschen. Die ID des Assistenten wird an die Funktion übergeben.
7. Das Skript geht in eine Endlosschleife über und wartet auf Nachrichten vom Benutzer. Bei Empfang einer Nachricht wird diese an die OpenAI API gesendet, die eine Antwort generiert und diese wird dann vom Furhat-Roboter ausgesprochen.

### Gruppenmitglieder

- Mabrouk Abdelkafi
- Ismail Adruich
- Diyar Altin
- Faruk-Kerim Güc
