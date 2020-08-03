#coding:utf-8

from base_class.db_class  import Image, Container,Challenge
from utils.exts import db
import uuid

class DBUtils():
    @staticmethod
    def create_new_container(image_id, user_id, flag, port):
        id = str(uuid.uuid4())
        container = Container(id = id, user_id = user_id, image_id = image_id,
                              name = user_id + "-"+ id, flag=flag, port=port)
        db.session.add(container)
        db.session.commit()
        db.session.close()
        return str(uuid_code)

    @staticmethod
    def remove_container():
        q = db.session.query(Container)
        q = q.filter(Container.user_id == user_id)
        q.delete()
        db.session.commit()
        db.session.close()

    @staticmethod
    def rename_container():
        pass
    
    @staticmethod
    def get_current_containers(user_id):
        q = db.session.query(Container)
        q = q.filter(Container.user_id == user_id)
        records = q.all()
        if len(records) == 0:
            return None
        return records[0]

    @staticmethod
    def get_all_alive_container():
        q = db.session.query(Container)
        q = q.filter(Container.status == "0")
        records = q.all()
        if len(records) == 0:
            return None
        return records

    @staticmethod
    def change_status_container(user_id):
        q = db.session.query(Container)
        q = q.filter(Container.user_id == user_id, Container.status == 0)
        records = q.all()
        if len(records) == 1:
            ((q.all())[0]).status = 1
        elif len(records) > 1:
            # TODO: 如果多个增加时间处理
            pass
        else:
            pass
        db.session.commit()
        db.session.close()

    @staticmethod
    def add_new_image(name, image_id):
        id = str(uuid.uuid4())
        image = Image(id = id, name = name, image_id = image_id)
        db.session.add(image)
        db.session.commit()
        db.session.close()

    @staticmethod
    def remove_Image():
        q = db.session.query(Image)
        q = q.filter(Image.id == id)
        q.delete()
        db.session.commit()
        db.session.close()

    @staticmethod
    def get_image_name(id):
        q = db.session.query(Image)
        q = q.filter(Image.id == id)
        records = q.all()
        return (records[0]).name

    @staticmethod
    def add_new_challenge(port, memory, cpu, type, image_id):
        id = str(uuid.uuid4())
        challenge = Challenge(id = id, memory = memory, cpu = cpu, type = type, 
                              port = port,image_id = image_id)
        db.session.add(challenge)
        db.session.commit()
        db.session.close()

    @staticmethod
    def list_challenge():
        q = db.session.query(Challenge)
        return q.all()

    @staticmethod
    def delete_challenge(id):
        q = db.session.query(Challenge)
        q = q.filter(Challenge.id == id)
        q.delete()
        db.session.commit()
        db.session.close() 