print("Booting up...")
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.holdtap import HoldTap
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData

keyboard = KMKKeyboard()
keyboard.col_pins = (board.GP3,board.GP4,board.GP2,board.GP1)
keyboard.row_pins = (board.GP26,board.GP27,board.GP28)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

holdtap = HoldTap()
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP29 , board.GP0, None), # encoder #1 
)
layers = Layers()
keyboard.modules.extend([layers, holdtap, encoder_handler])


oled = Oled(
    OledData(
        corner_one={
            0: OledReactionType.STATIC,
            1: ["Layer"],
        },
        corner_two={
            0: OledReactionType.LAYER,
            1: ["0", "1", "2"],
        },
        corner_three={
            0: OledReactionType.LAYER,
            1: ["BASE", "RAISE", "LOWER"],
        },
        corner_four={
            0: OledReactionType.LAYER,
            1: ["qwerty", "nums", "sym"],
        },
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=True,
    # oHeight=64,
)

keyboard.extensions.extend([MediaKeys(),oled])

# Key aliases
xxxxxxx = KC.NO
_______ = KC.TRNS

# Currently, these are placeholders as I want to get my hands on thee complete PCB and to bee able to test it.
# Switch Ids:
# SW SW SW SW SW RE
# 1  2  3  4  9  10
# SW SW SW SW SW SW
# 5  6  7  8  11 12
# 
# 1-8   : Normal keys <-> Macro keys
# 11-12 : Left/Right keys for changing key bind sets
# 9     : Enter key to change bind sets
# 10    : Volume/Brightness control, usage might change depending on program
#
keyboard.keymap = [
    # 1         | 2         | 3         | 4         | 9         | 10        |
    # 5         | 6         | 7         | 8         | 11        | 12        |

    # Base Layer : QWERTY
    [ 
        KC.Q,       KC.W,         KC.E,       KC.R,     KC.T,    KC.ESC,\
        KC.A,       KC.S,         KC.D,       KC.F,     KC.G,    KC.ENTER
    
    ],

    # 

    [ 
        KC.C,       KC.V,         KC.X,       KC.D,     KC.T,    _______,\
        KC.S,       KC.Z,         KC.Y,       KC.Q,     KC.W,    _______
    
    ],
]

selected_layer = 0

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

def la_prev()->None:
    selected_layer= clamp(selected_layer - 1, 0, len(keyboard.keymap)-1)
    KC.TO(selected_layer)

def la_next()->None:
    selected_layer = clamp(selected_layer + 1, 0, len(keyboard.keymap)-1)
    KC.TO(selected_layer)






if __name__ == '__main__':
    keyboard.go()
