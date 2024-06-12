# Dokumentation

Dieses Skript wird verwendet, um einen Chatbot mit dem OpenAI GPT-4 Modell und Furhats Remote API zu erstellen. Der Chatbot heißt "Maria Vogel" und kommuniziert auf Deutsch.

## Abhängigkeiten

- `furhat_remote_api`: Wird verwendet, um eine Verbindung zur Remote API von Furhat herzustellen, die es dem Skript ermöglicht, einen Furhat-Roboter zu steuern.
- `openai`: Wird verwendet, um eine Verbindung zur API von OpenAI herzustellen, die es dem Skript ermöglicht, das GPT-4 Modell zu nutzen.
- `atexit`: Wird verwendet, um eine Funktion zu registrieren, die aufgerufen wird, wenn das Skript beendet wird. Diese Funktion löscht den während der Ausführung des Skripts erstellten Assistenten.

## Funktionen

`delete_assistant(assistant_id)`: Diese Funktion löscht den Assistenten mit der gegebenen ID. Sie wird registriert, um aufgerufen zu werden, wenn das Skript beendet wird.

## Ausführung

1. Das Skript beginnt damit, eine Aufforderung aus einer Textdatei namens `"prompt.txt"` zu lesen.
2. Es stellt dann eine Verbindung zur Remote API von Furhat her und setzt die Stimme des Furhat-Roboters auf `"Marlene"`.
3. Das Skript stellt dann eine Verbindung zur API von OpenAI her.
4. Ein Assistent namens "Maria Vogel" wird mit der OpenAI API erstellt. Die Anweisungen für den Assistenten werden aus der Textdatei gesetzt und das verwendete Modell ist `"gpt-4o"`.
5. Ein Thread wird erstellt, um den Chatverlauf zu verarbeiten.
6. Die Funktion `delete_assistant` wird registriert, um aufgerufen zu werden, wenn das Skript beendet wird. Die ID des Assistenten wird als Argument an die Funktion übergeben.
7. Das Skript tritt dann in eine Endlosschleife ein, in der es auf eine Nachricht vom Benutzer wartet. Wenn eine Nachricht empfangen wird, wird sie an die OpenAI API gesendet und eine Antwort generiert. Die Antwort wird dann vom Furhat-Roboter gesprochen.
