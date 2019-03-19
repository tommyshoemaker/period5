while True:
    inputtext = str(input("Input encrypted message: "))

    translate = str.maketrans(
        "qwfpgjluyarstdhneiozxcvbkm", "qwertyuiopasdfghjklzxcvbnm"
    )

    translation = inputtext.translate(translate)

    print(translation)
