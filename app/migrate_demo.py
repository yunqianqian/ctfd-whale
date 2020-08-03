from utils import config,constant
from api.db_api import DBUtils
from api.docker_api import  ControlUtil
from flask import Flask, request
from utils.exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/image', methods = ['GET','POST','DELETE'])
def image():
    if request.method == "GET":
        res = ControlUtil.list_image()
    elif request.method == "POST":
        try:
            path = request.json.get("path")
        except Exception as e:
            print e
            return {"status": int(constant.ERROR_RETURN_VALUE),
                    "error": "Passing parameter exception!"}
        res = ControlUtil.upload_image(path)
    else:
        id = request.json.get("id")
        res = ControlUtil.delete_image(id)
    return res

@app.route('/challenge',methods = ['GET','POST','DELETE'])
def challenge():
    if request.method =="GET":
        res = ControlUtil.list_challenge()
    elif request.method == "POST":
        try:
            memory = request.json.get("memory")
            cpu = request.json.get("cpu")
            image_id = request.json.get("imageId")
            type = request.json.get("type")
            port = request.json.get("port")
            res = ControlUtil.add_new_challenge(image, port, memory, cpu, type, image_id)
        except Exception as e:
            return {"status": int(constant.ERROR_RETURN_VALUE),
                "error": "Passing parameter exception!"}
    else:
        pass
    return res

if __name__ == '__main__':
    app.run(debug=True)