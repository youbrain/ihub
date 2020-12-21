import os

from app import app, db
from models import Events
from forms import AddEventForm

from datetime import datetime
from sqlalchemy import extract
from sqlalchemy.sql import select
from werkzeug.utils import secure_filename
from flask import (Flask, request, render_template,
                   redirect, url_for, make_response,
                   send_file)


@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    login_hash = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'root' and password == 'pass':
            login_hash = 'sucs'
            res = make_response(redirect(url_for('dashboard')))
            res.set_cookie('session', login_hash)
            return res

        message = "Wrong username or password"

    res = make_response(render_template(
        'dashboard/login.html', message=message))
    res.set_cookie('session', login_hash)
    return res


@app.route('/dashboard/', methods=['get'])
def dashboard():
    if not request.cookies.get('session') == 'sucs':
        return redirect(url_for('login'))

    return render_template('dashboard/index.html')


@app.route('/add_event/', methods=['get', 'post'])
def add_event():
    form = AddEventForm()
    if form.validate_on_submit():
        # if f.filename
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save('uploads/' + filename)
        # date = [int(a) for a in form.time.data.split('-')][-1]
        query = Events(
            type=form.type.data,
            img_path='uploads/' + filename,
            time=datetime.strptime(
                form.time.data, '%d-%m-%Y %H:%M'),  # datetime(*date),
            title=form.title.data,
            description=form.description.data,
        )
        db.session.add(query)
        db.session.commit()

    return render_template('dashboard/add_event.html', form=form)


@app.route('/change_cookie/', methods=['POST'])
def change_cookie():
    cookie = request.form['change_cookie'].split(':')
    res = make_response(redirect('/dashboard'))
    res.set_cookie(*cookie)
    return res


@app.route('/uploads/<name>')
def get_file(name):
    return send_file('uploads/' + name, mimetype='image')


@app.route('/')
def index():
    # ivents = insta_posts.query.all()
    return render_template('index.html', posts=posts)


@app.route('/calendar/')
def calendar():
    # currwnt_month = datetime.now().strftime("%m")
    # conn = engine.connect()
    # r = select(Events)
    # r = db.session.execute(r)
    ivents = Events.query.all()

    return render_template('calendar.html', ivents=ivents)


# if __name__ == '__main__':
app.run(debug=True)
