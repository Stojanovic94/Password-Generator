import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import random, string

# Global configuration variables
no_of_options = 0
length_value = 7

# Callback functions
def get_slider_value(value):
    global length_value
    length_value = int(value)
    progress_status()

def progress_status():
    global no_of_options, length_value
    no_of_options = (upper_case.get() * 5 +
                     small_case.get() * 5 +
                     special_Chars.get() * 5 +
                     num.get() * 5 +
                     length_value * 5)
    length_progress['value'] = no_of_options
    
    # Change progress bar style based on strength
    if no_of_options < 50:
        length_progress.config(style="Red.Horizontal.TProgressbar")
    elif no_of_options < 80:
        length_progress.config(style="Yellow.Horizontal.TProgressbar")
    else:
        length_progress.config(style="Green.Horizontal.TProgressbar")

def generate_pass():
    global no_of_options, length_value
    switchCode = (str(upper_case.get()) +
                  str(small_case.get()) +
                  str(special_Chars.get()) +
                  str(num.get()))
    
    switcher = {
        '1100': generate1,
        '1101': generate2,
        '0001': generate3,
        '1111': generate4,
        '0100': generate5,
        '1000': generate6,
        '0010': generate7,
        '1001': generate8,
        '0101': generate9,
        '1010': generate10,
        '0110': generate11,
        '1110': generate12,
        '0011': generate13,
        '0111': generate14
    }
        
    password = switcher.get(switchCode, lambda: "Please select at least one checkbox ")()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def generate1():
    "Upper and Smaller"
    try:
        n = int(length_value)
        pool = string.ascii_uppercase + string.ascii_lowercase
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate2():
    "Upper, Smaller, and Number"
    try:
        n = int(length_value)
        pool = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate3():
    "Number"
    try:
        n = int(length_value)
        pool = string.digits
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate4():
    "Upper, Smaller, Number, and Special"
    try:
        n = int(length_value)
        pool = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate5():
    "Smaller"
    try:
        n = int(length_value)
        pool = string.ascii_lowercase
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate6():
    "Upper"
    try:
        n = int(length_value)
        pool = string.ascii_uppercase
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate7():
    "Special"
    try:
        n = int(length_value)
        pool = string.punctuation
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate8():
    "Upper and Number"
    try:
        n = int(length_value)
        pool = string.ascii_uppercase + string.digits
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate9():
    "Smaller and Number"
    try:
        n = int(length_value)
        pool = string.ascii_lowercase + string.digits
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate10():
    "Upper and Special"
    try:
        n = int(length_value)
        pool = string.ascii_uppercase + string.punctuation
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate11():
    "Smaller and Special"
    try:
        n = int(length_value)
        pool = string.ascii_lowercase + string.punctuation
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate12():
    "Upper, Smaller, and Special"
    try:
        n = int(length_value)
        pool = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate13():
    "Number and Special"
    try:
        n = int(length_value)
        pool = string.digits + string.punctuation
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def generate14():
    "Smaller, Number, and Special"
    try:
        n = int(length_value)
        pool = string.digits + string.ascii_lowercase + string.punctuation
        return "".join(random.sample(pool, n))
    except Exception:
        return "Invalid length_value"

def copyclip():
    passwordcopy = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(passwordcopy)
    tkinter.messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x350")
root.configure(bg="white")
root.resizable(False, False)  # Prevent window resizing



# Set ttk style for a modern look
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TButton", font=("Helvetica", 10))
style.configure("TLabel", font=("Helvetica", 10))
style.configure("TCheckbutton", font=("Helvetica", 10))

# Configure progress bar styles for different strength levels
style.configure("Red.Horizontal.TProgressbar", foreground='red', background='red')
style.configure("Yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
style.configure("Green.Horizontal.TProgressbar", foreground='green', background='green')

# Title Label
title_label = tk.Label(root, text="Password Generator", fg="black", bg="white",
                       font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=4, pady=(20, 10))

# Options Frame (Checkbuttons)
options_frame = tk.Frame(root, bg="white")
options_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

upper_case = tk.IntVar()
small_case = tk.IntVar()
num = tk.IntVar()
special_Chars = tk.IntVar()

chk_upper = tk.Checkbutton(options_frame, text="A-Z", variable=upper_case,
                           onvalue=1, offvalue=0, command=progress_status,
                           bg="white", font=("Helvetica", 10))
chk_upper.grid(row=0, column=0, padx=10, pady=5)

chk_small = tk.Checkbutton(options_frame, text="a-z", variable=small_case,
                           onvalue=1, offvalue=0, command=progress_status,
                           bg="white", font=("Helvetica", 10))
chk_small.grid(row=0, column=1, padx=10, pady=5)

chk_num = tk.Checkbutton(options_frame, text="0-9", variable=num,
                         onvalue=1, offvalue=0, command=progress_status,
                         bg="white", font=("Helvetica", 10))
chk_num.grid(row=0, column=2, padx=10, pady=5)

chk_special = tk.Checkbutton(options_frame, text="Special Characters",
                             variable=special_Chars, onvalue=1, offvalue=0,
                             command=progress_status, bg="white", font=("Helvetica", 10))
chk_special.grid(row=0, column=3, padx=10, pady=5)

# Slider Frame
slider_frame = tk.Frame(root, bg="white")
slider_frame.grid(row=2, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

slider_label = tk.Label(slider_frame, text="Length:", bg="white", font=("Helvetica", 10))
slider_label.grid(row=0, column=0, padx=10)
length_var = tk.IntVar(value=7)
s1 = tk.Scale(slider_frame, variable=length_var, from_=7, to=16, orient=tk.HORIZONTAL,
              command=get_slider_value, bg="white")
s1.grid(row=0, column=1, padx=10)

# Strength Label and Progressbar
strength_label = tk.Label(root, text="Password Strength", bg="white",
                          font=("Helvetica", 12, "bold"))
strength_label.grid(row=3, column=0, columnspan=4, pady=(10, 0))

length_progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=400, mode='determinate')
length_progress.grid(row=4, column=0, columnspan=4, pady=(5, 10))

# Output Frame (Generate Button, Entry, and Copy Button)
output_frame = tk.Frame(root, bg="white")
output_frame.grid(row=5, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

btn_generate = ttk.Button(output_frame, text="Generate", command=generate_pass)
btn_generate.grid(row=0, column=0, padx=10, pady=5)

password_entry = tk.Entry(output_frame, width=30, font=("Helvetica", 10))
password_entry.grid(row=0, column=1, padx=10, pady=5)

btn_copy = ttk.Button(output_frame, text="Copy", command=copyclip)
btn_copy.grid(row=0, column=2, padx=10, pady=5)

root.mainloop()








