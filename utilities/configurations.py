import configparser
from webbrowser import Error

import pymysql

def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


connect_config = {
    'host':getConfig()['SQL']['host'],
    'database':getConfig()['SQL']['database1'],
    'user':getConfig()['SQL']['user'],
    'password':getConfig()['SQL']['password']
}


def getConnection():
    conn = pymysql.connect(**connect_config)
    return conn
    # try:
    #     conn = pymysql.connect(**connect_config)
    #     if conn.open() == True:
    #         print('Connection Successful')
    #         return conn
    # except Error as e:
    #     print(e)






