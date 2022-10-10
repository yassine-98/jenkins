from flask import Flask, render_template
import random
app = Flask(__name__)

# list of cat images 
images = ["https://media1.tenor.com/images/80102550479835807fdd8ab3cbab2565/tenor.gif?itemid=15731367",
"https://th.bing.com/th/id/R.ca1e51c1d1d5a5ef16ff756c0cae532e?rik=4q%2fG%2feyqKx%2bKzQ&riu=http%3a%2f%2fgif-free.com%2fuploads%2fposts%2f2017-04%2f1491807253_cat-about-to-pounce.gif&ehk=Azy1%2b%2frdizHU0UU2a77MIDBaBY9H8DMUqic4QjjWY8Q%3d&risl=&pid=ImgRaw&r=0"]
@app.route('/')

def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8070,debug=True)