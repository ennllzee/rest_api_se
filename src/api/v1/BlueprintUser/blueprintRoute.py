#!/usr/bin/sanicAPI python3

from sanic import Blueprint
from sanic.response import json
# from ..loggingFile import Logger
from ..configure import config
from .rethinkdb import api

bp_users = Blueprint('users_v1', url_prefix='/api/users', version="v1")
    
@bp_users.route('/', methods=["GET", "POST"])
async def users(request):
    if request.method == "GET":
        res = {}
        return json({config.response_key: res})
    elif request.method == "POST":
        res = api.insertUser(request.json)
        return json({config.response_key: res})