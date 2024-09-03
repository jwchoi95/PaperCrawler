from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from time import sleep
import random



class Crawler:
    def __init__(self):
        # Initialize Edge browser with the specified service and options
        edge_service = Service(executable_path='./webdriver/msedgedriver.exe')
        edge_options = Options()
        self.browser = webdriver.Edge(service=edge_service, options=edge_options)
        self.wait_time = 0.5
        self.file_number = 0

    def run(self, root_url, idx, publisher):
        # Construct the full URL and navigate to it
        doi_url = f"https://doi.org/{root_url}"
        self.browser.get(doi_url)

        # Random wait time between 15 to 20 seconds
        sleep(random.uniform(15, 20))
        
        # Reload the page and wait again
        self.browser.get(doi_url)
        sleep(random.uniform(10, 15))

        # Select the appropriate XPath based on the publisher and extract content
        xpath_dict = {
            'elsevier': '//*[@id="mathjax-container"]/div[2]/article',
            'acs': '//*[@id="pb-page-content"]/div/main/article/div[4]/div[1]',
            'wiley': '//*[@id="main-content"]/div[1]/div/section/div/div/div/div/article',
            'nature': '//*[@id="content"]/main',
            'science': '#//*[@id="main"]/div[1]/article',
            'rsc': '//*[@id="pagetop"]/main'
        }

        # Fetch element based on publisher's XPath
        xpath = xpath_dict.get(publisher, None)
        if xpath:
            try:
                element = self.browser.find_element(By.XPATH, xpath)
                element_html = element.get_attribute("outerHTML")
                
                # Write the HTML content to file
                file_path = f"new_parser/htmls/lmo/{publisher}/caption/lmo_{publisher}_{idx}.html"
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(element_html)
            except Exception as e:
                return idx
        else:
            print(f"No XPath configured for publisher: {publisher}")
            return idx

        return idx  # Return index even on success for uniform return type


if __name__ == "__main__":
    idx = 0
    doi = '10.1016/j.nanoen.2019.104333'
    publisher = 'elsevier'
    crawler = Crawler()
    crawler.run(doi, idx, publisher)

        
   
      
        





