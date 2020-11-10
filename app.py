from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)


lotto_numbers = list(range(1,46))

@app.route("/")
def hello():

    return render_template("index.html", variable=lotto)

@app.route("/lotto",methods=['GET'])
def lotto():
    lotto = select_numbers(6)
    return jsonify(lotto)

def select_numbers(select_amount:int):
    ### 이곳을 같이 채워봐요

    lotto = [1,2,3,4,5,6]


    return lotto

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)