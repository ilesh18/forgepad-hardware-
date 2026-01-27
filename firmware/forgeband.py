import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
hackpad = KMKKeyboard()
macro_module = Macros()
hackpad.modules.append(macro_module)

key_pins = [
    board.GP26,  
    board.GP27,  
    board.GP28,  
    board.GP29, 
    board.GP6,   
    board.GP7,   
    board.GP0,  
    board.GP1,  
    board.GP2,  
]

hackpad.matrix = KeysScanner(
    pins=key_pins,
    value_when_pressed=False, 
)

hackpad.keymap = [
    [
        KC.MACRO("Hello"),                 
        KC.DELETE,                            
        KC.ENTER,                             

        KC.MACRO(                              # Ctrl + S
            Press(KC.LCTRL),
            Tap(KC.S),
            Release(KC.LCTRL),
        ),

        KC.MACRO(                              #  Ctrl + C
            Press(KC.LCTRL),
            Tap(KC.C),
            Release(KC.LCTRL),
        ),

        KC.MACRO(                              # Ctrl + V
            Press(KC.LCTRL),
            Tap(KC.V),
            Release(KC.LCTRL),
        ),

        KC.UP,                                
        KC.DOWN,                               
        KC.ESC,                              
    ]
]

if __name__ == "__main__":
    hackpad.go()
