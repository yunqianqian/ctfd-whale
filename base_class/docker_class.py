#!/usr/bin/python
# -*- coding: UTF-8 -*

import docker
from utils import util, constant

logger = util.init_log()

class DockerUtils(object):
    def __init__(self):
        try:
            self.client = docker.DockerClient(
                base_url=constant.DOCKER_BASE_URL)
        except Exception as e:
            self.client = None
            logger.error(
                "Fail to initialize Docker client, exception: {}".format(e))

    # TODO: add network, dns, cpu, memrory limit
    def add_service(self, user_id, image_name, container_name, flag, cpu, memory):
        try:
            self.client.services.create(image = image_name, name=container_name, env = {'FLAG': flag},
                                        resources = docker.types.Resources(
                                            mem_limit = util.convert_readable_text(memory),
                                            cpu_limit = int(cpu * 1e9)),
                                        networks = ["ctfd_frp_containers"],
                                        labels = {container_name: user_id},
                                        container_labels = {container_name: user_id},
                                        hostname = container_name)
            add_service_res = constant.SUCESS_RETURN_VALUE
        except Exception as e:
            logger.error(
                "Fail to startup container, exception: {}".format(e))
            add_service_res = constant.ERROR_RETURN_VALUE
        return add_service_res

    def del_service(self,container_name):
        services = self.client.services.list(filters={'label': container_name})
        #是否存在容器已经删掉，数据库数据还存在的情况？
        for s in services:
            s.remove()

    def get_service(self):
        result = {}
        list_service = self.client.services.list()
        for item in list_service:
            result[item.short_id] = item.name
        return result

    def get_container(self,container_name):
        res = self.client.containers.list(filters={'label': container_name})
        if res:
            return True
        return False


    def del_network(self):
        pass

    def list_image(self):
        images = []
        try:
            res = self.client.images.list()
            for item in res:
                if item.tags:
                    images.append(str((item.tags)[0]))
        except Exception as e:
            logger.error(
                "Fail to list images, exception: {}".format(e))
        return images


    def del_image(self,name):
        try:
            self.client.images.remove(name)
            res = constant.SUCESS_RETURN_VALUE
            print(res)
        except Exception as e:
            logger.error(
                "Fail to delete image, exception: {}".format(e))
            res = constant.ERROR_RETURN_VALUE
        return res
         
    def add_image(self, path):
        try:
            with open(path, 'rb') as f:
                content = f.read()
            res = self.client.images.load(content)
            res = res[0]
        except Exception as e:
            print e
            logger.error(
                "Fail to add image, exception: {}".format(e))
            res = constant.ERROR_UPLOAD_IMAGE
        return res