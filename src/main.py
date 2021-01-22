#!/usr/bin/sanicAPI python3

from sanic import Sanic
import os
from sanic.response import text
from api.v1.BlueprintQuestion.blueprintRoute import bp_question
from api.v1.BlueprintUser.blueprintRoute import bp_users

from sanic_cors import CORS

app = Sanic('daily_challenge')
app.blueprint(bp_question)
app.blueprint(bp_users)
CORS(app)

@app.route("/")
async def test(request):
    return text(str(os.getpid()))

def main():
    host = "192.168.1.37"
    port = 8000
    try:
        # app.run(host=host, port=port, auto_reload=True, access_log=False)
        app.run(host=host, port=port, auto_reload=True)
        raise Exception('Stop server')
    except (Exception, KeyboardInterrupt, SystemExit) as e:
        print(e)
    app.run(workers=4)


if __name__ == "__main__":
    main()