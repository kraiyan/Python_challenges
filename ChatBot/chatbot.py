import aiml
import os


kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# Create the kernel and learn AIML files



# Press CTRL-C to break this loop
while True:
		message=raw_input("Enter the message>>")

		if message == "quit":
	    		exit()
		elif message == "save":
	    		kernel.saveBrain("bot_brain.brn")
		else:
	    		print(kernel.respond(message))