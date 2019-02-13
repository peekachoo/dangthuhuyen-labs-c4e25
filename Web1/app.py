from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # Neu nguoi dung vao trang chu
def home(): # binding - goi homepage # ham dc dinh ngay sau route -> view function
    return "Hello World, this is flask homepage."

@app.route("/c4e25")
def c4e25():
    return "This is C4E25."

@app.route("/hi/quan")
def hi_me():
    return "Hello Quan."

@app.route("/hi/<name>") # <>
def hi(name):
    return "Hi " + name + "."

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    # in t(a, b)
    return str(a + b)

@app.route("/simple_html")
def simple_html():
    return "<h3>Simple</h3>"

@app.route("/html")
def html():
    return render_template("sample.html")

food_list = [
    "Cold Soba",
    "Tokbokki",
    "Udon",
    "Spaghetti",
    "Jajangmyeon"
]

@app.route("/menu")
def menu():
    return render_template("menu.html", food_list1=food_list)

@app.route("/food/<int:index>") # detail
def food(index):
    return render_template("food.html", title=food_list[index])

detail = {
    'title': 'Broccoli',
    'image': 'https://www.surdeplant.es/wp-content/uploads/2018/08/Healty-Green-Broccoli-green-34594014-736-767.jpg'
}

@app.route("/food_detail")
def food_detail():
    return render_template("food_detail.html", detail=detail)

if __name__ == "__main__":
    app.run(debug=True)