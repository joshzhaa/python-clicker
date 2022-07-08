#records mouse and keyboard inputs into a standardized text format
import pynput.mouse as pym
import pynput.keyboard as pyk

#quit key: pyk.Key.esc
#special action key: pyk.Key.insert
#comment key: pyk.Key.alt_gr

#returns a string describing the type of click
def button_to_string(button):
    match button:
        case pym.Button.left:
            return 'left_click'
        case pym.Button.middle:
            return 'middle_click'
        case pym.Button.right:
            return 'right_click'
        case _:
            return 'INVALID_CLICK'

def insert_text(key):
    global typing_flag
    match key:
        case pyk.Key.enter:
            print('')
            typing_flag = False
        case pyk.Key.space:
            print(' ', end = '')
        case pyk.Key.shift:
            pass
        case _:
            print(key.char, end = '')

def on_click(x, y, button, pressed):
    if pressed:
        print(button_to_string(button), x, y)

typing_flag = False

def on_press(key):
    global typing_flag
    match key:
        case pyk.Key.esc:
            mouse_recorder.stop()
            keyboard_recorder.stop()
        case pyk.Key.insert:
            print('special_action ', end = '')
            typing_flag = True
        case pyk.Key.alt_gr:
            print('COMMENT ', end='')
            typing_flag = True
        case _:
            if typing_flag:
                insert_text(key)
            else:
                print('type', key)

with pym.Listener(on_click=on_click) as mouse_recorder, pyk.Listener(on_press=on_press) as keyboard_recorder:
    mouse_recorder.join()
    keyboard_recorder.join()