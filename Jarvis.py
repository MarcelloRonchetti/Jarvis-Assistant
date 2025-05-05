
import sys
import speech_recognition
from gtts import gTTS
import os
import subprocess
import webbrowser
import keyboard

# Dizionario delle impostazioni linguistiche
LANGUAGES = {
    "italiano": "it-IT",
    "inglese": "en-US"
}

APPS = {
    "calcolatrice": "calc.exe",  
    "calculator": "calc.exe",
    "notepad": "notepad.exe",
    "discord": "C:/Users/marcy/AppData/Local/Discord/Update.exe --processStart Discord.exe",
    "arma 3": "C:/Users/marcy/Desktop/Arma 3.url",
    "raft": r"C:\Users\marcy\Desktop\Raft.url",
    "zattera": r"C:\Users\marcy\Desktop\Raft.url",
    "cs 2": r"C:\Users\marcy\Desktop\Counter-Strike 2.url"
    
    
      
}

SITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "chat": "https://chatgpt.com/?model=auto",
    "scacchi":"https://www.chess.com/home",
    "chess":"https://www.chess.com/home"
    # Aggiungi altri siti come desideri
}



# Inizializza il riconoscimento vocale
recognizer = speech_recognition.Recognizer()



def lingua_parlata():
    with speech_recognition.Microphone() as source:
        print ("Parla/speak")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Riconoscimento vocale in base alla lingua scelta
        text = recognizer.recognize_google(audio, language="it-IT")
        print("Hai detto:", text)
        if "italian" in text.lower() or "italiano" in text.lower() or "italy" in text.lower():
            return "italiano"
        elif "inglese" in text.lower() or "english" in text.lower():
            return "inglese"
        else:
            return ""
    
    except speech_recognition.UnknownValueError:
        print("Non ho capito l'audio.")
        return ""
    except speech_recognition.RequestError:
        print("Errore di rete.")
        return ""

 
    
# Funzione per scegliere la lingua
def choose_language():
    
    print("Scegli una lingua, lingue disponibili: italiano ")
    language_choice = lingua_parlata()
    if language_choice in LANGUAGES:
        return LANGUAGES[language_choice], language_choice
    else:
        print("Lingua non supportata.")
        return None, None



# Funzione per riconoscere la voce e convertirla in testo
def recognize_speech(language_code):
    with speech_recognition.Microphone() as source:
        print(f"Parla ora ({language_code})...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Riconoscimento vocale in base alla lingua scelta
        text = recognizer.recognize_google(audio, language=language_code)
        print("Hai detto:", text)
        return text
    except speech_recognition.UnknownValueError:
        print("Non ho capito l'audio.")
        return ""
    except speech_recognition.RequestError:
        print("Errore di rete.")
        return ""



def open_website(site_name):
    url = SITES.get(site_name)
    if url:
        print(f"Apro {url}...")
        webbrowser.open(url)
        return f"Apro il sito {site_name}."
    else:
        return "Sito non trovato. Controlla se è nel dizionario dei siti."  
    
    
     
def close_application(app_name):
    if app_name in APPS:
        try:
            print(f"Chiudo {app_name}...")
            subprocess.run(f"taskkill /f /im {APPS[app_name]}", shell=True)
            return f"Ho chiuso {app_name}."
        except Exception as e:
            print("Errore nella chiusura dell'app:", e)
            return "Non sono riuscito a chiudere l'applicazione."
    else:
        return "Applicazione non trovata."

    
   
def open_application(app_name):
    if app_name in APPS:
        path = APPS[app_name]
        
        # Controlla se il file è un file .url
        if path.endswith(".url"):
            try:
                print(f"Apro il file di collegamento {app_name}...")
                
                os.startfile(path)  # Usa os.startfile per i file .url
                
                return f"Apro {app_name} tramite il collegamento sul desktop."
            
            except Exception as e:
                print("Errore nell'apertura del collegamento:", e)
                return "Non sono riuscito ad aprire il collegamento specificato."
        else:
            try:
                print(f"Apro {app_name}...")
                subprocess.Popen(path)
                return f"Apro {app_name}."
            except Exception as e:
                print("Errore nell'apertura dell'app:", e)
                return "Non sono riuscito ad aprire l'applicazione."
    else:
        return "Applicazione non trovata."
 
 
    
# Funzione per convertire il testo in voce
def text_to_speech(text, language_code):
    tts = gTTS(text=text, lang=language_code.split("-")[0])  # Usa solo il codice di lingua (es. "it")
    tts.save("output.mp3")
    os.system("start output.mp3")  # Su Windows; per macOS usa "afplay output.mp3", su Linux "mpg321 output.mp3"




# Funzione per generare una risposta in base al testo riconosciuto
def generate_response(user_input, language_choice):
    user_input = user_input.lower()
    
    # Comando per aprire un sito web
    if "apri" in user_input or "open" in user_input:
        words = user_input.split()
        site_name = None
        for word in words:
            if word in SITES:  # Cerca il nome del sito nel dizionario
                site_name = word
                break
        
        if site_name:
            return open_website(site_name)
    
    if "open" in user_input.lower() or "apri" in user_input.lower():
        for app in APPS.keys():
            if app in user_input.lower():
                return open_application(app)
    
    # Comando di chiusura
    elif "close" in user_input.lower() or "chiudi" in user_input.lower():
        for app in APPS.keys():
            if app in user_input.lower():
                return close_application(app)
            
    if "fermati" in user_input or "stop" in user_input:
        print("Chiusura del programma.")
        sys.exit()  # Termina il programma        
            
    if "ciao" in user_input.lower() or "hello" in user_input.lower():
        return "Ciao!" if language_choice == "italiano" else "Hello!"
    
    elif "come stai" in user_input.lower() or "how are you" in user_input.lower():
        return "Sto bene, grazie!" if language_choice == "italiano" else "I'm good, thank you!"
    
    elif "esci" in user_input.lower() or "finish" in user_input.lower():
        return "Arrivederci!" if language_choice == "italiano" else "Goodbye!"
    
    
    
        
    else:
        return "Non ho capito la tua richiesta." if language_choice == "italiano" else "I didn't understand your request."
    
    


# Funzione principale del programma
def main():
    # Scelta della lingua
    '''language_code, language_choice = choose_language()
    if not language_code:
        return
    if language_choice=="it-IT":
        print(f"Modalità {language_choice.capitalize()} selezionata.")
    elif language_choice=="en-US":
        print(f"Mode  {language_choice.capitalize()} initialized.")
    '''
    language_code="it-IT"
    language_choice="italiano"
    while True:
        # Riconoscimento vocale
        user_input = recognize_speech(language_code)
        
        if user_input:
            # Genera una risposta in base all'input dell'utente
            
            response = generate_response(user_input, language_choice)
            
            # Se la risposta è un saluto finale, interrompe il ciclo
            if response.lower() in ["arrivederci!", "goodbye!"]:
                break 
            
            # Sintesi vocale della risposta
            print("Risposta:", response)
            #text_to_speech(response, language_code)            
            
            
if __name__ == "__main__":
    main()
keyboard.add_hotkey('ctrl+alt+o', main)

keyboard.wait('esc')
print("Programma terminato.")

