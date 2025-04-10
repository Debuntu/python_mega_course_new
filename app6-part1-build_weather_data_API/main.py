from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 15
    return {'station': station,
            'date': date,
            'temperature': temperature
    }


if __name__ == "__main__":
    #by default flask apps run on 5000 port, in case we want multiple apps running on flask, need to specify different ports
    # app.run(debug=True, port=5001)
    app.run(debug=True, port=5001)