from flask import Flask , render_template , url_for , request

app = Flask(__name__)

@app.route("/")
def main ():
    return render_template("index.html")

@app.route("/calculate", methods=["post"])
def calculate ():
    firstNumber = int(request.form["firstNumber"])
    operation = request.form["operation"]
    secondNumber = int(request.form["secondNumber"])
    note = ""
    color = "alert-success"

    if operation == "plus":
        result = firstNumber + secondNumber
        note = "Addition is successfully performed"
    elif operation == "minus":
        result = firstNumber - secondNumber
        note = "Subtraction is successfully performed"
    elif operation == "multiply":
        result = firstNumber * secondNumber
        note = "Multiplication is successfully performed"
    elif operation == "divide":
        result = firstNumber / secondNumber
        note = "Division is successfully performed"
    else:
        color = "alert-warning"
        note = "there is an error"
        print("there is an error")
    return render_template("index.html", result=result , note = note ,color = color )

if __name__ == "__main__":
    app.run(debug=True)