#coding:utf-8

import os
import uuid
import time
from base_class import docker_class
from base_class.db_class import Image,Container,Challenge
from  db_api import DBUtils
from utils import constant
from redis_utils import Redis
from flask import session

class ControlUtil:
    @staticmethod
    def add_container(app, challenge_id, user_id, flag, port):
        # delete container
        id = str(uuid.uuid4())
        res = ControlUtil.delete_container(app, user_id)
        challenge = Challenge.query \
            .filter(Challenge.id == challenge_id) \
            .first_or_404()
        image_id = challenge.image_id
        cpu = challenge.cpu
        memory = challenge.memory
        image = Image.query \
            .filter(Image.image_id == image_id) \
            .first_or_404()
        image_name = image.name
        container_name = user_id + "-"+ id
        # startup container
        docker_client = docker_class.DockerUtils()
        docker_client.add_service(user_id, image_name, container_name, flag, cpu, memory)
        check_res = True
        #循环检测容器是否启动
        check_num = 15
        while check_num:
            print(check_num)
            time.sleep(2)
            check_res = docker_client.get_container(container_name)
            print(check_res)
            check_num = check_num - 1
            if check_res:
                break
        #没有启动container，则删掉service        
        if not check_res:
            docker_client.del_service(container_name)
            return{"status": int(constant.ERROR_STARTUP_CONTAINER),"err":"The container did not start properly"}
        DBUtils.add_new_container(id, image_id, user_id, container_name, flag, port)
        return {"status": constant.SUCESS_RETURN_VALUE}

    @staticmethod
    def delete_container(app, user_id):
        container = Container.query \
            .filter(Container.user_id == user_id).first()
        if container is None:
            return False
        #删除容器
        docker_client = docker_class.DockerUtils()
        docker_client.del_service(container.name)
        #删除数据库
        DBUtils.delete_container(user_id)
        #释放端口
        if container.port != 0:
            redis_util = Redis(app)
            redis_util.add_available_port(container.port)
        return True
    @staticmethod
    def list_container():
        res = DBUtils.get_all_container()
        return res
    @staticmethod
    def upload_image(path):
        res = constant.ERROR_RETURN_VALUE
        dirname,filename = os.path.split(path)
        print dirname
        print filename
        if filename[-4:] == ".tar":
            docker_client = docker_class.DockerUtils()
            res = docker_client.add_image(path)
            if res is not constant.ERROR_UPLOAD_IMAGE:
                name = res.tags
                image_id = (str(res.short_id))[7:]
                print image_id
                DBUtils.add_new_image(name, image_id)
                res = constant.SUCESS_RETURN_VALUE
        return {"status": res}

    @staticmethod
    def list_image():
        try:
            docker_client = docker_class.DockerUtils()
            images = docker_client.list_image()
            res = {"status": int(constant.SUCESS_RETURN_VALUE), "data":images}
        except Exception as e:
            res = {"status":constant.ERROR_RETURN_VALUE}
        return res
    @staticmethod
    def delete_image(id):
        try:
            name = DBUtils.get_image_name(id)
            print name
            docker_client = docker_class.DockerUtils()
            res = docker_client.del_image(name)
            if not res:
                DBUtils.delete_image(id)
        except Exception as e:
            print res
            res = constant.ERROR_RETURN_VALUE
        return {"status":res}

    @staticmethod
    def restart_container():
        pass
    @staticmethod
    def rename_container():
        pass


