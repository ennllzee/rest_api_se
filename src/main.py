#!/usr/bin/sanicAPI python3

from sanic import Sanic
import os
from sanic.response import text
from api.v1.BlueprintQuestion.blueprintRoute import bp_question
from api.v1.BlueprintUser.blueprintRoute import bp_users
from api.v1.BlueprintHistory.blueprintRoute import bp_history

from sanic_cors import CORS
import socket

app = Sanic('daily_challenge')
app.blueprint(bp_question)
app.blueprint(bp_users)
app.blueprint(bp_history)
CORS(app)

@app.route("/")
async def test(request):
    return text(str(os.getpid()))

if __name__ == "__main__":
    # ssl = {'cert': "src/ert.pem", 'key': "src/key.pem"}
    host = '0.0.0.0'
    port = 8000
    
    # serv_coro = app.create_server(host=host, port=port, return_asyncio_server=True)
    # import asyncio
    # loop = asyncio.get_event_loop()
    # serv_task = asyncio.ensure_future(serv_coro, loop=loop)
    # server = loop.run_until_complete(serv_task)
    # server.after_start()
    # try:
    #     loop.run_forever()
    # except KeyboardInterrupt as e:
    #     loop.stop()
    # finally:
    #     server.before_stop()

    #     # Wait for server to close
    #     close_task = server.close()
    #     loop.run_until_complete(close_task)

    #     # Complete all tasks on the loop
    #     for connection in server.connections:
    #         connection.close_if_idle()
    #     server.after_stop()
    try:
        # app.run(host=host, port=port, auto_reload=True, access_log=False)
        app.run(host=host, port=port, auto_reload=True)
        raise Exception('Stop server')
    except (Exception, KeyboardInterrupt, SystemExit) as e:
        print(e)