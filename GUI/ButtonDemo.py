from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class buttonDemo(EasyFrame):
    def _init_(self):
        EasyFrame._init_(self, title = "Button Demo")
        self.label = self.addLabel(text = "Hello", row = 0, column = 0, columnspan = 2 , sticky = "NSEW")
        self.clearButton = self.addButton(text = "Clear", row = 1, column = 0, command = self.clear)
        self.restoreButton = self.addButton(text = "Restore", row = 1, column = 1, command = self.restore, state = "disabled")
        def clear(self):
            self.label["text"] = ""
            self.clearButton["state"] = "disabled"
            self.restoreButton["state"] = "normal"
        def restore(self):
            self.label["text"] = "Hello"
            self.clearButton["state"] = "normal"
            self.restoreButton["state"] = "disabled"
        
def main():
    buttonDemo().mainloop()
if __name__ == "__main__":
    main()