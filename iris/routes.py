from . import app
from flask import render_template, request
from . import dataset
import joblib
import os

data = dataset.data_to_dict()


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html",
                           page_name='Home')


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        data_row = list()

        for a, b, c, d, e in zip(data["sepal length (cm)"], data["sepal width (cm)"],
                                 data["petal length (cm)"], data["sepal width (cm)"], data["targets"]):
            data_row.append([a, b, c, d, e])
        return render_template("about.html",
                               datahead=data.keys(),
                               dataset=data_row,
                               page_name='About')


@app.route("/graphs")
def graph():
    return render_template("graphs.html",
                           page_name='Graphs')


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("predict.html",
                               page_name='Predict',
                               first_result="Setosa",
                               model='dtc',
                               measures=[1.0, 1.0, 1.0, 1.0])
    else:
        model = request.form["options"]

        m = joblib.load(os.getcwd() + f"\\iris\\ML_models\\{model}.sav")
        prediction = m.predict([[
            float(request.form["sw"]),
            float(request.form["sl"]),
            float(request.form["pw"]),
            float(request.form["pl"]),
        ]])
        print(model, prediction)
        return render_template("predict.html",
                               page_name='Predict',
                               result=prediction[0],
                               model=model,
                               measures=[request.form["sw"],
                                         request.form["sl"],
                                         request.form["pw"],
                                         request.form["pl"]])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',
                           page_name='Oops o_0'), 404
