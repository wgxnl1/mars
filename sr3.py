import datetime
from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

db_session.global_init("database/mars_explorer.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    user.team_leader = 1
    user.job = 'deployment of residential modules 1 and 2'
    user.work_size = 15
    user.collaborators = '2,3'
    user.start_date = datetime.datetime.now
    user.is_finished = False


    session = db_session.create_session()
    session.add(user)
    session.commit()
    app.run()


if __name__ == '__main__':
    main()