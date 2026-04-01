from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def feedback():
    print("Page loaded")   # 👈 add this line

    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        feedback = request.form.get("feedback")
        message = f"Thanks {name}, your feedback is received!"

    return render_template("form.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)