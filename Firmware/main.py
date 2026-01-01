print("Booting up...")
import board, busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.holdtap import HoldTap
from kmk.extensions.display import Display, TextEntry, ImageEntry

# For SSD1306
from kmk.extensions.display.ssd1306 import SSD1306

# Replace SCL and SDA according to your hardware configuration.
i2c_bus = busio.I2C(board.D5, board.D4)
driver = SSD1306(
    # Mandatory:
    i2c=i2c_bus,
    # Optional:
    device_address=0x3C,
)

keyboard = KMKKeyboard()
keyboard.col_pins = (board.D10,board.D9,board.D8,board.D7)
keyboard.row_pins = (board.D1, board.D2,board.D3)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

holdtap = HoldTap()
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    # regular direction encoder and a button
    (board.D4 , board.D7, None), # encoder #1 
)
layers = Layers()
keyboard.modules.extend([layers, holdtap, encoder_handler])



display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='Layer: ', x=0, y=32, y_anchor='B'),
        TextEntry(text='BASE', x=40, y=32, y_anchor='B', layer=0),
        TextEntry(text='RAISE', x=40, y=32, y_anchor='B', layer=1),
        TextEntry(text='LOWER', x=40, y=32, y_anchor='B', layer=2),
        TextEntry(text='0 1 2', x=0, y=4),
        TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
        TextEntry(text='1', x=12, y=4, inverted=True, layer=1),
        TextEntry(text='2', x=24, y=4, inverted=True, layer=2),
    ],
    # Optional width argument. Default is 128.
    # width=128,
    # height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)

keyboard.extensions.extend([MediaKeys(),display])

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
