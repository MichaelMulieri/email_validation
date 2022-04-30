from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add/email', methods=['POST'])
def add_email():
    if not User.validate_email(request.form):
        return redirect('/')
    User.save(request.form)
    return redirect('/success')

@app.route('/success')
def show_email():
    users = User.get_all()
    return render_template('all_email.html' , all_email = users)

@app.route('/destroy/<int:id>')
def destroy(id):
    data = {
        "id":id
    }
    User.destroy(data)
    return redirect("/success")
