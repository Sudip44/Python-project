import tkinter as tk
import nltk
import random
import re
import time
from nltk.chat.util import Chat, reflections

#download necessary nltk resources
nltk.download('punkt')

#a dictionary to store user information
user_info = {}

#define pairs of inputs and respomses for the chatbot
pairs =[
   (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, how about you?', 'I am great, thanks for asking!']),
    (r'what is your name?', ['I am a chatbot, I don’t have a name!', 'You can call me Chatbot!']),
    (r'bye|exit', ['Goodbye! Take care.', 'See you later!']),
    (r'help', ['I can help you with general queries, just ask!']),
    (r'what is your name?', ['I don’t have a personal name, but you can call me Chatbot!']),
    (r'what time is it?', [f'The current time is {time.strftime("%H:%M:%S")}.']),
    (r'what is the date today?', [f'Today is {time.strftime("%A, %B %d, %Y")}.']),
    (r'what is your favorite color?', ['I am just a chatbot, I don’t have preferences, but I think blue is cool!']),
    (r'add (\d+) and (\d+)', lambda match: f"The sum is {int(match.group(1)) + int(match.group(2))}."),
    (r'give me a joke', ['Why don’t skeletons fight each other? They don’t have the guts!']),

]
#function to handle user info
def get_user_name(user_input):
    """Get the user's name from their input."""
    match = re.match(r"my name is (.*)", user_input, re.IGNORECASE)
    if match:
        user_info["name"] = match.group(1)
        return f"Your name is {user_info['name']}."
    return None

#create a chatbot
def get_response(user_input):
    if "name" not in user_info:
        name_response = get_user_name(user_input)
        if name_response:
            return name_response
        chat = Chat(pairs, reflections)
        response = chat.respond(user_input)
        if response is None:
            response = "Sorry, I didn't understand that. Could you please rephrase?"
        return response
    def send_message():
        """Send a message to the chatbot."""
        user_input = user_entry.get().strip().lower()
        if user_input == "":
            return
        if user_input in ("exit", "bye", "goodbye"):
            root.destroy()
        else:
            # clear the input field
            user_entry.delete(0, tk.END)
            # add the user's input to the conversation window
            try:
                conv_window.config(state=tk.NORMAL)
                conv_window.insert(tk.END, f"You: {user_input}\n")
                conv_window.config(state=tk.DISABLED)
                # get the chatbot's response and add it to the conversation window
                response = get_response(user_input)
                conv_window.config(state=tk.NORMAL)
                conv_window.insert(tk.END, f"Chatbot: {response}\n")
                conv_window.config(state=tk.DISABLED)
                # scroll to the bottom of the conversation window
                conv_window.see(tk.END)
            except Exception as e:
                print(f"Error: {e}")

    root = tk.Tk()
    root.title("Chatbot")
    #create a frame for converstation
    frame = tk.Frame(root)
    scrollbar = tk.Scrollbar(frame)
    conv_window = tk.Text(frame,wrap=tk.WORD,yscrollcommand=scrollbar.set, height=50, width=50, state=tk.DISABLED)
    scrollbar.config(command=conv_window.yview)
    frame.pack(padx=10,pady=10)
    conv_window.pack(side=tk.LEFT)
    scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

    #create a input field
    user_entry = tk.Entry(root, width=40)
    send_button = tk.Button(root, text="Send", command=send_message)
    user_entry.pack(padx=10,pady=10)
    send_button.pack(pady=5)
    
    #start the loop
    root.mainloop()
