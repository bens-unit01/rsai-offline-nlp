import sys
import aiml
import os 

class AiModule(object):
    '''
    classdocs
    '''
    kernel = None; 

    def respond(self, input):
        return self.kernel.respond(input) 
       
        
    def __init__(self, path):
        os.chdir(path); 
        self.kernel = aiml.Kernel()
        self.kernel.setBotPredicate("name", "RSAI")
        self.kernel.setBotPredicate("favoritecolor", "blue")
        self.kernel.setBotPredicate("city", "Montreal")
        self.kernel.setBotPredicate("country", "Canada")
        self.kernel.setBotPredicate("nationality", "Canadian")
        self.kernel.setBotPredicate("birthplace", "Montreal")
        self.kernel.setBotPredicate("location", "Montreal")

        if os.path.isfile("bot_brain.brn"):
            self.kernel.bootstrap(brainFile = "bot_brain.brn")
        else:
            self.kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
            self.kernel.saveBrain("bot_brain.brn")   
             
            
