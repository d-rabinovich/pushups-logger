# This file is responsible for CRUD: Create, Update, Delete
from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)

# Home page
@main.route('/')
def index():
    return render_template('index.html')

# Profile page
@main.route('/profile')
def profile():
    return render_template('profile.html')