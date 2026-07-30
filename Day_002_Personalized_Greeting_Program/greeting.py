print("Welcome to our Python coding session!")
name = input("Enter Dev coder name:").strip()
# strip trim all spaces

if name:
    # title() capatilize each word first letter as formal
    clean_name = name.title()   
    print(f"Hello, {clean_name}!")
    print("I'm glad you are coding with us today.")
else:
    print("Hello, Mystery coder")
    print("Again run your program and share your name with us.")

