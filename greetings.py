def greetings(name, lang):
    greeting = {
        "English" :"Hello",
        "Spanish" : "Hola",
        "French" :"Bonjour",
        "Yoruba" :"Ele o"
        }
    msg = f"{greeting[lang]} {(name)}!"
    print(msg)
