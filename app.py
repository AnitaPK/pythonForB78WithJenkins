from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # some sample data
    users = [
        {"name": "Rahul", "age": 25, "email": "rahul@gmail.com"},
        {"name": "Anita", "age": 28, "email": "anita@gmail.com"},
        {"name": "Amit", "age": 30, "email": "amit@gmail.com"},
        {"name": "Pooja", "age": 29, "email": "pooja@gmail.com"}
    ]
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
