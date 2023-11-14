import tkinter as tk

def go():
    clear()
    match selected_option.get():
        case "decimal (base 10)":
            convert_from_decimal()
        case "binary (base 2)":
            convert_from_binary()
        case "hexadecimal (base 16)":
            convert_from_hexadecimal()
        case "octal (base 8)":
            convert_from_octal()
        case default:
            return 0

def convert_from_decimal():
    user_input = int(user_entry.get())
    entries[0].insert(0, user_input)
    entries[1].insert(0, bin(user_input).replace('0b', ''))
    entries[2].insert(0, hex(user_input).replace('0x', ''))
    entries[3].insert(0, oct(user_input).replace('0o', ''))

def convert_from_binary():
    user_input = user_entry.get()
    decimal_user_input = int(user_input, 2)
    entries[0].insert(0, decimal_user_input)
    entries[1].insert(0, user_input)
    entries[2].insert(0, hex(decimal_user_input).replace('0x', ''))
    entries[3].insert(0, oct(decimal_user_input).replace('0o', ''))

def convert_from_hexadecimal():
    user_input = user_entry.get()
    decimal_user_input = int(user_input, 16)
    entries[0].insert(0, decimal_user_input)
    entries[1].insert(0, bin(decimal_user_input).replace('0b', ''))
    entries[2].insert(0, user_input)
    entries[3].insert(0, oct(decimal_user_input).replace('0o', ''))

def convert_from_octal():
    user_input = user_entry.get()
    decimal_user_input = int(user_input, 8)
    entries[0].insert(0, decimal_user_input)
    entries[1].insert(0, bin(decimal_user_input).replace('0b', ''))
    entries[2].insert(0, hex(decimal_user_input).replace('0x', ''))
    entries[3].insert(0, user_input)

def clear():
    for entry in entries: 
        entry.delete(0, tk.END)

def on_option_selected(event):
    selected_option.set(event)

window = tk.Tk()
window.title("Number System Converter")
window.resizable(False, False)

##############
top_frame = tk.Frame(window, bg="#4831d4")
top_frame.grid(row=0, column=0, sticky="ew")
bottom_frame = tk.Frame(window, bg="#ccf381")
bottom_frame.grid(row=1, column=0)

entries = []
dropdown_options = [
    "decimal (base 10)",
    "binary (base 2)",
    "hexadecimal (base 16)",
    "octal (base 8)"
]

for idx, text in enumerate(["Decimal:", "Binary:", "Hexadecimal:", "Octal:"]):
    label = tk.Label(top_frame, text=text, bg="#ccf381", fg="#4831d4")
    entry = tk.Entry(top_frame, state="normal", font=("Arial", 17))
    entries.append(entry)
    label.grid(row=idx, column=0, padx=10, pady=5, sticky="ew")
    entry.grid(row=idx, column=1, sticky="ew")

lbl_convert = tk.Label(bottom_frame, text="-CONVERT-", bg="#4831d4", fg="#ccf381")
lbl_convert.grid(row=0, column=0, padx=5)

user_entry = tk.Entry(bottom_frame)
user_entry.grid(row=0, column=1, padx=5)

selected_option = tk.StringVar()
selected_option.set(dropdown_options[0])
option_menu = tk.OptionMenu(bottom_frame, selected_option, *dropdown_options, command=on_option_selected)
option_menu.grid(row=0, column=2, padx=5, pady=5)

go_button = tk.Button(bottom_frame, text="GO", command=go, bg="#4831d4", fg="#ccf381", font=("Impact", 12))
go_button.grid(row=0, column=3, padx=5)

window.mainloop()