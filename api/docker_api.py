import os
from base_class import docker_class
from base_class.db_class import Image,Container
from  db_api import DBUtils
from utils import constant

class ControlUtil:
    @staticmethod
    def add_container(image_id, user_id, flag, port):
        # change db status
        res = DBUtils.change_status_container(user_id)
        # startup container
        docker_client = docker_class.DockerUtils()
        res = docker_client.add_service(user_id, image_id, container_name, flag)
        if res == constant.SUCESS_RETURN_VALUE:
            # sucess: insert db
            DBUtils.create_new_container(image_id, user_id, name, flag, port)
            res = constant.SUCESS_RETURN_VALUE   
        else:
            res = constant.ERROR_RETURN_VALUE

        # failed
        
        # frp transmit
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
        except Exception as e:
            res = constant.ERROR_RETURN_VALUE
        return {"status":res}


    @staticmethod
    def del_container():
        pass

    @staticmethod
    def list_container():
        pass
    @staticmethod
    def restart_container():
        pass
    @staticmethod
    def rename_container():
        pass

def upload_image():
    pass

def del_image():
    pass

def list_image():
    pass

