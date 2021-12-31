from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'valorM': fields.List(fields.Integer(), required=True, description= "Valor em metros")})
