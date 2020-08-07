#coding:utf-8

from base_class.db_class  import Image, Container,Challenge
from utils.exts import db
import uuid

class DBUtils():
    @staticmethod
    def add_new_container(id, image_id, user_id, container_name, flag, port):
        id = str(uuid.uuid4())
        container = Container(id = id, user_id = user_id, image_id = image_id,
                              name = container_name, flag=flag, port=port)
        db.session.add(container)
        db.session.commit()
        db.session.close()

    @staticmethod
    def delete_container(user_id):
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
        records = q.all()
        return records

    @staticmethod
    def get_all_container():
        q = db.session.query(Container)
        return q.all()

    @staticmethod
    def change_status_container(user_id):
        q = db.session.query(Container)
        q = q.filter(Container.user_id == user_id, Container.status == "0")
        records = q.all()
        if len(records) == 1:
            ((q.all())[0]).status = "1"
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
    def delete_image(id):
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
    def add_new_challenge(port, memory, cpu, redirect_type, image_id):
        id = str(uuid.uuid4())
        challenge = Challenge(id = id, memory = str(memory), cpu = float(cpu), 
                              redirect_type = str(redirect_type), 
                              port = str(port), image_id = str(image_id))
        db.session.add(challenge)
        db.session.commit()
        db.session.close()

    @staticmethod
    def list_challenge():
        q = db.session.query(Challenge)
        res = []
        for item in q.all():
            res.append(item.id)
        return res

    @staticmethod
    def delete_challenge(id):
        q = db.session.query(Challenge)
        q = q.filter(Challenge.id == id)
        q.delete()
        db.session.commit()
        db.session.close()

    @staticmethod
    def get_challenge(id):
        q = db.session.query(Challenge)
        q = q.filter(Challenge.id == id)
        records = q.all()
        db.session.commit()
        db.session.close()
        print (records[0]).image_id 
        return (records[0]).image_id