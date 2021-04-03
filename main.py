from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    cont = 'test'
    return render_template('index.html', cont)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)