#!/usr/bin/sanicAPI python3

from sanic import Blueprint
from sanic.response import json
# from ..loggingFile import Logger
from ..configure import config
from ..rethinkdbApi import rethinkApi
from .rethinkdb import api

bp_question = Blueprint('question_v1', url_prefix='/api/question', version="v1")
    
@bp_question.route('/', methods=["GET", "POST"])
async def getAllQuestion(request):
    if request.method == "GET":
        params = request.args
        if params.get('limit', None):
            res = api.getLimitRandomQuestion(int(params['limit'][0]))
        else:
            res = api.getAllQuestion()
        return json({config.responseKey: res})
    elif request.method == "POST":
        res = api.insetQuestion(request.json)
        return json({config.responseKey: res})
    
@bp_question.route('/test', methods=["GET", "POST", "PUT", "DELETE"])
async def test(request):
    print(request.method)
    return json({config.responseKey: 200})