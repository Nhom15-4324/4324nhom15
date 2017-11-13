#!/usr/bin/python
import mysql.connector
import config

def create_mysql_connection():
    try:
        db = mysql.connector.connect(host=config.mysql_host,    # your host, usually localhost
                         user=config.mysql_user,         # your username
                         passwd=config.mysql_pass,  # your password
                         db=config.mysql_db)        # name of the data base
        return db
    except:
        return None
    
