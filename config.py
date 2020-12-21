import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-gue12ss'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=os.environ.get('POSTGRES_USER'),
    #                                                                                 pw=os.environ.get('POSTGRES_PW'),
    #                                                                                 url=os.environ.get('POSTGRES_URL'),
    #
    #                                                                                 db=os.environ.get('POSTGRES_DB'))
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or
                               'sqlite:///' + os.path.join(basedir, 'app.sqlite')) + '?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # silence the deprecation warning

    UPLOAD_FOLDER = 'uploads'
