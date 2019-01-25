from flask import Flask, redirect 

app = Flask(__name__)

@app.route("/about_me")
def about_me():
    return "Name: Dang Thu Huyen<br/>Age: 19<br/>Job: Student<br/>Hobbies: Drawing, singing,..."

@app.route("/school")
def school():
    return redirect("http://techkids.vn")

if __name__ == "__main__":
    app.run(debug=True)