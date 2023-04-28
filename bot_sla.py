from selenium import webdriver
import time, telebot
from selenium.webdriver.common.by import By
import cred

#подключаем бота в ТГ
TG_TOKEN = cred.TG_TOKEN
bot = telebot.TeleBot(TG_TOKEN)


driver = webdriver.Chrome()

login = cred.login
password = cred.password

driver.get(cred.url)

chat_id = '419765607'
# ввод логина и нажатие на кнопку далее

login_jira = driver.find_element('id', 'userNameInput')
login_jira.send_keys(login)
login_button = driver.find_element('id', 'nextButton')
login_button.click()

# ввод пароля и нажатие на кнопку вход

password_jira = driver.find_element('id', 'passwordInput')
password_jira.send_keys(password)
password_button = driver.find_element('id', 'submitButton')
password_button.click()

bot.send_message(chat_id, 'Подтверди двухфакторку')

time.sleep(15)

while True:
        sla = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[5]/div/div[1]/div/div[1]/div[2]/div/div['
                                            '5]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div['
                                            '16]/div/div[1]/span/div/div[2]/span').get_attribute(
            "innerHTML").splitlines()
        #print(sla)
        # если письмо есть (список не пустой) то
        if sla:
            # кликаем на папку SLA
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[5]/div/div[1]/div/div[1]/div[2]/div/div['
                                          '5]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div['
                                          '16]/div/div[1]/span/div').click()
            time.sleep(3)
            # кликаем на письмо
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[5]/div/div[1]/div/div[5]/div[3]/div/div['
                                          '2]/div/div/div/div[5]/div[4]/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div['
                                          '2]').click()
            # тема тикета
            time.sleep(7)

            tickit_theme = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[5]/div/div[1]/div/div[5]/div['
                                                         '3]/div/div[5]/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/div['
                                                         '1]/span').get_attribute('innerHTML').splitlines()[0]
            text = driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div/div[3]/div[5]/div/div[1]/div/div[5]/div[3]/div/div['
                                       '5]/div[ '
                                       '1]/div/div/div[3]/div[2]/div[2]/div[6]/div[1]/div/div/div[1]/div[1]/div[3]/div['
                                       '6]/div[3]/div[1]/div/div/div').get_attribute(
                'innerHTML').splitlines()

            # читаем письмо
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[5]/div/div[1]/div/div[5]/div[3]/div/div['
                                          '2]/div/div/div/div[5]/div[4]/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div['
                                          '2]/div[3]/div[3]/div/div/div[3]/button/span[1]').click()

            bot.send_message(chat_id, tickit_theme+'\n'.join(text).replace('<br>', '').replace
            ('<b>Ссылка на заявку:</b> <a href=\"', ''))
            #print(tickit_theme)
            #print(text)
            time.sleep(10)
            # кликаем на папку SLA
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[5]/div/div[1]/div/div[1]/div[2]/div/div['
                                          '5]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div['
                                          '16]/div/div[1]/span/div').click()

            time.sleep(30)

