import sys;
import os;
from SpeakPythonRecognizer import SpeakPythonRecognizer
from AiModule import AiModule 

def execute(s):
	print s;
	#exec s;

print "init app ..............................."

recog = SpeakPythonRecognizer(execute, "houseCommands");
recog.setDebug(1);
#ai_module = AiModule("./aiml") 
#recog.set_ai(ai_module);   

print "init completed .................................." 
while 1:
    
    recog.recognize();
    print "-------------------------------------";

print "exit from main"; 
