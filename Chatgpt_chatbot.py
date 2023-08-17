import openai
# $5 is free after that money is required
openai.api_key="paste api key"

messages=[]
system_msg=input("What type of chatbot would u like to create\n")
messages.append({"role":"system","content":system_msg})

print("Your assistant is ready")
while input != "quit()":
    message=input()
    
    messages.append({"role":"user","content":message})
    response=openai.ChatCompletion.create(                                          
        model="gpt-3.5-turbo",
        messages=messages)
    reply=response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":reply})
    print("\n" + reply + "\n")  