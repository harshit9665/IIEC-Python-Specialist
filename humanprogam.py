import pyttsx3
import os
# init function to get an engine instance for the speech synthesis  
engine = pyttsx3.init() 

# say method on the engine that passing input text to be spoken 
engine.say('Hello Harshit Singh, how may I help you, sir.') 

# run and wait method, it processes the voice commands.  
engine.runAndWait() 
while True:
	print("\n")
	print("---MENU---")
	print("You can choose any of following to open")
	print("1. Chrome")
	print("2. Notepad")
	print("3. Paint")
	print("\n")
	print("Chat with me your requirements:" ,end='')
	x = input()
	#os.system(x)

	if (("run" in x) or ("execute" in x)) and ("chrome" in x):
		os.system("chrome.exe")
	elif (("run" in x) or ("execute" in x)) and (("notepad" in x) or ("editor" in x)):
		os.system("notepad")
	elif (("run" in x) or ("execute" in x)) and ("mspaint" in x):
		os.system("mspaint")
	elif (("quit" in x) or ("exit" in x)):
		break
	else:
		print("Not Supported")