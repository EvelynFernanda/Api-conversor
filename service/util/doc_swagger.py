from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'valorM': fields.List(fields.Float(), required=True, description= "Valor em metros")})
