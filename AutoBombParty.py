from collections import defaultdict
from requests import get
from random import choice

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def get_words():
    try:
        print('. Carregando dicionário...')
        words = get('https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt').text.split('\n')
    except:
        input('└───> Erro! Sem conexão com a internet. O script foi encerrado.')
        exit()

    dic = defaultdict(list)
    for word in words:
        if word and len(word) < 8:
            dic[word[0]].append(word)
    return dic

words_list = get_words()

class Driver():
    def __init__(self):
        super().__init__()
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--log-level=3')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://jklm.fun')
        self.timeout = 60
        self.wait = WebDriverWait(self.driver, self.timeout)
        
        print('├─> Aguardando sala...')
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[4]/div[1]/iframe')))
        except:
            print(f'└───> Nenhuma sala foi encontrada nos últimos {self.timeout} segundos. O script foi encerrado.')
            self.driver.quit()

        else:
            print('└──> Jogo detectado')
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div[1]/iframe'))

            while 1:
                try:
                    self.wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/form/input')))
                    
                    self.syl = self.driver.find_element(By.CLASS_NAME, 'syllable').text.lower()

                    self.box = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[2]/form/input')
                    self.box.click()
                    
                    self.box.send_keys(choice(self.create_list(self, self.syl, words_list)), Keys.RETURN)
                except Exception as err:
                    pass
                    #print(err)

    def create_list(self, obj, user_input, dic):
        words = []
        for key in dic:
            words.extend(dic[key])
        return [i for i in words if user_input in i.lower()]
Driver()
