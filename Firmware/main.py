print("Booting up...")
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP3,board.GP4,board.GP2,board.GP1)
keyboard.row_pins = (board.GP26,board.GP27,board.GP28)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# Currently, these are placeholders as I want to get my hands on thee complete PCB and to bee able to test it.
# Swwitch Ids:
# SW SW SW SW SW RE
# 1  2  3  4  9  10
# SW SW SW SW SW SW
# 5  6  7  8  11 12
# 
# 1-8   : Normal keys <-> Macro keys
# 11-12 : Left/Right keys for changing key bind sets
# 9     : Enter key to change bind sets
# 10    : Volume/Brightness control, usage might change depeending on program
#
keyboard.keymap = [
    [KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y],
    [KC.A,KC.S,KC.D,KC.F,KC.G,KC.H],
]

bind_sets = [
    {
        "name"      : "Basic Keys",
        "keymap"    : [    
                [KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y],
                [KC.A,KC.S,KC.D,KC.F,KC.G,KC.H],
            ],
        
    },

    {
        "name"      : "Krita Macros",
        "keymap"    : [    
                [KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y],
                [KC.A,KC.S,KC.D,KC.F,KC.G,KC.H],
            ],
        
    },
]




if __name__ == '__main__':
    keyboard.go()
