from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:96Ladybug@localhost/mydatabase'
#db = SQLAlchemy(app)


engine = create_engine('mysql://root:96Ladybug5@localhost:5000/PeerReview')
#dialect_driver://username:password@host:port/database


from views import *
