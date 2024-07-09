from flask import render_template, request, redirect, url_for
from app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        town = request.form.get('town')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        if name and town and hobby and age:
            posts.append({'name': name, 'content': {'town': town, 'hobby': hobby, 'age': age}})
            return redirect(url_for('index'))
    return render_template('blog.html', posts=posts)