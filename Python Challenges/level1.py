while True:
    inputtext = str(input("Input encrypted message: "))

    translate = str.maketrans(
        "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
    )

    translation = inputtext.translate(translate)

    print(translation)
