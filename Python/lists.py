def returnitem(number):
    funclist = [0, 1, 2, 3, 4]
    return funclist[number]

try:
    print (returnitem(int(input("Enter a number: "))))
except:
    print ("Sorry, not able to return")
