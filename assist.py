import pyttsx3
import datetime
import speech_recognition as sr 
engine =pyttsx3.init()


def speak(audio):
	engine.say(audio)
	engine.runAndWait()
	
def time():
	Time = datetime.datetime.now().strftime("%I:%M:%S")
	speak(Time)

def date():
	year = int(datetime.datetime.now().year)
	month = int(datetime.datetime.now().month)
	day = int(datetime.datetime.now().day)
	hour = datetime.datetime.now().hour 
	if hour >=6 and hour < 12:
		speak(" Good Morning")
	elif hour >=12 and hour < 18:
		speak(" Good Afternoon ")
	elif hour >=18 and hour <24:
		speak(" Good eVENING ")
	else:
		speak("Good Night") 
	speak(day)
	speak(month)
	speak(year)
	
def wishme():
	speak ("Welcome back")
	speak("Current Time is ")
	time()
	speak("Current Date is ")
	date()
	speak(" AI at your service")

def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening")
		r.puase_threshold=1
		audio = r.listen(source)
	
	try:
		print("Recognizing")
		query = r.recognize_google(audio,language='en-in')
		print(query)
		
	except Exception as e: 
		print(e)
		speak("Can you give it another try")
		return "None"
	return query 
#wishme()
takeCommand()