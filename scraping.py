import requests
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from csv import writer
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

#driver = webdriver.Firefox()
#driv = driver.get("https://www.paginegialle.it/ricerca/alberghi/zona%20Costiera%20Amalfitana?/p-1")


def costaAmal():
    with open('costaAmal.csv','a') as csv_file:
            csv_writer = writer(csv_file)
            headers = ['Title', 'City', 'Phone']
            csv_writer.writerow(headers)
            
            val = input('Inserisci: ristoranti o alberghi: ')
            for x in range(1,50):#50 alberghi 95 risoranti
                response = requests.get('https://www.paginegialle.it/ricerca/{}/zona%20Costiera%20Amalfitana/p-{}'.format(val,x))
                soup = BeautifulSoup(response.text,'html.parser')
                cards = soup.find_all(class_='vcard listElement')
                cards2 = soup.find_all(class_='vcard listElement flFree')
                for card in cards:
                    title = card.find(class_='fn itemTitle').get_text().replace('\n', '')
                    city = card.find(class_='locality').get_text().replace('\n', '')
                    phone = card.find(class_='phone-label').get_text().replace('\n', '')

                for card in cards2:
                    title = card.find(class_='fn itemTitle').get_text().replace('\n', '')
                    city = card.find(class_='locality').get_text().replace('\n', '')
                    phone = card.find(class_='phone-label').get_text().replace('\n', '')
                    
                    #driver.find_element_by_css_selector('.btn.btn-black.icn-sitoWeb.shinystat_ssxl').click()
                    csv_writer.writerow([title,city,phone])
                time.sleep(1)
                response.close()


            
def costaSorr():
    with open('costaSorr.csv','a') as csv_file:
            csv_writer = writer(csv_file)
            headers = ['Title', 'City', 'Phone']
            csv_writer.writerow(headers)

            val = input('Inserisci: ristoranti o alberghi: ')
            for x in range(1,49):#78 ristoranti 49 alberghi
                response = requests.get('https://www.paginegialle.it/ricerca/{}/zona%20Costiera%20Sorrentina/p-{}'.format(val,x))
                soup = BeautifulSoup(response.text,'html.parser')
                cards = soup.find_all(class_='vcard listElement')
                cards2 = soup.find_all(class_='vcard listElement flFree')
                for card in cards:
                    title = card.find(class_='fn itemTitle').get_text().replace('\n', '')
                    city = card.find(class_='locality').get_text().replace('\n', '')
                    phone = card.find(class_='phone-label').get_text().replace('\n', '')

                for card in cards2:
                    title = card.find(class_='fn itemTitle').get_text().replace('\n', '')
                    city = card.find(class_='locality').get_text().replace('\n', '')
                    phone = card.find(class_='phone-label').get_text().replace('\n', '')
                    
                    #driver.find_element_by_css_selector('.btn.btn-black.icn-sitoWeb.shinystat_ssxl').click()
                    csv_writer.writerow([title,city,phone])
                time.sleep(1)
                response.close()

print("   SSSSSSSSSSSSSSS                                                                  888888888      ")     
print(" SS:::::::::::::::S                                                               88:::::::::88    ")
print("S:::::SSSSSS::::::S                                                             88:::::::::::::88  ")
print("S:::::S     SSSSSSS                                                            8::::::88888::::::8 ")
print("S:::::S                cccccccccccccccc   ooooooooooo vvvvvvv           vvvvvvv8:::::8     8:::::8 ")
print("S:::::S              cc:::::::::::::::c oo:::::::::::oov:::::v         v:::::v 8:::::8     8:::::8 ")
print(" S::::SSSS          c:::::::::::::::::co:::::::::::::::ov:::::v       v:::::v   8:::::88888:::::8  ")
print("  SS::::::SSSSS    c:::::::cccccc:::::co:::::ooooo:::::o v:::::v     v:::::v     8:::::::::::::8   ")
print("    SSS::::::::SS  c::::::c     ccccccco::::o     o::::o  v:::::v   v:::::v     8:::::88888:::::8  ")
print("       SSSSSS::::S c:::::c             o::::o     o::::o   v:::::v v:::::v     8:::::8     8:::::8 ")
print("            S:::::Sc:::::c             o::::o     o::::o    v:::::v:::::v      8:::::8     8:::::8 ")
print("            S:::::Sc::::::c     ccccccco::::o     o::::o     v:::::::::v       8:::::8     8:::::8 ")
print("SSSSSSS     S:::::Sc:::::::cccccc:::::co:::::ooooo:::::o      v:::::::v        8::::::88888::::::8 ")
print("S::::::SSSSSS:::::S c:::::::::::::::::co:::::::::::::::o       v:::::v          88:::::::::::::88  ")
print("S:::::::::::::::SS   cc:::::::::::::::c oo:::::::::::oo         v:::v             88:::::::::88    ")
print(" SSSSSSSSSSSSSSS       cccccccccccccccc   ooooooooooo            vvv                888888888      ")
print("\n")

y = input('1-per la cost amalfitana 2-per la cost sorrentina: ')
if y == "1":
    costaAmal()
else:
    costaSorr()