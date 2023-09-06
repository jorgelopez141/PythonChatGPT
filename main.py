########
## Este archivo es una conversacion total
## primero te va a pedir que le des un nombre a tu archivo donde va a guardar toda la conversacion con chatgpt
## asegurate de tener una conversacion de un tema en especifico
## luego le das "quit" cuando querras terminar la platica 
## recorda que el titulo es como se va a llamar el archivo. por lo tanto no pongas ?/\. ni nada de eso

## esto lo aprendiste de este video: https://www.youtube.com/watch?v=YVFWBJ1WVF8

## para leer el output del archivo utiliza el archivo readingPythonOutput.py


#######

import openai 
import apiKey
import os 
import json

from datetime import datetime
now = datetime.now()

current_time = now.strftime("%m-%d-%y %H-%M-%S")
#print("Current Time =", current_time)




openai.api_key= apiKey.MY_API_KEY

#print(apiKey.MY_API_KEY)

### code that works 
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[        
#             {"role":"user","content": "Who is stronger Superman or Hulk?"}                    
#     ]
# )

# print(response)
### until here

chat_log = []
titleChat = input("title of this chat?")

finalFileName= titleChat + " " + current_time +".txt"

while True:
    user_message = input("Send a message: \n")
    if user_message.lower() == "quit":
        with open(finalFileName,"w") as f:
            for i in chat_log:
                f.write(json.dumps(i)) #transforma diccionario en texto json.dumps
                f.write("\n") 
        break 
    else:
        chat_log.append({"role":"user","content": user_message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_log
        )
        
        assistant_response= response['choices'][0]["message"]["content"]
        print("ChatGPT:",assistant_response,"\n")
        chat_log.append({"role":"assistant","content": assistant_response})