from flask import Flask, render_template, request
import random, os
from werkzeug.utils import secure_filename
from datetime import datetime

from ml_model import predict_duplicate

app = Flask(__name__)
random.seed(0)
app.config['SECRET_KEY'] = os.urandom(24)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

dir_path = os.path.dirname(os.path.realpath(__file__))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        q1 = request.form.get('question1', '')
        q2 = request.form.get('question2', '')
        if q1 and q2:
            pred = predict_duplicate(q1, q2)
            if pred == 1:
                result = "These questions are the same."
            else:
                result = "These questions are different."
        else:
            result = "Please enter both questions."
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)