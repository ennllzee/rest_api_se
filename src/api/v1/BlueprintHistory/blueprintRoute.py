
from sanic import Blueprint
from sanic.response import json
# from ..loggingFile import Logger
from ..configure import config
from .rethinkdb import api

bp_history = Blueprint('history_v1', url_prefix='/api/history', version="v1")
    
@bp_history.route('/', methods=["GET", "POST"])
async def history(request):
    if request.method == "GET":
        res = api.getAllHistoryGroupTime(request.headers['userId'])
        return json({config.response_key: res})
    elif request.method == "POST":
        res = api.insertHistory(request.json)
        return json({config.response_key: res})