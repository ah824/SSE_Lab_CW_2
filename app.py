from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)

if __name__ == "__main__":
    app.run(debug=True)

 