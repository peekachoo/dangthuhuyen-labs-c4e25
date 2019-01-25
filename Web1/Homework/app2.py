from flask import Flask, render_template

app = Flask(__name__)

profile = {
    "l": {
                "Name": "L Lawliet",
                "Gender": "Male",
                "Yob": 1979,
                "Likes": "Sweets"
            },
    "mello": {
                "Name": "Mihael Keehl",
                "Gender": "Gay",
                "Yob": 1989,
                "Likes": "Chocolate"
            }, 
    "near": {
                "Name": "Nate River",
                "Gender": "Male",
                "Yob": 1991,
                "Likes": "Toys"
            },
    "matt": {
                "Name": "Mail Jeevas",
                "Gender": "Gay",
                "Yob": 1990,
                "Likes": "Mello"
            }
}

@app.route("/user/<username>")
def user(username):
    wammy = {}
    f = "light"
    for i, j in profile.items():
        if i.lower() == username:
            for k, l in j.items():
                wammy[k] = l
            f = "dark"

    if f == "light":
        return "User not found"
    else: 
        return render_template("user.html", wammy=wammy)

if __name__ == "__main__":
    app.run(debug=True)