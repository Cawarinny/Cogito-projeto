import json
import requests
import pickle
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def webScraping():
    try:
        with open('credentials.json', 'r') as arq:
            dadosPortifolio = json.load(arq)

        emailUser = dadosPortifolio['Email']
        passwordUser = dadosPortifolio['Password']

        # Em segundos
        sleep = 20

        # Url usados no processo
        url = 'https://br.investing.com'
        urlLogin = 'https://br.investing.com/login/'
        urlPortfolio = 'https://br.investing.com/portfolio'
        urlMajorIndices = 'https://br.investing.com/indices/major-indices'

        # Iniciando Browser
        option = Options()
        option.headless = True
        driver = webdriver.firefox.firefox_binary.FirefoxBinary(firefox_path='./geckodriver.exe')
        driver = webdriver.Firefox(options=option)

        # loga na Plataforma
        try:
            driver.get(url)
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                driver.add_cookie(cookie)
        
        except:
            driver.get(urlLogin)
            driver.implicitly_wait(sleep)
        
            driver.find_element_by_css_selector('#onetrust-accept-btn-handler').click()
            userLogin = driver.find_element_by_css_selector('#loginFormUser_email')
            userLogin.send_keys(emailUser)

            passwordLogin = driver.find_element_by_css_selector('#loginForm_password')
            passwordLogin.send_keys(passwordUser)

            driver.implicitly_wait(sleep)
            driver.find_element_by_css_selector('#signup > a').click()

            driver.implicitly_wait(sleep)
            pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

        # Pega os dados da Carteira
        driver.get(urlPortfolio)
        driver.implicitly_wait(sleep)  

        promiseTablePortfolio = driver.find_element_by_css_selector(".js-table-sortable")
        html_content = promiseTablePortfolio.get_attribute('outerHTML')

        soup = BeautifulSoup(html_content, 'html.parser')
        tablePortfolio = soup.find(name='table')

        df_full = pd.read_html(str(tablePortfolio))[0].head(5)
        df = df_full[['Nome', 'Var%']]
        df.columns = ['Indices', 'Var. %']

        portfolio = {}
        portfolio['Portfolio'] = df.to_dict()

        fp = open('portfolio.json', 'w', encoding='utf-8')
        js = json.dumps(portfolio, indent=4)
        fp.write(js)
        fp.close()

        # Pega os dados dos Principais Indices
        driver.get(urlMajorIndices)
        driver.implicitly_wait(sleep)  # Em segundos

        tableMajorIndices = driver.find_element_by_css_selector("table.datatable_table__2Qbdw:nth-child(1)")
        html_content = tableMajorIndices.get_attribute('outerHTML')

        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find(name='table')

        df_full = pd.read_html(str(table))[0].head(41)
        df = df_full[['Índice', 'Var. %']]
        df.columns = ['Indices', 'Var. %']

        majorIndices = {}
        majorIndices['majorIndices'] = df.to_dict()

        fp = open('majorIndices.json', 'w', encoding='utf-8')
        js = json.dumps(majorIndices, indent=4)
        fp.write(js)
        fp.close()

        driver.quit()
        return 'Success'

    except:
        driver.quit()
