from flask import  render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/proceso', methods=['POST'])
def create_dojo():
    print(request.form)
    if not Dojo.validate_dojo(request.form):

        return redirect('/')
    else:
        Dojo.save(request.form)
    return redirect("/results")

@app.route('/results')
def results():
    encuesta = Dojo.last()
    return render_template('results.html', encuesta=encuesta)

