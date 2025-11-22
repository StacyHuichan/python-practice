def greet_person(name=None):
    if name is None:
        name = input("What is your name? ")

    print(f"Hello, {name}!")
    mood = input("How are you feeling?" ).lower()

    if mood == "happy":
        print("Cool")
    elif mood =="Tired":
        print("Go to sleep!")
    elif mood == " Excited":
        print("Yay!!!")
    else:
        print("Go away!")
    
    print(" What you want? -_-")

greet_person()
greet_person("Stacy")