from flask import Flask, render_template, request
import random

app = Flask(__name__)

initial = -1


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == 'GET':
        return render_template("index.html", number=initial)
    else:
        first = int(request.form.get("first"))
        second = int(request.form.get("second"))
        result = random.randint(first, second)
        return render_template("index.html", number=result)


if __name__ == '__main__':
    app.run()