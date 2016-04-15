
# Main file where story should be based.

from random import randint
from time import sleep
import city
import dune
import ghetto

   # #
   # #    ####  #####  ###### ###### ##### # #    #  ####
 ####### #    # #    # #      #        #   # ##   # #    #
   # #   #      #    # #####  #####    #   # # #  # #
 ####### #  ### #####  #      #        #   # #  # # #  ###
   # #   #    # #   #  #      #        #   # #   ## #    #
   # #    ####  #    # ###### ######   #   # #    #  ####

greetings = [
"Hello. Come here often? Just kidding, what's your name?",
"Wassup, homie. Whats yo name, dawg?",
"FAM!",
"Give name pls"]

def greeting():
    print greetings[randint(0,3)]
    username = raw_input('> ')
    print "Nice to meet you, %s" % username
    sleep(1)
    print 'Now not to alarm you or anything, this game is very bs and you better not get triggered. This is the only warning.'
    sleep(1)
    print 'also im bad at programming so if you quit this terminal you lose everything. its a better version of permadeath <3'
    sleep(1)
    spawn()

   # #
   # #    ####  #####    ##   #    # #    #
 ####### #      #    #  #  #  #    # ##   #
   # #    ####  #    # #    # #    # # #  #
 #######      # #####  ###### # ## # #  # #
   # #   #    # #      #    # ##  ## #   ##
   # #    ####  #      #    # #    # #    #

inventory = []
    #Figure out how to make random spawns work
    #spawns = [dune,city,ghetto]
    #spawns[randint(0,2)].main()

def spawn():
    print "Pick a number between 1 and 3"
    spawnChoice = raw_input('> ')
    if spawnChoice == 1:
        dune.main()
    if spawnChoice == 2:
        city.main()
    if spawnChoice == 3:
        ghetto.main()
    else:
        "That's not how it works."
        sleep(1)
        spawn()

greeting()
