'''
Code to use the IBM Speech to Text service
Code Taken from https://developer.ibm.com/answers/questions/203041/speech-to-text-with-python-error-500.html
Answer given by AlexanderSeroshtan | Jul 28, 2015 at 08:54 AM
This is the code for the Curl request
'''

import requests
import json
'''
https://pypi.python.org/pypi/SpeechRecognition/
pip install pyaudio
pip install speechrecognition
'''
import speech_recognition as sr

'''
curl -u <username>:<password> -X POST --header "Content-Type: audio/flac" --header "Transfer-Encoding: chunked" --data-binary @<path>0001.flac
"https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true"
on page http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/speech-to-text/tutorial.shtml#tutorial
'''
def speechToText(fileName, audioFormat, language):
    if(language=="es"):
        model = "es-ES_BroadbandModel"
    else:
        model = "en-US_BroadbandModel"

    #URL of the IBM Speech to text
    url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true&model='+model
    # The command again sets the continuous parameter to true. It also sets the timestamps parameter to true to request
    # that the service return timestamps to indicate the beginning and end of each word in the audio stream. And it sets
    #  the max_alternatives parameter to 3 to direct the service to return the three most likely alternatives for the transcription.
    #url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true&timestamps=true&max_alternatives=3&word_alternatives_threshold=0.25'
    #For spanish
    #model=es - ES_BroadbandModel
    #Credentials on the Bluemix.net system
    username = ''
    password = ''
    #Headers for the audio content
    headers = {'Content-Type': 'audio/'+audioFormat}
    #File to transcribe
    audio = open('recordings/'+fileName, 'rb')
    #Request to the  page
    r = requests.post(url, data=audio, headers=headers, auth=(username, password))
    return r.text


'''
curl -u "{username}":"{password}" -H "Content-Type: application/json" -d "{\"text\": \"Hi Team, I know the times are difficult! Our sales have been disappointing for the past three quarters for our data analytics product suite. We have a competitive data analytics product suite in the industry. But we need to do our job selling it! \"}" "https://gateway.watsonplatform.net/tone-analyzer-beta/api/v3/tone?version=2016-02-11"
http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/tone-analyzer/tutorial.shtml
'''
def toneAnalizer(basetext):
    # URL of the IBM Speech to text
    url = 'https://gateway.watsonplatform.net/tone-analyzer-beta/api/v3/tone?version=2016-02-11'
    # Credentials on the Bluemix.net system
    username = ""
    password = ""
    # Headers for the audio content
    headers = {'Content-Type': 'application/json'}
    # Text to evaluate
    text = "{\"text\": \" "+basetext+" \"}"

    # Request to the  page
    r = requests.post(url, data=text, headers=headers, auth=(username, password))
    # Printing the transcription
    print(r.text)

'''
#jsonTranscription = speechToText("0001.flac", "flac", "en")
#jsonTranscription = speechToText("english.wav", "wav", "en")
jsonTranscription = '{"results": [{"alternatives": [{"confidence": 0.899, "transcript": "you\'re a very interesting tool "}], "final": true}], "result_index": 0}'
result = json.loads(jsonTranscription)
print(jsonTranscription)
#https://geekytheory.com/como-utilizar-json-en-python/
transcription = result['results'][0]['alternatives'][0]['transcript']
#['alternatives']['transcript']
print(transcription)
#toneAnalizer('Hi Team, I know the times are difficult! Our sales have been disappointing for the past three quarters for our data analytics product suite. We have a competitive data analytics product suite in the industry. But we need to do our job selling it!')
toneAnalizer(transcription)
'''

'''
Function using Google speech recognition software
'''
def speechToTextGoogle(fileName, lang):
    r = sr.Recognizer()
    with sr.WavFile('recordings/'+fileName) as source:
        audio = r.record(source)  # read the entire WAV file
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said: " + r.recognize_google(audio,language=lang))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

speechToTextGoogle("0001.flac", "en")
speechToTextGoogle("english.wav", "en")
speechToTextGoogle("spanish.wav", "es")