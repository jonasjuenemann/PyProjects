"""print("Hi, this is Chatbot")
print("I will repeat what you say")
username = input("Tell me your Name: ")
print("Cool " + username + ". Good to know you!")"""


# Define your functions

def coffee_bot():
    print("Welcome to the cafe!")
    name = get_name()
    if name in ["exit", "q", "quit"]:
        return
    order_drink = True
    drinks = []
    drink_dic = {"a": "Brewed Coffee", "b": "Mocha", "c": "Latte", }
    size_dic = {"a": "Small", "b": "Medium", "c": "Large", }
    mocha_dic = {"a": "peppermint mocha", "b": "mocha", }
    milk_dic = {"a": "2% milk", "b": "Non-fat milk", "c": "Soy milk", }
    while order_drink:
        drink_type = get_drink_type()
        size = get_size()
        if drink_type == "b":
            mocha = order_mocha()
            drinks.append([drink_type, size, mocha])
            print(f"Great, A " + mocha_dic[mocha] + " in Size " + size_dic[size] + " is being prepared for you!")
            order_drink = continue_order()
            continue
        if drink_type == "c":
            milk_type = order_latte()
            drinks.append([drink_type, size, milk_type])
            print(f"Great, A " + drink_dic[drink_type] + " with " + milk_dic[milk_type] + " in Size " + size_dic[size] + " is being prepared for you!")
            order_drink = continue_order()
            continue
        drinks.append([drink_type, size])
        print(f"Great, A " + drink_dic[drink_type] + " in Size " + size_dic[size] + " is being prepared for you!")
        order_drink = continue_order()
    print(f"Thank you for your order {name}. You ordered: ")
    return_string = ""
    for i in drinks:
        return_string += ""
        if i[0] == "b":
            return_string += f"A {mocha_dic[i[0]]} in Size {size_dic[i[1]]}\n"
        elif i[0] == "c":
            return_string += f"A {drink_dic[i[0]]} in Size {size_dic[i[1]]} with {milk_dic[i[2]]}\n"
        else:
            return_string += f"A {drink_dic[i[0]]} in Size {size_dic[i[1]]}\n"
    print(return_string)
    return

def get_name():
    name = input("Can I get your name please? ")
    return name

def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    res = res.lower()
    if res not in ["a", "b", "c"]:
        print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
        res = get_size()
    return res

def get_drink_type():
    res = input('And What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
    res = res.lower()
    if res not in ["a", "b", "c"]:
        print(
            "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
        res = get_drink_type()
    return res

def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
    res = res.lower()
    if res not in ["a", "b", "c"]:
        print(
            "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
        res = order_latte()
    return res

def order_mocha():
    while True:
        res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! ')
        if res not in ["a", "b"]:
            print(
                "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
            continue
        return res

def continue_order():
    res = input('Would you like to order another drink? (y/n) ')
    res = res.lower()
    if res not in ["y", "n"]:
        print(
            "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
        res = continue_order()
    if res == "y":
        return True
    if res == "n":
        return False

# Call coffee_bot()!

coffee_bot()
