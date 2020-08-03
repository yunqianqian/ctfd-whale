# -*- coding: utf-8 -*-

DIALECT   = "mysql"
DRIVER    = "pymysql"
USERNAME  = "root"
PASSWORD  = "123456"
HOST      = "192.168.159.130"
PORT      = "3306"
DATABASE  = "ctfd"

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,
                                                                       HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
