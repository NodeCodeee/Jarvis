import asyncio
import speech_recognition as sr
from commands import wizbulbs, arduino


WizBulbTurnOnArgs = ['włącz światło', 'włącz', 'zapal', 'turn on']
WizBulbTurnOffArgs = ['wyłącz światło', 'wyłącz', 'zgaś', 'turn off']
WizBulbChangeColorArgs = ['zmień kolor na', 'ustaw kolor na', 'ustaw kolor']
WizBulbChangeBrightnessArgs = ['ustaw moc na', 'ustaw moc']

def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='pl_PL')
        text = text.lower()
        print(f'TEXT: {text} ')

        if any(arg in text for arg in WizBulbTurnOnArgs):

            asyncio.run(arduino.turnOn())

        elif any(arg in text for arg in WizBulbTurnOffArgs):

            asyncio.run(arduino.turnOff())

        elif any(arg in text for arg in WizBulbChangeColorArgs):

            asyncio.run(wizbulbs.setColor(text))

        elif any(arg in text for arg in WizBulbChangeBrightnessArgs):

            asyncio.run(wizbulbs.setColor(text))

        
  
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
