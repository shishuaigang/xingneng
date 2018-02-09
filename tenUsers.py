import http.cookiejar
import json
import time
import urllib.parse
import urllib.request
from multiprocessing import Pool

import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from function_set.readINI import Readini
from page import home

CONFIG = Readini().ini_data()


def getCookie():
    c = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(c))
    URL = CONFIG['conf']['URL'] + '/API/Account/Login'
    data = {
        'APIVersion': CONFIG['conf']['APIVersion'],
        'phonenumber': CONFIG['conf']['ACCOUNT'],
        'password': CONFIG['conf']['PASSWORD'],
        'rememberme': 'True'
    }
    post_info = urllib.parse.urlencode(data).encode(encoding='UTF-8')
    request = urllib.request.Request(URL, post_info)
    html = opener.open(request).read()
    return c


def run(func_name):
    eval(func_name)()


def func1():
    params = {
        'APIVersion': CONFIG['conf']['APIVersion']
    }
    while True:
        re = requests.post(CONFIG['conf']['URL'] + '/UAPI/WorkingBill/RecordSearch', data=params, cookies=getCookie())
        print(re.status_code, json.loads(re.content)['status'])


def func2_outter():
    def func2():
        FF1 = webdriver.Firefox(executable_path=CONFIG['conf']['DRIVER_PATH'])
        FF1.get(CONFIG['conf']['URL'])
        FF1.find_element(*home.phone_number).send_keys(CONFIG['conf']['ACCOUNT'])
        FF1.find_element(*home.password).send_keys(CONFIG['conf']['PASSWORD'])
        FF1.find_element(*home.login_btn).click()
        WebDriverWait(FF1, 20, 0.1).until(ec.visibility_of_element_located(home.Workbill_Config))
        FF1.find_element(*home.Workbill_Config).click()
        WebDriverWait(FF1, 20, 0.1).until(ec.visibility_of_element_located(home.Workbill_Guanli))
        FF1.find_element(*home.Workbill_Guanli).click()
        WebDriverWait(FF1, 20, 0.1).until(ec.visibility_of_element_located(home.ByCondition))
        FF1.find_element(*home.ByCondition).click()

        def func2_inner():
            time.sleep(0.2)
            FF1.find_element(*home.searchButton).click()

        while True:
            func2_inner()

    func2()


def func3():
    params = {
        'APIVersion': CONFIG['conf']['APIVersion'],
        'begintime': '2017-1-1 10:00:01',
        'edntime': '2018-2-1 10:00:01',
        'itemtype': '00000000-0000-0000-0000-000000000000',
        'regionids': '',
        'alarmtype': '0',
        'keyword': ''
    }
    while True:
        re = requests.post(CONFIG['conf']['URL'] + '/UAPI/CoreData/DataItemRecordSearch', data=params,
                           cookies=getCookie())
        print(re.status_code, json.loads(re.content)['status'])


def func4_outter():
    def func4():
        FF2 = webdriver.Firefox(executable_path=CONFIG['conf']['DRIVER_PATH'])

        def func4_inner():

            FF2.get(CONFIG['conf']['URL'])
            FF2.find_element(*home.phone_number).send_keys(CONFIG['conf']['ACCOUNT'])
            FF2.find_element(*home.password).send_keys(CONFIG['conf']['PASSWORD'])
            FF2.find_element(*home.login_btn).click()
            try:
                WebDriverWait(FF2, 20, 0.1).until(ec.visibility_of_element_located(home.login_success_flag))
            except Exception:
                print("未登录成功")

        func4_inner()
        FF2.quit()

    while True:
        func4()


def func5():
    params = {
        'APIVersion': CONFIG['conf']['APIVersion'],
        'begintime': '2017-05-13',
        'edntime': '2018-08-13',
        'regionids': '',
        'keyword': ''
    }
    while True:
        re = requests.post(CONFIG['conf']['URL'] + '/UAPI/NewTask/Search', data=params, cookies=getCookie())
        print(re.status_code, json.loads(re.content)['status'])


def func6():
    params = {
        'APIVersion': CONFIG['conf']['APIVersion']
    }
    while True:
        re = requests.post(CONFIG['conf']['URL'] + '/UAPI/PotentialTrouble/ManualTroubleSearch', data=params,
                           cookies=getCookie())
        print(re.status_code, json.loads(re.content)['status'])


def func7():
    params = {
        'APIVersion': CONFIG['conf']['APIVersion']
    }
    while True:
        requests.post(CONFIG['conf']['URL'] + '/UAPI/PotentialTrouble/ProjectRecordSearch', data=params,
                      cookies=getCookie())


def func8():
    params = {
        'APIVersion': CONFIG['conf']['APIVersion']
    }
    while True:
        requests.post(CONFIG['conf']['URL'] + '/UAPI/PotentialTrouble/TroubleCollectionSearch', data=params,
                      cookies=getCookie())


def func9():
    params = {
        'APIVersion': CONFIG['conf']['APIVersion']
    }
    while True:
        requests.post(CONFIG['conf']['URL'] + '/UAPI/Knowledge/WebPointSearch', data=params,
                      cookies=getCookie())


def func10():
    params = {
        'APIVersion': CONFIG['conf']['APIVersion']
    }
    while True:
        requests.post(CONFIG['conf']['URL'] + '/UAPI/WorkingBill/RecordCheckSearch', data=params,
                      cookies=getCookie())


if __name__ == '__main__':
    # func5()
    proc = {'func1', 'func2_outter', 'func3', 'func4_outter', 'func5', 'func6', 'func7', 'func8', 'func9', 'func10'}
    # print(type(proc))
    pool = Pool(10)
    for i in proc:
        pool.apply_async(run, (i,))
    pool.close()
    pool.join()
