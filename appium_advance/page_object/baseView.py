class BaseView(object):
    def __init__(self,driver):
        self.driver=driver
    def find_element(self,*loc):
        return self.find_element(*loc)
