import cv2
import os
import modules.functions as function
import modules.speech as speech
import modules.getIntent as Intent


def get_speech():
    engine = speech.Speech()
    listening = False
    intent = None
    while True:
        cam = cv2.VideoCapture(0)
        if not listening:
            resp = engine.recognize_speech()
            if(resp != None):
                intent = Intent.get_intent(resp)
            if(intent == 'anywea' and resp != None):
                listening = True

        else:
            engine.text_to_speech("What can I help you with?")
        
            intent = ''
            engine.text_to_speech("Listening")
            resp = engine.recognize_speech()
            engine.text_to_speech("Processing")

            if(resp != None):
                intent = Intent.get_intent(resp)
                intent = intent.lower()



                if(intent == 'weather'):
                    function.weatherForecaste()

                elif intent == 'stop':
                    listening = False
                    engine.text_to_speech("OK Quitting now, Please tell me if you need my assistance again.")

                elif resp != None:
                    engine.text_to_speech("Sorry, I did not understood. Can you say it again?")

            cam.release()

