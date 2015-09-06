#!/usr/bin/python

import sys
import aiml
import commands
 
k = aiml.Kernel()
 
# load the aiml file
k.learn("aiml-other/eliza.aiml")
 
# set a constant
k.setBotPredicate("name", "Chatty")
 
while True:
    input = raw_input("> ")
    if input == "quit":
        sys.exit(0)
    response = k.respond(input)
    # print out on the shell
    print response
    # and as speech
    # print commands.getoutput("/usr/bin/espeak -v en+f4 -p 99 -s 160 \"" + response + "\"")
