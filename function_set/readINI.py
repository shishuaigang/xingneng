import configparser
import os


class Readini:

    def __init__(self):
        self.inif = '/Users/shishuaigang/PycharmProjects/xingneng/function_set/config.ini'

    def ini_data(self):
        if os.path.exists(self.inif):
            cf = configparser.ConfigParser()
            cf.read(self.inif)
            return cf
        else:
            raise FileNotFoundError("文件不存在")


if __name__ == '__main__':
    tmp = Readini().ini_data()
    print(tmp['conf']['URL'])
