from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

class Crawler():
   

    def __init__(self, webdriver_name="PhantomJS"):
        if webdriver_name == "PhantomJS":
            self.browser = webdriver.PhantomJS(executable_path = './webdriver/phantomjs.exe')
            
        elif webdriver_name == "Edge":
            edge_service = Service(executable_path='./webdriver/msedgedriver.exe')
            edge_options = Options()
            self.browser = webdriver.Edge(service=edge_service, options=edge_options)
            
        elif webdriver_name == "Firefox":
            self.browser = webdriver.Firefox(executable_path='./webdriver/geckodriver.exe')
            
        else:
            print("Error : Unknown webdriver name")

        self.product_group_name = ''
        self.wait_time = 0.5
        self.file_number = 0


    def download(self, root_url,k):
        self.get_html(root_url)
        self.browser.maximize_window()
        for i in range(0, k):

            start= i*1000+1
            end = (i+1)*1000
            if end <=1000:
                minEnd = end
            else:
                minEnd= start+999
            
            
            sleep(3)
            self.browser.find_element(By.CSS_SELECTOR, '#snRecListTop > app-export-menu > div > button').send_keys(Keys.ENTER) 
            try:
                sleep(2)

                self.browser.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div/div/div/div[8]/button').click() 
            except Exception:
                try:
                    self.browser.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div/div/div[8]/button').click()
                except Exception:
                    try:
                        self.browser.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div/div/div[8]/button').click()
                    except Exception:
                        try: 
                            self.browser.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div/div/div[8]/button').click()
                        except Exception:
                            pass
                pass

            sleep(1)
            self.browser.find_element(By.XPATH, '/html/body/app-wos/main/div/div/div[2]/div/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/form/div/fieldset/mat-radio-group/div[3]/mat-radio-button/label/span[1]').click() # 0 ~1000 선택
            self.browser.find_element(By.XPATH, '/html/body/app-wos/main/div/div/div[2]/div/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/form/div/fieldset/mat-radio-group/div[3]/mat-form-field[1]/div/div[1]/div[3]/input').clear() #
            self.browser.find_element(By.XPATH, '/html/body/app-wos/main/div/div/div[2]/div/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/form/div/fieldset/mat-radio-group/div[3]/mat-form-field[1]/div/div[1]/div[3]/input').send_keys(str(start))
            self.browser.find_element(By.XPATH, '/html/body/app-wos/main/div/div/div[2]/div/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/form/div/fieldset/mat-radio-group/div[3]/mat-form-field[2]/div/div[1]/div[3]/input').clear()
            self.browser.find_element(By.XPATH, '/html/body/app-wos/main/div/div/div[2]/div/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/form/div/fieldset/mat-radio-group/div[3]/mat-form-field[2]/div/div[1]/div[3]/input').send_keys(str(minEnd))
            self.browser.find_element(By.CSS_SELECTOR,'body > app-wos > main > div > div > div.holder > div > div > div.held > app-input-route:nth-child(3) > app-export-overlay > div > div.window > div.window-content.ng-star-inserted > app-export-out-details > div > div.window-content.ng-star-inserted > form > div > div.ng-star-inserted > wos-select > button').send_keys(Keys.ENTER)        
            sleep(2)
            self.browser.find_element(By.XPATH, '/html/body/app-wos/main/div/div/div[2]/div/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/form/div/div[1]/wos-select/div/div/div/div[3]').click()
            sleep(2)
            self.browser.find_element(By.XPATH, '/html/body/app-wos/main/div/div/div[2]/div/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/form/div/div[2]/button[1]').click()
            sleep(8)
            


                


             

            

        
        
        
if __name__ == "__main__":
    crawler = Crawler("Edge")
    url = "" 
    crawler.download(url, 5)
