import sys
import aiml
import os 

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    print "App started ..."
    
    # Create the kernel and learn AIML files
    os.chdir("aiml"); 
    kernel = aiml.Kernel()
    #kernel.learn("std-startup.xml")
    #kernel.respond("load aiml b")
    if os.path.isfile("bot_brain.brn"):
        kernel.bootstrap(brainFile = "bot_brain.brn")
    else:
        kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
        kernel.saveBrain("bot_brain.brn")
    # Press CTRL-C to break this loop
    while True:
        print kernel.respond(raw_input("Enter your message >> "))

if __name__ == "__main__":
    main()

