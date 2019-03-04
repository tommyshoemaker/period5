while True:
    inputtext = str(input("Input message to encrypt: "))
    translate = str.maketrans(
        "abcdefghijklmnopqrstuvwxyz", "yzabcdefghijklmnopqrstuvwx"
    )

    translation = inputtext.translate(translate)

    print(translation)
