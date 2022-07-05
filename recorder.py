#records mouse and keyboard inputs into a standardized text format
import pynput.mouse as pym
import pynput.keyboard as pyk

#returns a string describing the type of click
def button_to_string(button):
    if button == pym.Button.left:
        return 'left_click'
    elif button == pym.Button.right:
        return 'right_click'
    else:
        return 'INVALID_CLICK'

def on_click(x, y, button, pressed):
    if pressed:
        print(button_to_string(button), x, y)

def on_press(key):
    if key == pyk.Key.esc:
        mouse_recorder.stop()
        keyboard_recorder.stop()
    else:
        print('type', key)

with pym.Listener(on_click=on_click) as mouse_recorder, pyk.Listener(on_press=on_press) as keyboard_recorder:
    mouse_recorder.join()
    keyboard_recorder.join()