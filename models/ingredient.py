import sqlite3
from db import db

class IngredientModel(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    amount = db.Column(db.Float(precision=2))
    measurement = db.Column(db.String(20))

    recipe_id = db.Column(db.Integer,db.ForeignKey('recipes.id'))
    recipe = db.relationship('RecipeModel')

    def __init__(self,name,amount,measurement,recipe_id):
        self.name = name
        self.amount = amount
        self.measurement = measurement
        self.recipe_id = recipe_id

    def json(self):
        return {
            'id' : self.id,
            'name': self.name,
            'amount' : self.amount,
            'measurement' = self.measurement
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def find_by_id(cls , _id):
        return cls.query.filter_by(id=_id).first()

    def find_by_recipe(cls, recipe_id):
        return cls.query.filter_by(recipe_id=recipe_id)