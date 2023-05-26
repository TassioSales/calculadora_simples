import tkinter as tk

def on_button_click(button_text):
    if button_text == '=':
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, 'Error')
    elif button_text == 'C':
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculadora")

display = tk.Entry(root, width=20, font=('Arial', 20), justify='right')
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        button = tk.Button(root, text=button_text, width=5, height=2, font=('Arial', 15))
        button.grid(row=i+1, column=j)
        button.configure(command=lambda button_text=button_text: on_button_click(button_text))

root.mainloop()
