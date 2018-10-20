from gtts import gTTS 
import speech_recognition as sr 
import os
import webbrowser
import smtplib

def talkToDeepu(audio):
	print(audio)
	tts = gTTS(text=audio,lang='en')
	tts.save('audio.mp3')
	os.system('mpg123 audio.mp3')

def DeepsCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('hello anudeep')
		r.pause_threshold=1
		r.adjust_for_ambient_noise(source,duration=1)
		audio = r.listen(source)
	try :	
		command = r.recognize_google(audio)
		print('you said: '+command+'\n')

	except sr.UnknownVakueError:
		assistant(DeepsCommand())

	return command

def assistant(command):
	if 'facebook' in command:
		chrome_path = '/usr/bin/google-chrome'
		url = 'https://www.facebook.com'
		webbrowser.get(chrome_path).open(url)
		
	if 'youtube' in command:
		chrome_path = '/usr/bin/google-chrome'
		url = 'https://www.youtube.com'
		webbrowser.get(chrome_path).open(url)

	if 'github' in command:
		chrome_path = '/usr/bin/google-chrome'
		url = 'https://www.github.com'
		webbrowser.get(chrome_path).open(url)

	if 'hello' in command:
		talkToDeepu('how can i help you ?')
	

talkToDeepu('hello anudeep')

while True:
	assistant(DeepsCommand())	 	 				
