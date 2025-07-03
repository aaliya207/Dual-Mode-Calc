import tkinter as tk

# --- Themes ---
themes = {
    "light": {
        "bg": "#fff0f6",
        "display_bg": "#ffe4f1",
        "fg": "#5d2d50",
        "button": {
            "AC": "#ffb3c6",
            "C": "#ffc2d1",
            "%": "#ff99ac",
            "/": "#ff66a3",
            "*": "#ff66a3",
            "-": "#ff66a3",
            "+": "#ff66a3",
            "=": "#ff85a2",
            "num": "#ffd0e1",  # <--- changed from #fff0f6 to a slightly deeper pink
            "dark_toggle": "#ffb3c6"
        }
    },
    "dark": {
        "bg": "#2f1f3b",
        "display_bg": "#3a264f",
        "fg": "#fce4ff",
        "button": {
            "AC": "#ce4b7e",
            "C": "#c85c9e",
            "%": "#9c3587",
            "/": "#aa4ac7",
            "*": "#aa4ac7",
            "-": "#aa4ac7",
            "+": "#aa4ac7",
            "=": "#f77fb0",
            "num": "#51345f",
            "dark_toggle": "#ce4b7e"
        }
    }
}

# --- Functions ---
def button_click(value):
    current = display_var.get()
    if current == "Error":
        current = ""
    display_var.set(current + value)

def clear():
    current = display_var.get()
    display_var.set(current[:-1])

def all_clear():
    display_var.set("")

def calculate():
    try:
        result = str(eval(display_var.get()))
        display_var.set(result)
    except:
        display_var.set("Error")

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme()

def apply_theme():
    theme = themes[current_theme]
    root.configure(bg=theme["bg"])
    display.configure(bg=theme["display_bg"], fg=theme["fg"])
    for (btn, meta) in buttons:
        key = meta.get("type")
        btn.configure(bg=theme["button"][key], fg=theme["fg"], activebackground=theme["button"][key])

# --- Main Window ---
root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")
current_theme = "light"

# --- Display ---
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 24), bd=10, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10, sticky="nsew")

# --- Buttons ---
btn_defs = [
    ("AC", all_clear, "AC"), ("C", clear, "C"), ("%", lambda: button_click('%'), "%"), ("Dark", toggle_theme, "dark_toggle"),
    ("7", lambda: button_click('7'), "num"), ("8", lambda: button_click('8'), "num"), ("9", lambda: button_click('9'), "num"), ("/", lambda: button_click('/'), "/"),
    ("4", lambda: button_click('4'), "num"), ("5", lambda: button_click('5'), "num"), ("6", lambda: button_click('6'), "num"), ("*", lambda: button_click('*'), "*"),
    ("1", lambda: button_click('1'), "num"), ("2", lambda: button_click('2'), "num"), ("3", lambda: button_click('3'), "num"), ("-", lambda: button_click('-'), "-"),
    ("0", lambda: button_click('0'), "num"), (".", lambda: button_click('.'), "num"), ("=", calculate, "="), ("+", lambda: button_click('+'), "+")
]

buttons = []
row = 1
col = 0
for (text, cmd, btype) in btn_defs:
    btn = tk.Button(root, text=text, command=cmd, width=5, height=2, font=("Arial", 18), bd=0)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    buttons.append((btn, {"type": btype}))
    col += 1
    if col > 3:
        col = 0
        row += 1

# Make buttons resize
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

apply_theme()
root.mainloop()
