from flask import Flask
import pymysql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/letsupdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer(),primary_key = True, nullable = False )
    name = db.Column(db.String(20), nullable = False )
    age = db.Column(db.Integer(), nullable = False )
    sex = db.Column(db.String(8),nullable = False )

class Programs(db.Model):
    id = db.Column(db.Integer(), primary_key = True, nullable = False)
    name = db.Column(db.String(20), nullable = False )
    student = db.Column(db.Integer(), nullable = False )
    time = db.Column(db.String(25), nullable = False )

db.create_all()

# student1 = Students(id=1,name='harsh',age=19,sex='male')
# student2 = Students(id=2,name='srishti',age=20,sex='male') 
# student3 = Students(id=3,name='kiran',age=22,sex='male') 
# student4 = Students(id=4,name='nilesh',age=24,sex='male')                 

# program1 = Programs(id=1,name='python-django',student=32,time='6 months')
# program2 = Programs(id=2,name='Ai-Ml',student=22,time='9 months')
# program3 = Programs(id=3,name='web-dev',student=56,time='6 months')

# db.session.add_all([student1, student2, student3, student4,program1,program2,program3])
# db.session.commit()

#all_programs = Programs.query.all()
# all_programs = Programs.query.all()
# for program in all_programs:
#     print(program.id, program.name, program.time, program.student)

# program = Programs.query.filter_by(name = 'python-django').first()
# print(program.id, program.name, program.time)


program = Programs.query.get(2)
print(program.time)
program.time = '3 months'
db.session.add(program)
db.session.commit()
program = Programs.query.get(2)
print(program.time)