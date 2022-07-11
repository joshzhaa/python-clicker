Usage:
    1. record clicks and typed input with recorder.py: python recorder.py > log.txt, press esc to end recorder
        - format: {left_click | middle_click | right_click} {x} {y} or {type} {char}
        - esc to exit, ins then type then hit enter for a special_action, alt_gr then type then hit enter for comment
    2. replay inputs with clicker.py
        - special actions: special_action {name of special action} *args

Notes:
    1. records key types and mouse buttons
    2. available special actions: double_click, short_sleep, long_sleep
