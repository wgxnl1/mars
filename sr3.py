import datetime
from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

db_session.global_init("database/mars_explorer.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    jobs = Jobs()
    jobs.team_leader = 1
    jobs.job = 'deployment of residential modules 1 and 2'
    jobs.work_size = 15
    jobs.collaborators = '2,3'
    jobs.start_date = datetime.datetime.now()
    jobs.is_finished = False


    session = db_session.create_session()
    session.add(jobs)
    session.commit()
    app.run()


if __name__ == '__main__':
    main()