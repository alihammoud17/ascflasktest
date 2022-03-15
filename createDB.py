import imp
from api import db, TextModel

db.create_all()

firstText = TextModel(text="مرحبا يل عالم")
secondText = TextModel(text="اكل الولد التفاحة")

db.session.add(firstText)
db.session.add(secondText)
db.session.commit()
