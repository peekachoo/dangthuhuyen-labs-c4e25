from flask import Flask, render_template

app = Flask(__name__)

# 1
# @app.route("/bmi/<int:w>/<int:h>")
# def bmi(w, h):
#     h = h/100
#     bmi = w/(h*h)
#     if bmi < 16:
#         r = "Severely underweight"
#     elif bmi < 18.5:
#         r = "Underweight"
#     elif bmi < 25:
#         r = "Normal"
#     elif bmi < 30: 
#         r = "Overweight"
#     else:
#         r = "Obese"
#     return r

# 2
@app.route("/bmi/<int:w>/<int:h>")
def bmi(w, h):
    h = h/100
    bmi = w/(h*h)
    return render_template("bmi.html", bmi=bmi)


if __name__ == "__main__":
    app.run(debug=True)