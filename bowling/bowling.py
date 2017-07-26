from flask import Flask, render_template, url_for, request

score = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
}
firstname = ""
lastname = ""
current_frame = 1


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/bowling_data', methods=['POST'])
def bowling_data():
    global firstname
    global lastname
    global score
    global current_frame

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    total_score = 0
    for num in score.values():
        total_score += num
    return render_template("bowling_score.html",
                           firstname=firstname,
                           lastname=lastname,
                           score=score,
                           total_score=total_score,
                           frame_number=current_frame)


@app.route('/update_score', methods=['POST'])
def update_score():
    # Sets the global variables
    global firstname
    global lastname
    global score
    global current_frame

    # Sets the frame score into the main score dict
    frame_score_input = int(request.form['input_score'])
    score[current_frame] = frame_score_input

    # Calculates the total score
    total_score = 0
    for num in score.values():
        total_score += num

    # Advances the current frame by 1
    current_frame += 1

    return render_template("bowling_score.html",
                           firstname=firstname,
                           lastname=lastname,
                           score=score,
                           total_score=total_score,
                           frame_number=current_frame)


if __name__ == '__main__':
    app.run(debug=True)
