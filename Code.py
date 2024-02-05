import string
import random
from tkinter import *
from tkinter import messagebox
from twilio.rest import Client
# Yoimport ur Twilio account credentials
TWILIO_ACCOUNT_SID = “YOUR  SID”
TWILIO_AUTH_TOKEN = "YOUR API"
TWILIO_PHONE_NUMBER = "YOUR TWILIO NUMBER "
# Random Password Generator
def generate_random_password():
    length = int(random_length.get())
     characterList = ""
    if random_letters.get():
        characterList += string.ascii_letters
    if random_digits.get():
        characterList += string.digits
    if random_special.get():
        characterList += string.punctuation
    if len(characterList) == 0:
        messagebox.showerror("Error", "Please select at least one character set!")
        return
    password = []
    for i in range(length):
        randomchar = random.choice(characterList)
        password.append(randomchar)
    random_password_entry.delete(0, END)
    random_password_entry.insert(0, "".join(password))
    send_random_button.config(state=NORMAL)  # Enable the "Send Random Password" button
# Strong Password Generator
def generate_strong_password():
    characters_number = int(strong_length.get())
    if characters_number < 8:
        messagebox.showerror("Error", "Your number should be at least 8!")
        return
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)
    part1 = round(characters_number * (60 / 100))
    part2 = round(characters_number * (40 / 100))
    result = []
    for x in range(part1):
        result.append(s1[x])
        result.append(s2[x])
    for x in range(part2):
        result.append(s3[x])
        result.append(s4[x])
    random.shuffle(result)
    password = "".join(result)
    strong_password_entry.delete(0, END)
    strong_password_entry.insert(0, password)
    send_strong_button.config(state=NORMAL)  # Enable the "Send Strong Password" button
# Send Random Password via SMS
def send_random_password():
    phone_number = phone_entry.get()
    password = random_password_entry.get()
    purpose_text = purpose.get()
    if not phone_number:
        messagebox.showerror("Error", "Please enter your phone number!")
        return
    try:
        # Create a Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        # Send the SMS
        sms_body = f"The random password generated for '{purpose_text}' is: {password}"
        message = client.messages.create(
            body=sms_body,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        messagebox.showinfo("Success", "Random password sent to your phone!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
# Send Strong Password via SMS
def send_strong_password():
    phone_number = strong_phone_entry.get()
    password = strong_password_entry.get()
    purpose_text = purpose.get()
    if not phone_number:
        messagebox.showerror("Error", "Please enter your phone number!")
        return
    try:
        # Create a Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        # Send the SMS
        sms_body = f"The strong password generated for '{purpose_text}' is: {password}"
        message = client.messages.create(
            body=sms_body,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        messagebox.showinfo("Success", "Strong password sent to your phone!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
# Create GUI
root = Tk()
root.title("Password Generator")
root.geometry("400x650")
# Purpose Widget
purpose_frame = Frame(root)
purpose_frame.pack(pady=5)
purpose_label = Label(purpose_frame, text="Select Purpose:")
purpose_label.pack()
purpose = StringVar()
purpose.set("Select")
purpose_options = [
    "Gmail",
    "Instagram",
    "Facebook",
    "LinkedIn",
    "Twitter",
    "Netflix",
    "Amazon",
    "Dropbox",
    "GitHub",
    "Slack",
    "WhatsApp",
    "other"
]
purpose_menu = OptionMenu(purpose_frame, purpose, *purpose_options)
purpose_menu.pack(pady=5, padx=10, ipadx=10)
# Custom Purpose Entry (for "other" option)
custom_purpose_frame = Frame(root)
custom_purpose_frame.pack(pady=5)
custom_purpose_label = Label(custom_purpose_frame, text="Custom Purpose:")
custom_purpose_label.pack()
custom_purpose_entry = Entry(custom_purpose_frame, width=30)
custom_purpose_entry.pack(ipady=3)
# Random Password Generator
random_frame = Frame(root)
random_frame.pack(pady=5)
random_label = Label(random_frame, text="Random Password Generator")
random_label.pack()
random_length_label = Label(random_frame, text="Password Length:")
random_length_label.pack()
random_length = Spinbox(random_frame, from_=8, to=32, width=5)
random_length.pack()
random_letters = BooleanVar()
random_letters.set(True)
random_letters_checkbox = Checkbutton(random_frame, text="Include Letters", variable=random_letters)
random_letters_checkbox.pack()
random_digits = BooleanVar()
random_digits.set(True)
random_digits_checkbox = Checkbutton(random_frame, text="Include Digits", variable=random_digits)
random_digits_checkbox.pack()
random_special = BooleanVar()
random_special.set(True)
random_special_checkbox = Checkbutton(random_frame, text="Include Special Characters", variable=random_special)
random_special_checkbox.pack()
generate_random_button = Button(random_frame, text="Generate Random Password", command=generate_random_password,
                                padx=5, pady=5)
generate_random_button.pack()
random_password_entry = Entry(random_frame, width=30)
random_password_entry.pack(ipady=3)
# Phone Entry
phone_frame = Frame(root)
phone_frame.pack(pady=5)
phone_label = Label(phone_frame, text="Enter Phone Number:")
phone_label.pack()
phone_entry = Entry(phone_frame, width=30)
phone_entry.pack(ipady=3)
# Send Random Password via SMS
random_sms_frame = Frame(root)
random_sms_frame.pack(pady=5)
send_random_button = Button(random_sms_frame, text="Send Random Password via SMS", command=send_random_password,
                            state=DISABLED, padx=5, pady=5)
send_random_button.pack()
# Strong Password Generator
strong_frame = Frame(root)
strong_frame.pack(pady=5)
strong_label = Label(strong_ 
strong_length_label = Label(strong_frame, text="Password Length (min 8):")
strong_length_label.pack()
strong_length = Spinbox(strong_frame, from_=8, to=32, width=5)
strong_length.pack()
generate_strong_button = Button(strong_frame, text="Generate Strong Password", command=generate_strong_password,
                                padx=5, pady=5)
generate_strong_button.pack()
strong_password_entry = Entry(strong_frame, width=30)
strong_password_entry.pack(ipady=3)
# Send Strong Password via SMS
strong_sms_frame = Frame(root)
strong_sms_frame.pack(pady=5)
strong_phone_label = Label(strong_sms_frame, text="Enter Phone Number:")
strong_phone_label.pack()
strong_phone_entry = Entry(strong_sms_frame, width=30)
strong_phone_entry.pack(ipady=3
send_strong_button = Button(strong_sms_frame, text="Send Strong Password via SMS", command=send_strong_password,
                            state=DISABLED, padx=5, pady=5)
send_strong_button.pack()
# Start the main loop
root.mainloop()
