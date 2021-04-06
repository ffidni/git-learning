def greet_human_only(name):
    return f"Hello {name}!" if name.isalpha() else "No greeting for you."

if __name__ == '__main__':
    print(greet_human_only(input("Input your name: ")))