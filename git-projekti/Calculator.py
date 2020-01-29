import calc_modules
from Gui import CalcGui, Keys



class Calculator:

    def __init__(self):
        self.gui = CalcGui()
        self.ans = None
        self.value = 0
        self.screen = "0"
        self.lastOp = None
        
        self.gui.update(self.screen)

    def run(self):
        while True:
            event = self.gui.read_buttons()
            if event in (None, 'Exit'):
                break
            if event == Keys.Num_0:
                if self.screen != '0':
                    self.screen += '0'
            if event == Keys.Num_1:
                if self.screen == '0':
                    self.screen = '1'
                else:
                    self.screen += '1'
            if event == Keys.Num_2:
                if self.screen == '0':
                    self.screen = '2'
                else:
                    self.screen += '2'
            if event == Keys.Num_3:
                if self.screen == '0':
                    self.screen = '3'
                else:
                    self.screen += '3'
            if event == Keys.Num_4:
                if self.screen == '0':
                    self.screen = '4'
                else:
                    self.screen += '4'
            if event == Keys.Num_5:
                if self.screen == '0':
                    self.screen = '5'
                else:
                    self.screen += '5'
            if event == Keys.Num_6:
                if self.screen == '0':
                    self.screen = '6'
                else:
                    self.screen += '6'
            if event == Keys.Num_7:
                if self.screen == '0':
                    self.screen = '7'
                else:
                    self.screen += '7'
            if event == Keys.Num_8:
                if self.screen == '0':
                    self.screen = '8'
                else:
                    self.screen += '8'
            if event == Keys.Num_9:
                if self.screen == '0':
                    self.screen = '9'
                else:
                    self.screen += '9'
            if event == Keys.DEC:
                self.screen += '.'


            if event == Keys.EQUALS:
                if self.value != None and self.lastOp != None:
                    tmp = float(self.screen)
                    self.value = self.lastOp(self.value, tmp)
                    self.screen = str(self.value)
                

            if event == Keys.CLEAR:
                self.value = 0
                self.screen = "0"
                self.lastOp = None

            if event == Keys.PLUS:
                if self.value != None and self.lastOp != None:
                    tmp = float(self.screen)
                    self.value = self.lastOp(self.value, tmp)
                self.lastOp = calc_modules.plus
                self.value = float(self.screen)
                self.screen = "0"

            if event == Keys.MINUS:
                if self.value != None and self.lastOp != None:
                    tmp = float(self.screen)
                    self.value = self.lastOp(self.value, tmp)
                self.lastOp = calc_modules.minus
                self.value = float(self.screen)
                self.screen = "0"

            if event == Keys.MULT:
                if self.value != None and self.lastOp != None:
                    tmp = float(self.screen)
                    self.value = self.lastOp(self.value, tmp)
                self.lastOp = calc_modules.multiply
                self.value = float(self.screen)
                self.screen = "0"

            if event == Keys.DIVIDE:
                if self.value != None and self.lastOp != None:
                    tmp = float(self.screen)
                    self.value = self.lastOp(self.value, tmp)
                self.lastOp = calc_modules.divide
                self.value = float(self.screen)
                self.screen = "0"

            if event == Keys.ROOT:
                if self.value != None and self.lastOp != None:
                    tmp = float(self.screen)
                    self.value = self.lastOp(self.value, tmp)
                self.lastOp = calc_modules.root
                self.value = float(self.screen)
                self.screen = "0"

            if event == Keys.EXP:
                if self.value != None and self.lastOp != None:
                    tmp = float(self.screen)
                    self.value = self.lastOp(self.value, tmp)
                self.lastOp = calc_modules.exponent
                self.value = float(self.screen)
                self.screen = "0"

            if event == Keys.ANS:
                if self.ans != None:
                    self.screen = str(self.ans)
                    self.ans = None
                else:
                    self.ans = float(self.screen)
                    self.screen = '0'


            try:
                self.gui.update(self.screen)
            except ValueError:
                self.gui.update("Err")
                self.screen = "0"

    def __del__(self):
        self.gui.close()

# example
if __name__ == "__main__":
    calc = Calculator()
    calc.run()