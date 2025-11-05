from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/staging')
def staging():
    return render_template('staging.html')

@app.route('/testing')
def testing():
    return render_template('testing.html')

if __name__ == '__main__':
    app.run(debug=True)