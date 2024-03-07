#creamos un entorno vistual -> python -m venv venv
#ctrl + shift + p 
#instalamos openai -> pip install openai en el terminal

#importamos el modulo
#traemos la key
#ultimo python chat.py

#from openai import OpenAI
import openai
import time  # for measuring time duration of API calls
import os

openai.api_key = "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"

chat_history = [] #una lista del historial de mensajes 

while True:
    prompt = input("ingresa una pregunta o prompt: ")

    if prompt == "exit":
        break
    else:
        chat_history.append({"role": "user", "content": prompt}) #el prompt en el historial
        response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages= chat_history,
                stream = True,
                max_tokens= 50,
         )

        collected_chunks = []
        collected_messages = []
            # iterate through the stream of events
        for chunk in response:
            collected_chunks.append(chunk)  # save the event response
            chunk_message = chunk.choices[0].delta.content  # extract the message
            collected_messages.append(chunk_message)  # save the message
                

        # clean None in collected_messages
        collected_messages = [m for m in collected_messages if m is not None]
        full_reply_content = ''.join([m for m in collected_messages])


        chat_history.append({"role": "system", "content": full_reply_content}) #la respuesta tambien en el historial
        print(f"Full conversation received: {full_reply_content}")

        #response_message = response.choices[0].message.content
        #print(response_message)









