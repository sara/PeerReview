from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

engine = create_engine("mysql://root:96Ladybug@localhost:8080/PeerReview")

con = engine.connect()
Base.prepare(engine, reflect=True)

Students = Base.classes.students
Reviews = Base.classes.reviews
Taken = Base.classes.taken
Skills = Base.classes.skills

session = Session(engine)


