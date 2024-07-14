import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

def talk(text):
    def run_talk():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    t = threading.Thread(target=run_talk)
    t.start()

def process_command(command):
    response = ""
    if 'play' in command:
        song = command.replace('play', '')
        response = 'playing ' + song
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        response = 'Current time is ' + time
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        response = info
    elif 'what is' in command:
        person1 = command.replace('what is', '')
        info = wikipedia.summary(person1, 1)
        response = info
    elif 'how are you doing today' in command:
        response = 'I am doing good'
    elif 'joke' in command:
        response = pyjokes.get_joke()
    else:
        response = 'Please say the command again.'

    return response

@app.route('/alexa', methods=['POST'])
def alexa():
    data = request.get_json()
    command = data.get('command', '').lower()
    response_text = process_command(command)
    talk(response_text)
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)


