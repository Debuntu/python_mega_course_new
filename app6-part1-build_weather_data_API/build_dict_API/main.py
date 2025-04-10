from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")

def home():
    return render_template("home.html")

#here we are taking the 'word as a variable in the url like <word>
@app.route("/api/v1/<word>")
def meaning(word):
    return {
        'definition': word,
        'word': word.upper()
    }


if __name__ == "__main__":
    #by default flask apps run on 5000 port, in case we want multiple apps running on flask, need to specify different ports
    # app.run(debug=True, port=5001)
    app.run(debug=True, port=5000)