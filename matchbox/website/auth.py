from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])    
def login():
    
    return render_template("login.html")

auth.route('logout', methods=['GET', 'POST'])
def logout():
    return render_template("logout.html")

auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template("sign_up.html")

