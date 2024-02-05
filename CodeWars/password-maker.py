def make_password(phrase):
    password = phrase[0]
    for i in range(1, len(phrase)):
        if phrase[i - 1] == " ":
            password += phrase[i]
    # print(password)

    for char in password:
        if char.lower() == "i":
            password = password.replace(char, "1")
        elif char.lower() == "o":
            password = password.replace(char, "0")
        elif char.lower() == "s":
            password = password.replace(char, "5")

    return password
