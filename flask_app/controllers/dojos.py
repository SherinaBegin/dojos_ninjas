from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
   return redirect('/dojos')

@app.route('/dojos')
def dojos():
   dojos = Dojo.get_all()
   print(dojos)
   return render_template('index.html', dojos = dojos)

@app.route('/dojo/create', methods=['POST'])
def create_dojo():
   print(request.form)
   Dojo.save_dojo(request.form)
   return redirect ('/')

@app.route('/dojo/<int:id>')
def show_dojo(id):
   data = {
      'id': id
   }
   return render_template('show_dojo.html', dojo = Dojo.get_one(data))

@app.route('/dojo/delete/<int:id>')
def delete_dojo(id):
   data = {
      'id':id
   }
   Dojo.delete_dojo(data)
   return redirect('/dojos')


