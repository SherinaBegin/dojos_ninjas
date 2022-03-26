from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.ninja import Ninja

@app.route('/ninjas/add', methods=['POST'])
def add_ninja():
   print(request.form)
   Ninja.save_ninja(request.form)
   return redirect('/')
