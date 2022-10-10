import socket

from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route('/')

def index():
    
    var=socket.gethostname()

    return render_template('index.html.j2',var=var)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090,debug=True)

