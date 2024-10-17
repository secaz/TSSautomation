import tkinter as tk
import pyautogui
import time
import pyperclip  # For clipboard handling
import os
import sys

def restart_program():
    """Restart the application."""
    root.destroy()  # Close the current window
    os.execl(sys.executable, sys.executable, *sys.argv)  # Restart the program

def automate_text(text_to_paste, repeat_count, additional_actions=None):
    """Automate pasting of text and execute additional actions if specified."""
    result_label.config(text="You have 3 seconds to switch to the application.")
    root.update()
    time.sleep(3)

    pyperclip.copy(text_to_paste)

    for _ in range(repeat_count):
        pyautogui.click()  # Click the left mouse button
        pyautogui.hotkey('ctrl', 'v')  # Paste the clipboard content
        if additional_actions:
            for action in additional_actions:
                action()  # Execute any additional actions (like pressing enter)
        pyautogui.hotkey('shift', 'tab')  # Switch tabs
        time.sleep(0.2)  # Optional small delay between iterations for stability

    result_label.config(text="Automation completed.")

def automate_label_invoice():
    """Handle label/invoice automation."""
    result_label.config(text="You have 3 seconds to switch to the application.")
    root.update()
    time.sleep(3)
    
    user_input = entry_input.get()  # Get the text from the input field
    try:
        repeat_count = int(entry_count.get())
        if repeat_count <= 0:
            raise ValueError("Please enter a positive number.")
    except ValueError as e:
        result_label.config(text=f"Error: {str(e)}")
        return

    automate_text(user_input, repeat_count)

def automate_boxes():
    """Handle boxes automation."""
    result_label_boxes.config(text="You have 3 seconds to switch to the application.")
    root.update()
    time.sleep(3)

    selected_box_type = box_type_var.get()  # Get the selected box type from radio buttons
    box_texts = {
        "box": "box",
        "pounds": "pounds",
        "nirem": "NIREM",
        "niaid": "NIAID"
    }

    text_to_paste = box_texts.get(selected_box_type)
    
    if not text_to_paste:
        result_label_boxes.config(text="Error: No selection made.")
        return

    try:
        repeat_count = int(entry_count_boxes.get())
        if repeat_count <= 0:
            raise ValueError("Please enter a positive number.")
    except ValueError as e:
        result_label_boxes.config(text=f"Error: {str(e)}")
        return

    for _ in range(repeat_count):
        pyautogui.click()
        pyperclip.copy(text_to_paste)  
        pyautogui.hotkey('ctrl', 'v')  
        time.sleep(1)  
        pyautogui.press('enter')  
        pyautogui.hotkey('shift', 'tab')

    result_label_boxes.config(text="Automation completed.")

def automate_save_and_switch():
    """Handle save and switch automation."""
    try:
        repeat_count = int(entry_count_save.get())
        if repeat_count <= 0:
            raise ValueError("Please enter a positive number.")
    except ValueError as e:
        result_label_save.config(text=f"Error: {str(e)}")
        return

    additional_actions = [lambda: time.sleep(0.2), pyautogui.hotkey('ctrl', 's')]
    automate_text("", repeat_count, additional_actions)  

def validate_inputs():
    """Validate inputs and enable/disable the start button accordingly."""
    user_input = entry_input.get().strip()
    repeat_count_text = entry_count.get().strip()
    if user_input and repeat_count_text.isdigit() and int(repeat_count_text) > 0:
        start_button_label_invoice.config(state=tk.NORMAL)
    else:
        start_button_label_invoice.config(state=tk.DISABLED)

def validate_boxes_inputs():
    """Validate inputs for the boxes frame."""
    repeat_count_text = entry_count_boxes.get().strip()
    if repeat_count_text.isdigit() and int(repeat_count_text) > 0:
        start_button_boxes.config(state=tk.NORMAL)
    else:
        start_button_boxes.config(state=tk.DISABLED)

def validate_save_inputs():
    """Validate inputs for the save frame."""
    repeat_count_text = entry_count_save.get().strip()
    if repeat_count_text.isdigit() and int(repeat_count_text) > 0:
        start_button_save.config(state=tk.NORMAL)
    else:
        start_button_save.config(state=tk.DISABLED)

# Function to show frames
def show_frame(frame):
    """Show the specified frame and hide the main menu frame."""
    label_invoice_frame.pack_forget()
    boxes_frame.pack_forget()
    save_and_switch_frame.pack_forget()
    main_menu_frame.pack_forget()
    
    frame.pack(fill=tk.BOTH, expand=True)

# Create the main window
root = tk.Tk()
root.title("TSS Automation")
root.geometry("450x600")
root.configure(bg="#F0F8FF")

# Create the main menu frame
main_menu_frame = tk.Frame(root, bg="#F0F8FF")

# Add a title label at the top
title_label = tk.Label(main_menu_frame, text="TSS AUTOMATION", font=("Arial", 22, "bold"), fg="#007B7F", bg="#F0F8FF")
title_label.pack(pady=(0, 20))

# Add buttons for Automations on the main screen
button_label_invoice = tk.Button(main_menu_frame, text="📄 Label/Invoice", width=20, command=lambda: show_frame(label_invoice_frame), bg="#2AB0FF", font=("Arial", 12), relief="raised", activebackground="#007B7F", fg="white")
button_label_invoice.pack(pady=(10, 5))

button_boxes = tk.Button(main_menu_frame, text="📦 Boxes", width=20, command=lambda: show_frame(boxes_frame), bg="#2AB0FF", font=("Arial", 12), relief="raised", activebackground="#007B7F", fg="white")
button_boxes.pack(pady=(10, 5))

button_save_switch = tk.Button(main_menu_frame, text="💾 Save", width=20, command=lambda: show_frame(save_and_switch_frame), bg="#2AB0FF", font=("Arial", 12), relief="raised", activebackground="#007B7F", fg="white")
button_save_switch.pack(pady=(10, 5))

# Create and place the restart button at the bottom left
restart_button = tk.Button(root, text="Restart", command=restart_program, bg="#FF6F61", font=("Arial", 10, "bold"), fg="white", relief="raised")
restart_button.pack(side=tk.BOTTOM, anchor='sw', padx=10, pady=10)

main_menu_frame.pack(fill=tk.BOTH, expand=True)

# Create a frame for the label/invoice automation
label_invoice_frame = tk.Frame(root, bg="#F0F8FF")

# Add a home button to the label/invoice frame in the top left corner
home_button_label_invoice = tk.Button(label_invoice_frame, text="🏠 HOME", command=lambda: show_frame(main_menu_frame),
                                       bg="#2AB0FF", font=("Arial", 10), relief="flat", fg="white")
home_button_label_invoice.pack(side=tk.TOP, anchor='nw', padx=5, pady=5)

# Create and place the input fields for label/invoice automation
tk.Label(label_invoice_frame, text="Enter text to paste:", bg="#F0F8FF", font=("Arial", 12, "bold")).pack(pady=5)
entry_input = tk.Entry(label_invoice_frame, width=40, font=("Arial", 12))
entry_input.pack(pady=5)

tk.Label(label_invoice_frame, text="How many times to repeat:", bg="#F0F8FF", font=("Arial", 12, "bold")).pack(pady=5)
entry_count = tk.Entry(label_invoice_frame, width=10, font=("Arial", 12))
entry_count.pack(pady=5)

# Create and place the button to start the automation (initially disabled)
start_button_label_invoice = tk.Button(label_invoice_frame, text="🔄 Start Automation", command=automate_label_invoice, state=tk.DISABLED, bg="#A9A9A9", font=("Arial", 12), relief="flat")
start_button_label_invoice.pack(pady=20)

# Label to show results
result_label = tk.Label(label_invoice_frame, text="", bg="#F0F8FF", font=("Arial", 12))
result_label.pack(pady=5)

# Bind the validation function to the entry fields
entry_input.bind("<KeyRelease>", lambda event: validate_inputs())
entry_count.bind("<KeyRelease>", lambda event: validate_inputs())

# Create a frame for boxes automation
boxes_frame = tk.Frame(root, bg="#F0F8FF")

# Add a home button to the boxes frame in the top left corner
home_button_boxes = tk.Button(boxes_frame, text="🏠 HOME", command=lambda: show_frame(main_menu_frame),
                               bg="#2AB0FF", font=("Arial", 10), relief="flat", fg="white")
home_button_boxes.pack(side=tk.TOP, anchor='nw', padx=5, pady=5)

# Add radio buttons for package type selection
box_type_var = tk.StringVar(value="box")
tk.Label(boxes_frame, text="Select Type:", bg="#F0F8FF", font=("Arial", 12, "bold")).pack(pady=5)

for box_type in ["box", "pounds", "nirem", "niaid"]:
    tk.Radiobutton(boxes_frame, text=box_type, variable=box_type_var, value=box_type, bg="#F0F8FF", font=("Arial", 12)).pack(anchor='w', padx=10)

tk.Label(boxes_frame, text="How many times to repeat:", bg="#F0F8FF", font=("Arial", 12, "bold")).pack(pady=5)
entry_count_boxes = tk.Entry(boxes_frame, width=10, font=("Arial", 12))
entry_count_boxes.pack(pady=5)

# Create and place the button to start the boxes automation (initially disabled)
start_button_boxes = tk.Button(boxes_frame, text="🔄 Start Automation", command=automate_boxes, state=tk.DISABLED, bg="#A9A9A9", font=("Arial", 12), relief="flat")
start_button_boxes.pack(pady=20)

# Label to show results
result_label_boxes = tk.Label(boxes_frame, text="", bg="#F0F8FF", font=("Arial", 12))
result_label_boxes.pack(pady=5)

# Bind the validation function to the entry fields
entry_count_boxes.bind("<KeyRelease>", lambda event: validate_boxes_inputs())

# Create a frame for the save and switch automation
save_and_switch_frame = tk.Frame(root, bg="#F0F8FF")

# Add a home button to the save and switch frame in the top left corner
home_button_save = tk.Button(save_and_switch_frame, text="🏠 HOME", command=lambda: show_frame(main_menu_frame),
                              bg="#2AB0FF", font=("Arial", 10), relief="flat", fg="white")
home_button_save.pack(side=tk.TOP, anchor='nw', padx=5, pady=5)

tk.Label(save_and_switch_frame, text="How many times to repeat:", bg="#F0F8FF", font=("Arial", 12, "bold")).pack(pady=5)
entry_count_save = tk.Entry(save_and_switch_frame, width=10, font=("Arial", 12))
entry_count_save.pack(pady=5)

# Create and place the button to start the save and switch automation (initially disabled)
start_button_save = tk.Button(save_and_switch_frame, text="🔄 Start Automation", command=automate_save_and_switch, state=tk.DISABLED, bg="#A9A9A9", font=("Arial", 12), relief="flat")
start_button_save.pack(pady=20)

# Label to show results
result_label_save = tk.Label(save_and_switch_frame, text="", bg="#F0F8FF", font=("Arial", 12))
result_label_save.pack(pady=5)

# Bind the validation function to the entry fields
entry_count_save.bind("<KeyRelease>", lambda event: validate_save_inputs())

# Run the application
root.mainloop()
