import yaml
from appium import webdriver
import  logging
import logging.config
file=open(r"C:\Users\Henry\PycharmProjects\srapysusu\appium_advance\yaml\desired_caps.yaml","r")
data=yaml.load(file)

CON_LOG="../log/log.conf"
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
def appium_desired():

    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['app']=data['app']
    desired_caps['noReset']=data['noReset']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    logging.info("start app....")
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()