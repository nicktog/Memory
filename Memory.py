# implementation of card game - Memory - Nick Togneri

import simplegui
import random

list1 = range(1,9)
list2 = range(1,9)
card_deck = list1 + list2
x = 0
y = 0
turns = 0
state = 0
# helper function to initialize globals

font_size = 50
font_color = "Yellow"

def new_game():
    global hidden, turns, x, y
    random.shuffle(card_deck)
    hidden = set(range(0,16))
    turns = 0
    x = 0
    y = 0
    label.set_text("Turns = " + str(turns))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, card_1, card_0, hidden, x, y, turns
    
    
    if state == 0:
        card_0 = card_deck[int(pos[0]/50)-1]
        x = int(pos[0]/50)
        if x in hidden:
            hidden.remove(x)
        state = 1
        
    elif state == 1:
        card_1 = card_deck[int(pos[0]/50)-1]
        y = int(pos[0]/50)
        if y in hidden:
            hidden.remove(y)
        state = 2
        turns += 1
        label.set_text("Turns = " + str(turns))

    else:
        if not card_0 == card_1:
            z = int(pos[0]/50)
            if z in hidden:
                hidden.remove(z)
            hidden.add(x)
            hidden.add(y)
            card_0 = card_deck[int(pos[0]/50)-1]
            state = 1
            x = z
        else:
            state = 1
            z = int(pos[0]/50)
            card_0 = card_deck[int(pos[0]/50)-1]
            if z in hidden:
                hidden.remove(z)
            x = z
            
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    # canvas.draw_text(text, point, font_size, font_color)
    global x, y, hidden, turns
    place = 0
    for num in card_deck:
        place += 50
        canvas.draw_text(str(num), (place % 800 + 10, 65), font_size, font_color)
    for card_back in hidden:
        canvas.draw_line([(card_back * 50 % 800) + 25, 0], [(card_back * 50 % 800) + 25, 100], 48, 'Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
label = frame.add_label("Turns = " + str(turns))


# get things rolling
new_game()
frame.start()

