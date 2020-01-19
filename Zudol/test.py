from flask import Flask
import Drowsiness_Detection

app = Flask(__name__)
app.config["DEBUG"] = True

@app.rout('/')


def index():
    # Connecting to a template (html file)
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9006)
