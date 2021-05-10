"""for i in range(1, 101):
    string = ""
    if i % 5 == 0:
        string += "Fuzz"
    if i % 3 == 0:
        string += "Buzz"
    if string:
        print(string)
        continue
    print(i)
"""
variables = { "moral": 0, }
x = 5

def printSomething():
    global x
    x += 1
    print(x)

print(x)
printSomething()
print(x)

x = 103

if x >= 5 and x <= 7 or x > 100:
    print("yay")