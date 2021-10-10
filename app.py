from selenium import webdriver
from time import sleep

class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('https://www.tinder.com')
        self.__startLoop = False


    @property
    def startLoop(self):
        return self.__startLoop
    
    @startLoop.setter
    def startLoop(self, value):
        self.__startLoop = value

    def login_tinder(self):
        sleep(2)
        login_btn = self.driver.find_element_by_xpath('//*[@id="q-1826079426"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login_btn.click()
        
        sleep(2)
        tel_btn = self.driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div[1]/div/div[3]/span/div[3]/button')
        tel_btn.click()
        
        self.wait_input()

    def wait_input(self):
        input()
        sleep(2)
        self.notifications()

    def notifications(self):
        location_btn = self.driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div/div/div[3]/button[1]') 
        location_btn.click()

        sleep(2)
        notification_btn = self.driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div/div/div[3]/button[2]') 
        notification_btn.click()

        sleep(1)
        cookie_btn = self.driver.find_element_by_xpath('//*[@id="q-1826079426"]/div/div[2]/div/div/div[1]/button') 
        cookie_btn.click()

        sleep(2)
        self.startLoop = True


    def handle_like(self):
        try:
            like = self.driver.find_element_by_xpath('//div[@class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc($c-like-green)"]//button')
            sleep(2)
            like.click()
        except:
            try:
                if self.driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div[2]/button[2]') is not None:
                    self.driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div[2]/button[2]').click()
                elif self.driver.find_element_by_xpath('//h3[text()="Acabaram suas curtidas!"]') is not None:
                    self.startLoop = False
                    print("Fechando o código!")
                    self.driver.close()
            except:
                pass
        '''finally:
            try:
                #não add tela inicial
                
                input()
                #deu match
            except Exception as e:
                pass
            finally:
                sleep(2)
                like.click()'''



if __name__ == "__main__":
    bot = TinderBot()
    bot.login_tinder()
    while bot.startLoop:
        bot.handle_like()