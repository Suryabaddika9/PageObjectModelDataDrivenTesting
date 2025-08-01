from configparser import  ConfigParser


def read(category,key):
    config = ConfigParser()
    config.read("Configurations/config.ini")
    return config.get(category,key)
