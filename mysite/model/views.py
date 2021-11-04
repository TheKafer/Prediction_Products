from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import keras
import json

dic = {
    0: 'PC',
    1: 'T-Shirt',
    2: 'apple seeds',
    3: 'bikini',
    4: 'carrot seeds',
    5: 'cases',
    6: 'cement',
    7: 'charger smartphone',
    8: 'circular saw',
    9: 'clove',
    10: 'dirt',
    11: 'drill',
    12: 'fertilizer',
    13: 'flower',
    14: 'gloves',
    15: 'hammer',
    16: 'hat',
    17: 'headphones',
    18: 'onion seeds',
    19: 'paste',
    20: 'redmi 7',
    21: 'redmi 8',
    22: 'redmi 9',
    23: 'redmi note 7',
    24: 'redmi note 8',
    25: 'redmi note 9',
    26: 'redmie note 9s',
    27: 'rope',
    28: 'saw',
    29: 'scarf',
    30: 'screw',
    31: 'selfie stick',
    32: 'shoes',
    33: 'shovel',
    34: 'skirt',
    35: 'socks',
    36: 'underwear'
}


@csrf_exempt
def getPrediction(request):
    model = keras.models.load_model('./model/prediction/' + 'REC_MODEL') # Cargar modelo
    model.load_weights('./model/prediction/' + 'REC_MODEL.h5') # Cargar pesos
    json_data = json.loads(request.body)
    number = round(model.predict([json_data['products']])[0][0])
    data = {
        'product': dic[number]
    }
    return JsonResponse(data)
