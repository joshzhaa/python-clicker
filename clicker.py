#replays inputs exactly according to recorder.py text format
import pynput.mouse as pym
import pynput.keyboard as pyk
import time
#import ctypes
#ctypes.windll.shcore.SetProcessDpiAwareness(1)

#LOGFILE_NAME = input('Enter name of input log file: ')
LOGFILE_NAME = 'input.txt'
#INFILE_POSITIONS = input('Enter name of file containing input file positions')

LONG_SLEEP = 300
SHORT_SLEEP = 30
CLICK_DELAY = 0.8
TYPE_DELAY = 0.2

def string_to_button(id):
    if id == 'left_click':
        return pym.Button.left
    elif id == 'right_click':
        return pym.Button.right
    else:
        return 4

#convert strings from log file to pyk.Key types
KEY_DICT = {'alt' : pyk.Key.alt, 'alt_l' : pyk.Key.alt_l, 'alt_r' : pyk.Key.alt_r, 'alt_gr' : pyk.Key.alt_gr, 'backspace' : pyk.Key.backspace, 'caps_lock' : pyk.Key.caps_lock, 'cmd' : pyk.Key.cmd, 'cmd_l' : pyk.Key.cmd_l, 'cmd_r' : pyk.Key.cmd_r, 'ctrl' : pyk.Key.ctrl, 'ctrl_l' : pyk.Key.ctrl_l, 'ctrl_r' : pyk.Key.ctrl_r, 'delete' : pyk.Key.delete, 'down' : pyk.Key.down, 'end' : pyk.Key.end, 'enter' : pyk.Key.enter, 'esc' : pyk.Key.esc,'f1' : pyk.Key.f1, 'f2' : pyk.Key.f2, 'f3' : pyk.Key.f3, 'f4' : pyk.Key.f4, 'f5' : pyk.Key.f5, 'f6' : pyk.Key.f6, 'f7' : pyk.Key.f7, 'f8' : pyk.Key.f8, 'f9' : pyk.Key.f9, 'f10' : pyk.Key.f10, 'f11' : pyk.Key.f11, 'f12' : pyk.Key.f12, 'f13' : pyk.Key.f13, 'f14' : pyk.Key.f14, 'f15' : pyk.Key.f15, 'f16' : pyk.Key.f16, 'f17' : pyk.Key.f17, 'f18' : pyk.Key.f18, 'f19' : pyk.Key.f19, 'f20' : pyk.Key.f20, 'home' : pyk.Key.home, 'left' : pyk.Key.left, 'page_down' : pyk.Key.page_down, 'page_up' : pyk.Key.page_up, 'right' : pyk.Key.right, 'shift' : pyk.Key.shift, 'shift_l' : pyk.Key.shift_l, 'shift_r' : pyk.Key.shift_r, 'space' : pyk.Key.space, 'tab' : pyk.Key.tab, 'up' : pyk.Key.up, 'insert' : pyk.Key.insert, 'menu' : pyk.Key.menu, 'num_lock' : pyk.Key.num_lock, 'pause' : pyk.Key.pause, 'print_screen' : pyk.Key.print_screen, 'scroll_lock' : pyk.Key.scroll_lock}

#return pyk.KeyCode
def parse_char(string):
    return pyk.KeyCode(char = string[1])

#return pyk.Key
def parse_key(string):
    return KEY_DICT[string[4:]]

def click(button):
    mouse.click(button)
    time.sleep(CLICK_DELAY)

def type(string):
    parsed = parse_char(string) if string[0] == '\'' else parse_key(string)
    keyboard.press(parsed)
    keyboard.release(parsed)
    time.sleep(TYPE_DELAY)

mouse = pym.Controller()
keyboard = pyk.Controller()

with open(LOGFILE_NAME) as file:
    for line in file:
        action = line.split()
        if action[0] == 'type':
            type(action[1])
        else:
            mouse.position = (action[1], action[2])
            click(string_to_button(action[0]))
