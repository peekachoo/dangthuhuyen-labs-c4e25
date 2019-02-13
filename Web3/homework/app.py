from flask import Flask , render_template , request
app = Flask(__name__)

@app.route('/new_bike' ,methods=["GET","POST"])
def new_bike():
    if request.method == "GET":
        return render_template("bike.html")
    elif request.method == "POST":
        form = request.form
        m = form["model"]
        f = form["fee"]
        i = form["image"]
        y = form["year"]
        # print(m, f, i, y)
        return "POST"

if __name__ == '__main__':
  app.run(debug=True)