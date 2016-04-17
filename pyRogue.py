
# Main file where story should be based.

from sys import exit
from random import randint
from time import sleep

class room(object):
    def enter(self):
        print "This room is not yet configured. Subclass it and implement enter()"
        exit()

class engine(object):
    def __init__(self, roomMap):
        self.roomMap = roomMap

    def play(self):
        currentRoom = self.roomMap.spawn()
        lastRoom = self.roomMap.nextRoom(finished)

        while currentRoom != lastRoom:
            nextRoomName = currentRoom.enter()
            currentRoom = self.roomMap.nextRoom(nextRoomName)

        currentRoom.enter()

   # #
   # #   #####   ####   ####  #    #  ####
 ####### #    # #    # #    # ##  ## #
   # #   #    # #    # #    # # ## #  ####
 ####### #####  #    # #    # #    #      #
   # #   #   #  #    # #    # #    # #    #
   # #   #    #  ####   ####  #    #  ####

class death(room):
    def enter(self):
        print 'You died. Try again?'
        exit(1)

class finished(room):
    def enter(self):
        print "Congratulations, you finished the game."

class bedroom(room):
    def enter(self):
        print "You are in your room."

class kitchen(room):
    def enter(self):
        print 'You walk into the kitchen.'

class street(room):
    def enter(self):
        print 'You walk out onto the street.'

class school(room):
    def enter(self):
        print 'You walk into your classroom.'

   # #
   # #   #    #   ##   #####
 ####### ##  ##  #  #  #    #
   # #   # ## # #    # #    #
 ####### #    # ###### #####
   # #   #    # #    # #
   # #   #    # #    # #

class map(object):

    rooms = {
    'bedroom': bedroom(),
    'kitchen': kitchen(),
    'street': street(),
    'school': school(),
    'finished': finished()
    }

    def __init__(self, startRoom):
        self.startRoom = startRoom

    def nextRoom(self, roomName):
        v = map.scenes.get(roomName)
        return v

    def spawn(self):
        return self.nextRoom(self.startRoom)

theMap = map('bedroom')
theGame = engine(theMap) #you just lost the game
theGame.play
