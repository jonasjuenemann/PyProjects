x = 1
y = [2]

# basically nen destructuring operqator, aber nur für Elemente mit length=1
x, = y

print(x)

y = 1


def j():
    print(y)  # funktioniert
    z = y + 5
    z += 1
    print(z)
    # y += 1  # funktioniert nicht, vorherige Teile der Funktion ebenfalls nicht mehr
    # y = 454545 # funktioniert nicht, da vorherige Teile der Funktion nicht mehr funktionieren -> auf einmal: referenz bevor Assignment
    # whether a variable is a global variable or local variable is determined at compile time
    # einer der Gründe spezifische main-Funktion zu definieren.


j()

names = ["Elaine", "George", "Jerry", "Cosmo"]

greetings = [f"Hello, {name}" for name in names]

print(greetings)

is_Jerry = [True if name == "Jerry" else False for name in names]

nested_lists = [[4, 8], [15, 16], [23, 42]]

product = [i1 * i2 for (i1, i2) in nested_lists]

greater_than = [True if (i1 > i2) else False for (i1, i2) in nested_lists]

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
print(list(zip(a, b)))
sums = [a + b for a, b in list(zip(a, b))]
print(sums)

quotients = [b / a for a, b in zip(a, b)]
print(quotients)

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))
# the start=1 option to enumerate here is optional. If we didn’t specify this, we’d start counting at 0 by default.

names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]

users = [f"Name: {name}, Age: {age}" for name, age in zip(names, ages)]

print(users)

a = [30, 42, 10, 45, 23, 67]
b = [15, 16, 17]

greater_than = [True if a > b else False for a, b in zip(a, b)]

print(greater_than)


for i, num in enumerate(a):
    a[i]

print(a)