from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
   dojos = Dojo.get_all()
   print(dojos)
   return render_template('add_ninja.html', dojos = dojos)

@app.route('/ninjas/save', methods=['POST'])
def save_ninja():
   print(request.form)
   Ninja.create_ninja(request.form)
   return redirect('/')



