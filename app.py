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
    lotto = [1,2,3,4,5,6]

    ### 이곳을 같이 채워봐요


    ## example 1
    lotto = []
    for i in range(select_amount):

        while True:
            select_num = random.randint(1, 45)

            is_duplicated = False
            for num in lotto:
                if select_num == num:
                    is_duplicated = True
                    break

            if is_duplicated:
                continue
            lotto.append(select_num)
            break

    ## example 2
    '''
    candidate_numbers = lotto_numbers[:]
    lotto = []
    for i in range(select_amount):
        select_num = candidate_numbers.pop(random.randrange(len(candidate_numbers)))
        lotto.append(select_num)
    '''

    ## example 3
    '''
    lotto = random.sample(lotto_numbers, select_amount)
    '''
    return lotto

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) 