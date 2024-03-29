import yaml
from appium import webdriver

file=open(r"C:\Users\Henry\PycharmProjects\srapysusu\appium_advance\yaml\desired_caps.yaml","r")
data=yaml.load(file)
desired_caps={}
desired_caps['platformName']=data['platformName']

desired_caps['platformVersion']=data['platformVersion']
desired_caps['deviceName']=data['deviceName']

desired_caps['app']=data['app']
desired_caps['noReset']=data['noReset']

desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']

driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)