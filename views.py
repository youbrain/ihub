import os

from app import app, db
from models import Events, InstaPosts
from forms import AddEventForm

from datetime import datetime
from sqlalchemy import extract, insert
from sqlalchemy.sql import select
from werkzeug.utils import secure_filename
from flask import (Flask, request, render_template,
                   redirect, url_for, make_response,
                   send_file)

from scrapper.insta import *


@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    login_hash = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'root' and password == 'ihubadmin':
            login_hash = 'sucs'
            res = make_response(redirect(url_for('dashboard')))
            res.set_cookie('session_', login_hash)
            return res

        message = "Помилка входу"

    res = make_response(render_template(
        'dashboard/login.html', message=message))
    res.set_cookie('session', login_hash)
    return res


@app.route('/dashboard/', methods=['get'])
def dashboard():
    if not request.cookies.get('session_') == 'sucs':
        return redirect(url_for('login'))

    return render_template('dashboard/index.html')


@app.route('/add_event/', methods=['get', 'post'])
def add_event():
    if not request.cookies.get('session_') == 'sucs':
        return redirect(url_for('login'))

    ivents = Events.query.all()
    form = AddEventForm()

    if request.method == 'POST':

        if form.validate_on_submit():
            # print('\n\n\n')
            # try:
            # if f.filename
            f = form.photo.data
            filename = secure_filename(f.filename)
            # 'uploads/' + filename)  #
            try:
                f.save('/root/ihub/uploads/' + filename)
            except FileNotFoundError:
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

            ivents = Events.query.all()

            print(request.args)

            return redirect(url_for('add_event'))
            # return render_template('dashboard/add_event.html', form=form, message=[1, 'Подія додана!'], ivents=ivents)
            # except:
            #     return render_template('dashboard/add_event.html', form=form, message=[0, 'Помилка'])

    # print('\n\n\n')
    return render_template('dashboard/add_event.html', form=form, ivents=ivents)


@app.route('/change_cookie/', methods=['POST'])
def change_cookie():
    cookie = request.form['change_cookie'].split(':')
    res = make_response(redirect('/dashboard'))
    res.set_cookie(*cookie)
    return res


@app.route('/logout/', methods=['get'])
def logout():
    res = make_response(redirect(url_for('index')))
    res.set_cookie('session_', '')
    return res


@app.route('/uploads/<name>')
def get_file(name):
    return send_file('uploads/' + name, mimetype='image')


@app.route('/static/img/<name>')
def get_static_file(name):
    return send_file('static/img/' + name, mimetype='image')


@app.route('/del_event/<event>')
def del_event(event):
    if not request.cookies.get('session_') == 'sucs':
        return redirect(url_for('login'))

    db.session.query(Events).filter(Events.id == int(event)).delete()
    db.session.commit()

    return redirect(url_for('add_event'))


@app.route('/inst/')
def inst():
    if not request.cookies.get('session_') == 'sucs':
        return redirect(url_for('login'))

    inst_posts = InstaPosts.query.all()
    return render_template('dashboard/insta.html', posts=inst_posts)


@app.route('/scrape_insta/')
def scrape_insta():
    if not request.cookies.get('session_') == 'sucs':
        return redirect(url_for('login'))

    parser = InstaParser(cookiess)
    hub_id = parser.get_profil_id('ihub_khm')
    posts = parser.get_tagged_posts(hub_id)
    for post in posts:
        query = InstaPosts(
            post_link='https://www.instagram.com/p/' +
            post['node']['shortcode'],      # link
            # post['node']['taken_at_timestamp'],  # published time
            # owner username
            owner_username=post['node']['owner']['username'],
            # description
            description=post['node']['edge_media_to_caption']['edges'][0]['node']['text'],
            img_link=post['node']['display_url'],  # photo link
            # cooments count
            cooments_count=post['node']['edge_media_to_comment']['count'],
            # likes count
            likes_count=post['node']['edge_liked_by']['count'],
        )
        db.session.add(query)
        db.session.commit()

    return redirect(url_for('inst'))


@ app.route('/del_inst_post/<post>')
def del_inst_post(post):
    if not request.cookies.get('session_') == 'sucs':
        return redirect(url_for('login'))

    db.session.query(InstaPosts).filter(InstaPosts.id == int(post)).delete()
    db.session.commit()

    return redirect(url_for('inst'))


@ app.route('/')
def index():
    ivents = InstaPosts.query.all()
    return render_template('index.html', ivents=ivents)  # , posts=posts


@ app.route('/calendar/')
def calendar():
    # currwnt_month = datetime.now().strftime("%m")
    # conn = engine.connect()
    # r = select(Events)
    # r = db.session.execute(r)
    ivents = Events.query.all()

    return render_template('calendar.html', ivents=ivents)



# if __name__ == '__main__':
app.run(debug=True)
