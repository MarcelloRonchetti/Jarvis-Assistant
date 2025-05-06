Jarvis - Assistente Vocale Personale (Python)
============================================

Jarvis è un assistente vocale personale sviluppato in Python. Riconosce comandi vocali in italiano e può aprire applicazioni, siti web e rispondere a frasi semplici. Funziona su Windows e include una scorciatoia da tastiera per avviarlo.

------------------------------------------------------------
REQUISITI
------------------------------------------------------------

Software:
- Windows OS
- Python 3.9 o superiore
- Microfono funzionante

Librerie Python richieste:
- SpeechRecognition
- gTTS
- keyboard
- pyaudio (usa pipwin per installarlo se necessario)

Installa tutte le dipendenze con i seguenti comandi:

pip install SpeechRecognition gTTS keyboard
pip install pipwin
pipwin install pyaudio

------------------------------------------------------------
STRUTTURA DEL PROGETTO
------------------------------------------------------------

Jarvis/
├── Jarvis.py            <- Script principale
├── start_jarvis.bat     <- File batch opzionale per avvio rapido
├── README.txt           <- Questo file

------------------------------------------------------------
AVVIO DEL PROGRAMMA
------------------------------------------------------------

1. Dal terminale:
   python Jarvis.py

2. Oppure crea un file batch chiamato start_jarvis.bat con il seguente contenuto:

@echo off
python Jarvis.py
pause

------------------------------------------------------------
COMANDI VOCALI DISPONIBILI
------------------------------------------------------------

Frasi di esempio:
- "Apri YouTube" -> apre il sito
- "Apri calcolatrice" -> avvia la calcolatrice
- "Chiudi notepad" -> chiude l'app
- "Ciao", "Come stai?", "Esci", "Fermati" -> risposte vocali

Siti web supportati:
- Google
- YouTube
- ChatGPT
- Chess.com

Applicazioni supportate (modificabili nel dizionario "APPS"):
- calcolatrice
- notepad
- Discord
- Raft
- Arma 3
- Counter-Strike 2

Puoi aggiungere altre app nel dizionario all’interno del file Jarvis.py.

------------------------------------------------------------
TASTI DI SCELTA RAPIDA
------------------------------------------------------------

CTRL + ALT + O     -> Avvia Jarvis
ESC                -> Termina il programma

------------------------------------------------------------
NOTE AGGIUNTIVE
------------------------------------------------------------

- La sintesi vocale (gTTS) è disattivata di default.
  Puoi riattivarla togliendo il commento alla funzione `text_to_speech()` nel main.

- La lingua è fissata su italiano. Per riattivare la scelta vocale della lingua, modifica la funzione choose_language().

------------------------------------------------------------
FUTURI SVILUPPI
------------------------------------------------------------

- Supporto per più lingue
- Integrazione con AI
- Comandi per dispositivi domotici

------------------------------------------------------------
AUTORE
------------------------------------------------------------

Sviluppato da [Marcello Ronchetti]


