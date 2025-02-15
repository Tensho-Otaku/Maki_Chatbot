import ollama
import os
from chatcli import chatcli
model = "chatbot_py"


modelfile='''
FROM mistral
SYSTEM You are a human friendly language model named "Maki" specialized in generating only 3 creative idea title when asked for it, elaborate on the ideas which are selected by the user's intent.
'''
model_list = [i["model"].split(":")[0] for i in ollama.list()["models"]]
def chat():
  cli = chatcli(model)
  if model not in model_list:
    try:
      print("Chatbot Model doesnt Exist \nCreating Chatbot Model")
      ollama.create(model=model,from_="mistral" , system=modelfile)
    except Exception as e:
      print(f"Error: {e}")
    else:
      print("Chatbot Model has been created")
      cli.run()
  else:
    cli.run()



#Main
if "mistral" not in model_list:
  try:
    print("Mistral Model doesnt Exist \nDownloading Mistral Model")
    os.system("ollama pull mistral")
  except Exception as e:
    print(e)
  else:
    print("Downloaded Mistral Model")
    chat()

else:
  chat()
