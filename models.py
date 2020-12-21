from app import db


class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)

    type = db.Column(db.String())
    img_path = db.Column(db.String())
    time = db.Column(db.DateTime)
    title = db.Column(db.String())
    description = db.Column(db.Text())

    def __repr__(self):
        return '<Event {}>'.format(self.title)


# class InstaPosts(db.Model):
#     __tablename__ = 'insta_posts'
#     id = db.Column(db.Integer, primary_key=True)
        
'''
class Users(db.Model):
    # Создаем таблицу пользователей
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    last_name = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    created = db.Column(db.DateTime, default=datetime.now())
    tasks = db.relationship('Tasks', backref='tasks')

    # Загоним данные в БД транзитом
    # def __init__(self, *args, **kwargs):
    #     super(Users, self).__init__(*args, **kwargs)

    def __init__(self, username, last_name, first_name):
        self.username = username
        self.last_name = last_name
        self.first_name = first_name

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Tasks(db.Model):
    # Создаем таблицу задач пользователей
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    name = db.Column(db.String(120), index=True)
    start = db.Column(db.Boolean, default=False)
    finish = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime, default=datetime.now())
    updated_on = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    # Загоним данные в БД транзитом
    def __init__(self, *args, **kwargs):
        super(Tasks, self).__init__(*args, **kwargs)

    # def __init__(self, name, last_name, first_name):
    #     self.name = name
    #     self.last_name = last_name
    #     self.first_name = first_name

    def __repr__(self):
        return '<Tasks {}>'.format(self.name)
'''
db.create_all()
