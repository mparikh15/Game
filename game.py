from sys import exit

#has_key = False

def large_chamber():
    print "As you walk into the large chamber, the doors behind you lock... "
    raw_input(" ")
    print "This is a large, mostly empty room and there are two doors"
    raw_input(" ")
    print "You move to the middle of the room and look to the north and west"
    raw_input(" ")
    print "The door to the north has a large lock on it with an engraving of a"
    print "a winged hippocampus."
    raw_input(" ")
    print "The door to the west is a simple wooden door, but a foul stench lies behind it..."
    raw_input(" ")
    door_choice(False)

def door_choice(key):
    holder = key
    print "You return to the middle of the large chamber"
    raw_input(" ")
    print "What do you choose to do? "
    lcchoice = raw_input("> ")

    if "WEST" in lcchoice:
        spike_chamber()

    elif "NORTH" in lcchoice and not key:
        print "You try to open the door, but it's locked!"
        raw_input(" ")
        print "You look closer at the lock, and it has a winged hippocampus on it."
        raw_input(" ")
        print "There must be a key somewhere in the dungeon..."
        raw_input(" ")
        door_choice(False)

    elif "NORTH" in lcchoice and key:
        gold_room()

    else:
        print "That's not really an option."
        door_choice(key)

def spike_chamber():
    print "You are in a room that is filled with spikes."
    raw_input(" ")
    print "Vague deja vu hits you, you've been here before."
    raw_input(" ")
    print "While you can see that the room is split in two, this side has a direct"
    print "and safe path into the spikes."
    raw_input(" ")
    print "There's a door on the other side that's blocked by the spikes. You suspect it"
    print "leads back to the room where you first woke up. No need to go there again."
    raw_input(" ")
    print "There's a shiny object in the middle of the rusty spikes."
    spike_choice()

def spike_choice():
    print "Do you want to go towards the object?"
    choice = raw_input("> ")

    if "YES" in choice or "Y" in choice:
        print "You walk forward through the spikes. Carefully..."
        raw_input("> ")
        print "You get to the middle of the spikes and look down."
        raw_input("> ")
        print "There's a key. It's very large and heavy, but you pick it up."
        raw_input("> ")
        print "After looking at it,"

        door_choice(True)

    elif "No" in choice or "N" in choice:
        print "You decide not to go towards the object and head back to the previous room."
        door_choice()

    else:
        print "Don't ignore the question, YES or NO??\n"
        spike_choice()


def spike_chamber_front():
    print "You walk into a poorly lit room."
    raw_input(" ")
    print "You realize that there's a huge array of spikes in front of you."
    raw_input(" ")
    print "You look more closely and see something shiny in the middle..."
    raw_input(" ")
    print "Unfortunately it's completely blocked off by spikes and there isn't"
    print "Any good way of getting over to it. Maybe Navi can help?"
    spike_test()


def spike_test():
    print "What do you do?"
    choice = raw_input("> ")

    if "navi" in choice or "NAVI" in choice or "Navi" in choice:
        print "Navi flies over to take a closer look."
        print "She reports back, 'It looks like a key of some sort."
        print "It has a winged seamonster symbol on it."
        print "Unfortunately it's blocked by all of those spikes...'"
        print "Navi doesn't think you'll be able to reach it from this side of the room."
        spike_test()

    elif "BACK" in choice:
        print "You head back."
        first_room()

    elif "SPIKE" in choice or "JUMP" in choice or "look" in choice:
        dead("That was a bad idea. You end up falling on a spike and dying.")

    else:
        print "That's not really an option..."
        spike_test()


def gold_room():
    print "You win!"
    exit(0)

def dead(why):
    print why
    exit(0)

def dark_hallway():
    print "You enter the door on the right and step into a large, dark hallway."
    raw_input(" ")
    print "You take a few steps forward and hear a voice."
    raw_input(" ")
    print "'HALT' shouts the voice."
    raw_input(" ")
    print "Ahead of you you see a frail old man."
    raw_input(" ")
    print "'To progress you must answer this riddle.'"
    raw_input(" ")
    print "It is greater than God; it is more evil than the devil; the poor have it;"
    print "the rich need it; and if you eat it, you will die. What is it?"
    raw_input(" ")
    riddle_one()

def riddle_one():
    print "What do you want to do/guess?"
    guess = raw_input("> ")

    if "NOTHING" in guess:
        print "'Very good! Very good indeed. Says the old man."
        raw_input(" ")
        print "'You may progress. Good luck.'"
        raw_input(" ")
        print "The old man disappears. You look around and cannot find him anwhere."
        raw_input(" ")
        print "You go up to the door at the other end of the chamber and it opens...\n"
        large_chamber()

    elif "BACK" in guess:
        print "You decide this isn't worth your time.\n"
        first_room()

    elif "NAVI" in guess:
        print "'I'm not really sure,' says Navi. 'I can't figure this one out."
        raw_input(" ")
        print "There's not much that the poor have that the rich don't. It's almost opposite.'"
        raw_input(" ")
        print "Navi pauses and thinks, if you can't figure it out, we could always FIGHT him.\n"
        riddle_one()

    elif "FIGHT" in guess:
        print "You yell at the old man and run towards him to fight."
        raw_input(" ")
        print "He laughs a bit under his breath and as you draw close, you realize"
        print "That he's not actually there. You look around, but can't find him."
        raw_input(" ")
        print "You walk forward to the door, but it won't open."
        raw_input(" ")
        print "There's no lock, but seems sealed too tightly..."
        raw_input(" ")
        print "There's no way forward along this path, so you head back.\n"
        first_room()

    else:
        print "Nope, that's not right! The old man laughs.\n"
        riddle_one()


def long_hallway():
    print "Super long hallway, go through all the way to the end..."
    large_chamber()


def start():
    print "Oww... You wake up in a dark room. Your head hurts and you can't remember how you got here."
    raw_input(" ")
    print "You hear a voice, it introduces itself..."
    raw_input(" ")
    print "'Hello old friend', it says. 'My name is Navi and I am here to help.'"
    raw_input(" ")
    print "I'm small and can take a closer look at things you cannot reach."
    raw_input(" ")
    print "To call me, just TYPE NAVI."
    raw_input(" ")
    print "Here, try it, just to see if you can do it right!\n"
    print "Make sure it's all caps!\n"
    test()


def test():
    choice = raw_input("> ")

    if  "NAVI" in choice:
        print "Good, glad we got that out of the way."
        raw_input(" ")
        starting_room()

    else:
        print "Nope, that's not quite right, try again!"
        test()

def starting_room():
    print "You look around this room."
    raw_input(" ")
    print "There are two doors here, one to the left and one to the right."
    raw_input(" ")
    print "In between those two doors is a long wall with seemingly nothing there..."
    raw_input(" ")
    print "Do you want to go through door 1 (left) or door 2 (right)?\n"

    door = int (raw_input("> "))
    if door == 1:
        spike_chamber_front()
    elif door == 2:
        dark_hallway()


def first_room():
    print "You are in the first room again. You notice that the large gap in the middle now has a door in the middle."
    raw_input(" ")
    print "It strikes you as odd. The door wasn't there the first time you were in this room, but it's clearly there now."
    raw_input(" ")
    print "Oh well you have a choice now."
    three_choices()

def three_choices():
    print "Which way do you want to go? LEFT, RIGHT or STRAIGHT."
    door = raw_input("> ")

    if "LEFT" in door:
        spike_chamber_front()
    elif "STRAIGHT" in door:
        long_hallway()
    elif "RIGHT" in door:
        dark_hallway()
    else:
        print "%s is not an option" % (door)
        three_choices()

    #print "Cheat code time for testing!!"
    #choice_2 = raw_input("> ")

        #if choice_2 == 1:
        #    large_chamber()
        #else:
        #    large_chamber()


start()
