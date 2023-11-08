import csv

def main():
    add_no_duplicates("shopping_list.csv", "peppers")


def fridge_list():
    file = open("fridge.csv", "r")
    data = list(csv.reader(file, delimiter=","))[0]
    file.close()
    return data

def store_list():
    file = open("shopping_list.csv", "r")
    data = list(csv.reader(file, delimiter=","))[0]
    file.close()
    return data

def use_up():
    file = open("fridge.csv", "r")
    fridge = list(csv.reader(file, delimiter=","))[0]
    file = open("data.csv", "r")
    done = list(csv.reader(file, delimiter=","))[0]
    result = []

    for word in fridge:
        if word in done:
            print(word)
        else:
            result.append(word)

    file = open("fridge.csv", "w")
    for word in result:
        file.write(word + ",")

    file.close()

    return result

""" def add():
    file = open("shopping_list.csv", "r")
    shopping_list = list(csv.reader(file, delimiter=","))[0]
    file = open("data.csv", "r")
    data = list(csv.reader(file, delimiter=","))[0]
    result = []

    for word in data:
        result.append(word)

    file = open("shopping_list.csv", "a")
    for word in result:
        file.write(word + ",")

    file.close()

    return result """


def add_no_duplicates(filename, text):
    file = open(filename, "r")
    datalist = list(csv.reader(file, delimiter=","))[0]
    file.close()

    datalist.append(text)

    no_duplicates_list = list(set(datalist))

    file = open(filename, "w")
    for item in no_duplicates_list:
        file.write(item + ",")
    file.close()

    return no_duplicates_list




    
""" 
def load_pantry():
    file = open("pantry.csv", "r")
    data = list(csv.reader(file, delimiter=","))[0]
    return data

def load_recipe():
    recipes = ["chicken_marsala_pasta", "fried_rice", "salmon", "beef_tacos"]
    for num in range(len(recipes)):
        print(str(num) + ": " + recipes[num])
    print("Please select a recipe: ")
    choice = int(input())
    recipe = recipes[choice]

    file = open(recipe+".csv", "r")
    data = list(csv.reader(file, delimiter=","))[0]

    return data
    
def compare(pantry, recipe):

    common = list(set(pantry) & set(recipe))
    dont_have = list(set(recipe) - set(pantry))

    print("Yay! You have: ")
    for ingredient in common:
        print(ingredient)
    print()
    print("To make this recipe you need to buy: ")
    for ingredient in dont_have:
        add_to_list(ingredient)
        print(ingredient)
    print("They have been added to your shopping list!")


def add_to_list(ingredient):
    file = open("shopping_list.csv", "a")
    file.write(ingredient+",")
    file.close() """

main()