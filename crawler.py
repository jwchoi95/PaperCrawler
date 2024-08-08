from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from time import sleep
import random



class Crawler():
   

    def __init__(self):
        
        edge_service = Service(executable_path='./webdriver/msedgedriver.exe')
        edge_options = Options()
        self.browser = webdriver.Edge(service=edge_service, options=edge_options)
        self.product_group_name = ''
        self.wait_time = 0.5
        self.file_number = 0
        
 

    def run(self, root_url):
        self.browser.get("https://doi.org/"+root_url)
        sleep(random.uniform(15,20))
        
        try:
            element = self.browser.find_element(By.XPATH, '//*[@id="mathjax-container"]/div[2]/article')
            element_html = element.get_attribute("outerHTML")
            with open(f"{root_url}.html", "w", encoding="utf-8") as f:
                f.write(element_html)   
            
        except Exception as e:
            return root_url  
        if self.browser: 
            self.browser.quit()


        
   
      
        
if __name__ == "__main__":
    
    doi = '10.1016/j.nanoen.2019.104333'
    crawler = Crawler()
    crawler.run(doi)





