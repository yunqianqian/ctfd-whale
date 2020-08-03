from utils.exts import db
import datetime
from sqlalchemy import ForeignKey

class Image(db.Model):
    id = db.Column('ID',db.String(64), primary_key=True)
    name = db.Column('NAME',db.String(128),unique=True,nullable=False)
    image_id =   db.Column('IMAGEID',db.String(128),unique=True,nullable=False)
    create_time = db.Column('CREATETIME',db.DateTime, nullable=False, default=datetime.datetime.now())
    __tablename__ = "image"

class Challenge(db.Model):
    id = db.Column('CONID',db.String(64), primary_key=True)
    memory_limit = db.Column('MEMORY',db.String(32),nullable=True,default="128m")
    cpu_limit = db.Column('CPU',db.String(16),nullable=True,default="0.5")
    image_id = db.Column('IMAGEID',ForeignKey('image.IMAGEID'),unique=False,nullable=False)
    redirect_type = db.Column('TYPE',db.String(32),nullable=True,default="direct")
    port = db.Column('PORT',db.String(64),nullable=True)
    create_time = db.Column('CREATETIME',db.DateTime, nullable=False, default=datetime.datetime.now())
    __tablename__ = "challenge"

class Container(db.Model):
    id = db.Column('CONID',db.String(64), primary_key=True)
    image_id = db.Column('IMAGEID',ForeignKey('image.IMAGEID'),unique=False,nullable=False)
    user_id = db.Column('USERID',db.String(17), nullable=False)
    name = db.Column('CONNAME',db.String(128), nullable=False)
    flag = db.Column('FLAG',db.String(256), nullable=True)
    port = db.Column('PORT',db.String(64),nullable=True)
    create_time = db.Column('CREATETIME',db.DateTime, nullable=False, default=datetime.datetime.now())
    status = db.Column('STATUS', db.String(1), nullable=False,default = '0')
    __tablename__ = "container"

    
