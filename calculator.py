import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()
        self.configure_grid()

    def create_widgets(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(expand=True, fill='both')

        input_field = tk.Entry(input_frame, font=('Arial', 24), textvariable=self.input_text, justify='right')
        input_field.pack(expand=True, fill='both')

        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill='both')

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row_index, row in enumerate(buttons):
            for col_index, char in enumerate(row):
                btn = tk.Button(button_frame, text=char, font=('Arial', 18), command=lambda ch=char: self.on_button_click(ch))
                btn.grid(row=row_index, column=col_index, sticky='nsew')

        # Make grid responsive
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)
            button_frame.rowconfigure(i, weight=1)

    def configure_grid(self):
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=4)
        self.root.columnconfigure(0, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += str(char)
        self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")  # Initial size
    Calculator(root)
    root.mainloop()
