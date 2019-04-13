import sqlite3
from db import db

class RecipeModel(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    time = db.Column(db.String(50))
    calories = db.Column(db.Integer)
    directions = db.Column(db.String)

    ingredients = db.relationship('IngredientModel')

    def __init__(self,title,time,calories,directions,ingredients):
        self.title = title
        self.time = time
        self.calories = calories
        self.directions = directions
        self.ingredients = ingredients

    def json(self):
        return {
                'title': self.title,
                'time' : self.time,
                'calories': self.calories,
                'directions': self.directions
                'ingredients': [ingr.json() for ingr in self.ingredients]
               }
    
    def save_to_db(self):
        db.session.add(self);
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()