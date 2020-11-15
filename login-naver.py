import os.path
from selenium import webdriver


class login():

    def __init__(self):
        self.is_logined = False
        self.driver = None

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument('window-size=1920x1080')
        self.options.add_argument("disable-gpu")

    def execute_login_process(self):
        user_id = input('ID: ')
        user_pw = input('PW: ')
        print('Please wait...')
        self.driver = webdriver.Chrome(os.path.abspath(
            'chromedriver'), chrome_options=self.options)
        self.driver.implicitly_wait(5)

        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys(user_id)
        self.driver.find_element_by_name('pw').send_keys(user_pw)
        print('processing...')
        self.driver.find_element_by_xpath(
            '//*[@id="frmNIDLogin"]/fieldset/input').click()

        try:
            self.driver.find_element_by_id('err_common')
        except:
            self.is_logined = True
            try:
                self.driver.find_element_by_xpath('//*[@id="phone_value"]')
            except:
                pass
            else:
                print('It seems that you are trying to login in a foreign country.\nWe need your telephone number to verify your identification')
                tel_num = input('Telephone number: ')
                print('Please wait...')
                self.driver.find_element_by_xpath(
                    '//*[@id="phone_value"]').send_keys(tel_num)
                self.driver.find_element_by_xpath(
                    '//*[@id="frmNIDLogin"]/fieldset/span/input').click()
                print('Processing...')
                try:
                    self.driver.find_element_by_id('error_common')
                except:
                    pass
                else:
                    print('Verification fail')
                    self.is_logined = False
        else:
            self.is_logined = False

    if self.is_logined:
        print("Login success!")
    else:
        print("Login has failed")

        return self.is_logined

    def close_login_session(self):
        if self.driver != None:
            self.driver.quit()
            return True
        else:
            return False
