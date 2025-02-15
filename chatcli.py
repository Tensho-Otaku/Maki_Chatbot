import os
import time
from ollama import chat

class chatcli:
    def __init__(self, model):
        self.message_h = []
        self.model = model

    def add_m(self, role, content):
        """Add a message to the message history."""
        self.message_h.append({'role': role, 'content': content})
    def clear_screen(self):
        """Clear the console screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def chat_with_model(self, user_input):
        """Send the user input to the model and print the response."""
        self.add_m('user', user_input)
        context = ''

        for part in chat(self.model, messages=self.message_h, stream=True):
            context += part['message']['content']
            print(part['message']['content'], end='', flush=True)

        self.add_m('system', context)
        print("\n")

    def run(self):
        """Run the chat program in a loop."""
        while True:
            try:
                user_input = input("User Input: ")

                if user_input.strip().lower() in {"exit", "quit"}:
                    print("Exiting...")
                    break

                if user_input.strip().lower() in {"clear", "cls","clean"}:
                    self.clear_screen()
                    continue

                self.chat_with_model(user_input)

            except KeyboardInterrupt:
                print("\n\nKeyboard Interrupt!\n")
                time.sleep(.5)
                continue

