from flask import (Flask, request, render_template,
                   redirect, url_for, make_response)


app = Flask(__name__, template_folder='templates')


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

    res = make_response(render_template('login.html', message=message))
    res.set_cookie('session', login_hash)
    return res


@app.route('/dashboard/', methods=['get'])
def dashboard():
    if not request.cookies.get('session') == 'sucs':
        return redirect(url_for('login'))

    return render_template('dashboard.html')



@app.route('/change_cookie/', methods=['POST'])
def change_cookie():
    cookie = request.form['change_cookie'].split(':')
    res = make_response(redirect('/dashboard'))
    res.set_cookie(*cookie)
    return res



@app.route('/dashboard/', methods=['get'])
def dashboard():
    if not request.cookies.get('session') == 'sucs':
        return redirect(url_for('login'))

    return render_template('dashboard.html')




@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
