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

    return render_template('shopping_list.html', data = data)

