import PySimpleGUI as sg
from enum import Enum
import base64

sg.theme('DarkAmber')

with open("./images/button_0.png", "rb") as image_file:
    button_0 = base64.b64encode(image_file.read())
with open("./images/button_1.png", "rb") as image_file:
    button_1 = base64.b64encode(image_file.read())
with open("./images/button_2.png", "rb") as image_file:
    button_2 = base64.b64encode(image_file.read())
with open("./images/button_3.png", "rb") as image_file:
    button_3 = base64.b64encode(image_file.read())
with open("./images/button_4.png", "rb") as image_file:
    button_4 = base64.b64encode(image_file.read())
with open("./images/button_5.png", "rb") as image_file:
    button_5 = base64.b64encode(image_file.read())
with open("./images/button_6.png", "rb") as image_file:
    button_6 = base64.b64encode(image_file.read())
with open("./images/button_7.png", "rb") as image_file:
    button_7 = base64.b64encode(image_file.read())
with open("./images/button_8.png", "rb") as image_file:
    button_8 = base64.b64encode(image_file.read())
with open("./images/button_9.png", "rb") as image_file:
    button_9 = base64.b64encode(image_file.read())
with open("./images/button_decimal.png", "rb") as image_file:
    button_decimal = base64.b64encode(image_file.read())
with open("./images/button_divide.png", "rb") as image_file:
    button_divide = base64.b64encode(image_file.read())
with open("./images/button_equals.png", "rb") as image_file:
    button_equals = base64.b64encode(image_file.read())
with open("./images/button_minus.png", "rb") as image_file:
    button_minus = base64.b64encode(image_file.read())
with open("./images/button_multi.png", "rb") as image_file:
    button_multi = base64.b64encode(image_file.read())
with open("./images/button_plus.png", "rb") as image_file:
    button_plus = base64.b64encode(image_file.read())
with open("./images/button_ce.png", "rb") as image_file:
    button_ce = base64.b64encode(image_file.read())
with open("./images/button_ans.png", "rb") as image_file:
    button_ans = base64.b64encode(image_file.read())
with open("./images/button_root.png", "rb") as image_file:
    button_root = base64.b64encode(image_file.read())
with open("./images/button_exp.png", "rb") as image_file:
    button_exp = base64.b64encode(image_file.read())


class Keys(Enum):
    Num_1 = 1
    Num_2 = 2
    Num_3 = 3
    Num_4 = 4
    Num_5 = 5
    Num_6 = 6
    Num_7 = 7
    Num_8 = 8
    Num_9 = 9
    Num_0 = 0

    EQUALS = 11
    CLEAR = 22
    PLUS = 33
    MINUS = 44
    MULT = 55
    DIVIDE = 66
    DEC = 77
    OUTPUT = 88
    ROOT = 99
    EXP = 111
    ANS = 222


BACKGROUND_COLOR = ('#2C2825', '#2C2825')

layout = [
    [
        sg.Text('Laskin', size=(8, 1), font=('Helvetica', 67), justification='right',
                text_color='black', background_color='white', key=Keys.OUTPUT)
    ],
    [
        sg.Button('', image_data=button_ce, button_color=BACKGROUND_COLOR,
                  key=Keys.CLEAR, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_root, button_color=BACKGROUND_COLOR,
                  key=Keys.ROOT, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_exp, button_color=BACKGROUND_COLOR,
                  key=Keys.EXP, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_ans, button_color=BACKGROUND_COLOR,
                  key=Keys.ANS, image_subsample=2, border_width=0)
    ],
    [
        sg.Button('', image_data=button_7, button_color=BACKGROUND_COLOR,
                  key=Keys.Num_7, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_8, button_color=BACKGROUND_COLOR,
                  key=Keys.Num_8, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_9, button_color=BACKGROUND_COLOR,
                  key=Keys.Num_9, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_divide, button_color=BACKGROUND_COLOR,
                  key=Keys.DIVIDE, image_subsample=2, border_width=0)
    ],
    [
        sg.Button('', image_data=button_4, button_color=BACKGROUND_COLOR,
                  key=Keys.Num_4, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_5, button_color=BACKGROUND_COLOR,
                  key=Keys.Num_5, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_6, button_color=BACKGROUND_COLOR,
                  key=Keys.Num_6, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_multi, button_color=BACKGROUND_COLOR,
                  key=Keys.MULT, image_subsample=2, border_width=0)
    ],
    [
        sg.Button('', image_data=button_1, button_color=BACKGROUND_COLOR,
                  key=Keys.Num_1, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_2, button_color=BACKGROUND_COLOR,
                  key=Keys.Num_2, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_3, button_color=BACKGROUND_COLOR,
                  key=Keys.Num_3, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_minus, button_color=BACKGROUND_COLOR,
                  key=Keys.MINUS, image_subsample=2, border_width=0)
    ],
    [
        sg.Button('', image_data=button_equals, button_color=BACKGROUND_COLOR,
                  key=Keys.EQUALS, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_0, button_color=BACKGROUND_COLOR,
                  key=Keys.Num_0, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_decimal, button_color=BACKGROUND_COLOR,
                  key=Keys.DEC, image_subsample=2, border_width=0),
        sg.Button('', image_data=button_plus, button_color=BACKGROUND_COLOR,
                  key=Keys.PLUS, image_subsample=2, border_width=0)
    ],

]


class CalcGui:

    def __init__(self):
        self.window = sg.Window('Laskin', layout, grab_anywhere=True)

    def read_buttons(self):
        event, _ = self.window.read()
        return event

    def update(self, value: str):
        if not isinstance(value, str):
            raise ValueError(f'Output value must be in string format not {str(type(value))}')
        elif len(value) > 8:
            raise ValueError(f'Output must be shorter than 8, not {str(len(value))}')
        else:
            self.window[Keys.OUTPUT].update(value)

    def close(self):
        self.window.close()


# Example
if __name__ == "__main__":
    gui = CalcGui()
    while True:
        event = gui.read_buttons()
        if event in (None, 'Exit'):
            break
        if event == Keys.Num_0:
            gui.update("test")
    gui.close()
