from utils import config,constant
from api.db_api import DBUtils
from api.docker_api import  ControlUtil
from flask import Flask, request
from utils.exts import db
from api.redis_utils import Redis
import json
import time

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.config['REDIS_HOST'] = "127.0.0.1"
app.config['REDIS_PORT'] = 6379
app.config['REDIS_DB'] = 0
app.config['REDIS_EXPIRE'] = 60
app.secret_key = 'limit'

@app.route('/image', methods = ['GET','POST','DELETE'])
def image():
    if request.method == "GET":
        res = ControlUtil.list_image()
    elif request.method == "POST":
        try:
            path = request.json.get("path")
        except Exception as e:
            return {"status": int(constant.ERROR_RETURN_VALUE),
                    "error": "Passing parameter exception!"}
        res = ControlUtil.upload_image(path)
    else:
        try:
            id = request.json.get("id")
        except Exception as e:
            return {"status": int(constant.ERROR_RETURN_VALUE),
                    "error": "Passing parameter exception!"}
        res = ControlUtil.delete_image(id)          
    return res

@app.route('/challenge',methods = ['GET','POST','DELETE'])
def challenge():
    if request.method == "GET":
        res = DBUtils.list_challenge()
        res = {"status": constant.SUCESS_RETURN_VALUE,"data": res}
    elif request.method == "POST":
        try:
            memory = request.json.get("memory")
            cpu = request.json.get("cpu")
            image_id = request.json.get("imageId")
            redirect_type = request.json.get("redirect_type")
            port = request.json.get("port")
        except Exception as e:
            return {"status": int(constant.ERROR_RETURN_VALUE),
                "error": "Passing parameter exception!"}
        res = DBUtils.add_new_challenge(port, memory, cpu, redirect_type, image_id)
        res = {"status": constant.SUCESS_RETURN_VALUE}
    else:
        id = request.json.get("id")
        DBUtils.delete_challenge(id)
        res = {"status": constant.SUCESS_RETURN_VALUE}
    return res

@app.route('/container',methods = ['POST'])
def container():
    try:
        challenge_id = request.json.get("challengeId")
        user_id = request.json.get("userId")
        flag = request.json.get("flag")
    except Exception as e:
        return {"status": int(constant.ERROR_PARA),
            "error": "Passing parameter exception!"}
    redis_util = Redis(app=app, user_id=user_id)
    if not redis_util.acquire_lock():
        return json.dumps({'success': False, 'msg': 'Request Too Fast!'})
    port = redis_util.get_available_port()       
    res = ControlUtil.add_container(app, challenge_id, user_id, flag, port)
    redis_util.release_lock()
    return res

@app.route('/settings', methods = ['GET'])
def redis():
   redis = Redis(app)
   redis.init_redis_port_sets()
   return {"status": 0}
    
if __name__ == '__main__':
    app.run(debug=True)