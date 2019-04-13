from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.ingredient import IngredientModel

class Ingredient(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help='Ingredient must have a name'
    )

    parser.add_argument(
        'recipe_id',
        type=int,
        required=True,
        help='Ingredient must belong to a recipe'
    )

    @jwt_required
    def get(self,_id):
        ingredient = IngredientModel.find_by_id(_id)
        if ingredient:
            return ingredient.json()
        
        return {'message': 'Ingredient not found'}, 404

    @jwt_required
    def post(self):
        data = Ingredient.parser.parse_args()

        ingredient = IngredientModel(data['name'],data['amount'],data['measurement'],data['recipe_id'])
        try:
            ingredient.save_to_db()
        except:
            return {'message': 'Error occured when trying to save ingredient'}, 500
        
        return ingredient.json(), 201

    @jwt_required
    def delete(self,_id):
        ingredient = IngredientModel.find_by_id(_id)
        if ingredient:
            IngredientModel.delete_from_db()
            return {'message' : 'Ingredient deleted'}
        
        return {'message': 'Ingredient not found'}, 404

    @jwt_required
    def put(self,_id):
        data = Ingredient.parser.parse_args()
        ingredient = IngredientModel(data['name'],data['amount'],data['measurement'],data['store_id'])
        if IngredientModel.find_by_id(_id):
            ingredient.id = _id

        ingredient.save_to_db()
        return ingredient.json()



class IngredientList(Resource):

    @jwt_required
    def get(self,recipe_id):
        return {'items': [i.json() for i in IngredientModel.find_by_recipe(recipe_id)]}
    
    @jwt_required
    def get(self):
        return {'items': [i.json() for i in IngredientModel.query.all()]}
