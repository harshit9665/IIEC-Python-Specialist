import pyttsx3
import os
# init function to get an engine instance for the speech synthesis  
engine = pyttsx3.init() 

# say method on the engine that passing input text to be spoken 
engine.say('Hello sir, how may I help you, sir.') 
# run and wait method, it processes the voice commands.  
engine.runAndWait() 
print("\n")
print("Press 1 : To open chrome")
print("Press 2 : To open notepad")
print("Press 3 : To open paint")
print("\n")
print("Enter your choice:" ,end='')
x = input()
#os.system(x)

if int(x) ==1:
	os.system("chrome.exe")
elif int(x)==2:
	os.system("notepad")
elif int(x)==3:
	os.system("mspaint")
else:
	print("Not Supported")