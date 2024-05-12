import pyshorteners
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

#Код ниже нужен для любой ошибке. При ошибке пользователь будет перенаправляться на главную страницу 
@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('home.html')

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        input_data = request.form["input-nickname"]
        print(input_data)
        pys = pyshorteners.Shortener()
        short = pys.tinyurl.short(input_data)

        #возврат сокращенного URL на html странице
        return render_template("return.html", short_url=short)

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
