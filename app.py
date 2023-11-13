from flask import Flask, render_template, request
from pantry_pal import *

app = Flask(__name__)


# run this with flask --app app run

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        submitted_pass = request.form['password']
        submitted_username = request.form['username']

        if submitted_pass == "samsom" and submitted_username == "anja":
            return render_template('home.html')
        else:
            return render_template("login.html")

    elif request.method == 'GET':
        return render_template('login.html')
    
@app.route("/home", methods=['GET', 'POST'])
def homepage():
    return render_template('home.html')

    

@app.route("/fridge", methods=['GET', 'POST'])
def fridge():
    data = fridge_list()
    return render_template('fridge.html', data = data)

@app.route("/cookbook", methods=['GET', 'POST'])
def cookbook():
    r1 = compare("recipes/broccoli_coconut_noodles.csv")
    r1h = r1[0] #recipe 1 have
    r1d = r1[1] #recipe 1 don't have
    r2 = compare("recipes/chicken_marsala_pasta.csv")
    r2h = r2[0]
    r2d = r2[1] 
    r3 = compare("recipes/fried_rice.csv")
    r3h = r3[0]
    r3d = r3[1] 
    r4 = compare("recipes/salmon.csv")
    r4h = r4[0]
    r4d = r4[1] 
    r5 = compare("recipes/spicy_noodles.csv")
    r5h = r5[0]
    r5d = r5[1] 

    return render_template('cookbook.html', r1h = r1h, r1d = r1d,
                            r2h = r2h, r2d = r2d, 
                            r3h = r3h, r3d = r3d, 
                            r4h = r4h, r4d = r4d, 
                            r5h = r5h, r5d = r5d, )



@app.route("/add_list1.py", methods=["POST"])
def add_list1():
    recipe = compare("recipes/broccoli_coconut_noodles.csv")
    dont_have = recipe[1]
    add_remaining_ingredients(dont_have)

    #specifiy a method that calls another method, that method does all the work, the first one just specifies which recipe csv to use

    return render_template('home.html')

@app.route("/add_list2.py", methods=["POST"])
def add_list2():
    recipe = compare("recipes/chicken_marsala_pasta.csv")
    dont_have = recipe[1]
    add_remaining_ingredients(dont_have)


    return render_template('home.html')

@app.route("/add_list3.py", methods=["POST"])
def add_list3():
    recipe = compare("recipes/fried_rice.csv")
    dont_have = recipe[1]
    add_remaining_ingredients(dont_have)

    return render_template('home.html')

@app.route("/add_list4.py", methods=["POST"])
def add_list4():
    recipe = compare("recipes/salmon.csv")
    dont_have = recipe[1]
    add_remaining_ingredients(dont_have)


    return render_template('home.html')

@app.route("/add_list5.py", methods=["POST"])
def add_list5():
    recipe = compare("recipes/spicy_noodles.csv")
    dont_have = recipe[1]
    add_remaining_ingredients(dont_have)

    return render_template('home.html')



@app.route("/write_data_use_up.py", methods=["POST"])
def write_data_use_up():
    text = request.form.get("text")

    file = open("data.csv", "a")

    file.write(text + ",")
    file.close()

    data = use_up()
    return render_template('fridge.html', data = data)


@app.route("/shopping_list", methods=['GET', 'POST'])
def shopping_list():
    data = store_list()
    return render_template('shopping_list.html', data = data)

@app.route("/write_data_add.py", methods=["POST"])
def write_data_add():
    text = request.form.get("text")

    data = add_no_duplicates("shopping_list.csv", text)

    return render_template('shopping_list.html', data = data)

@app.route("/remove.py", methods=["POST"])
def remove():
    text = request.form.get("text")


    data = remove_ingredient("shopping_list.csv", text)
    # then add this ingredient to the fridge
    add_no_duplicates("fridge.csv", text)

    return render_template('shopping_list.html', data = data)

