import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import numpy as np

# Conversor de medidas de metros em centimentros
class ConversorMetrosCent():

    def __init__(self):
            logger.debug(mensagens.INICIO_LOAD_MODEL)
            self.load_model()

    def load_model(self):

            logger.debug(mensagens.FIM_LOAD_MODEL)

    

    def executar_conv(self, value):
        response = {}

        logger.debug(mensagens.INICIO_CONVERSAO)
        start_time = time.time()

        response_predicts = self.buscar_predicao(value['valorM'])

        logger.debug(mensagens.FIM_CONVERSAO)
        logger.debug(f"Fim de todas as predições em {time.time()-start_time}")
        response = {
                    "Resultado da conversao": response_predicts}
        return response
       

    def buscar_predicao(self, valorM):
    
        logger.debug('Iniciando a conversão...')

        if valorM >= 1:
            response = valorM * 100
        else: 
            response = 'Digite a medida em metrôs'

        print(response)

        return response

        