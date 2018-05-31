from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np


browser = webdriver.Chrome()

def login():
    try:
        browser.get("https://bliss.uberinternal.com")
        browser.fullscreen_window()
        #browser.find_element_by_id('user_email').send_keys('')
        #browser.find_element_by_id('user_password').send_keys('')
        #browser.find_element_by_id('user_submit').click()
        #time.sleep(5)
        #browser.find_element_by_css_selector("body").click()
        time.sleep(100)
    except Exception:
        time.sleep(5)
        login()

def get_a_contact():
    try:
        browser.get("https://bliss.uberinternal.com")
        browser.fullscreen_window()
        time.sleep(9)
    except Exception:
        time.sleep(5)
        get_a_contact()

def core_process():
    try:
        get_a_contact()
        print("new contact processing starts here")
        print("waiting 5 seconds")
        time.sleep(5)
                                    #//*[@id="app"]/div/div/main/div/div[3]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/div
        driver_callbacks_selector = '//*[@id="app"]/div/div/main/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]'
        set_selector = '//*[@id="app"]/div/div/main/div/div[3]/div[2]/div[2]/div[1]/div[2]/button[2]'
        #set_selector = '//*[@id="app"]/div/div/main/div/div[3]/div[2]/div[2]/div[1]/div[2]/button'
        #//*[@id="app"]/div/div/main/div/div[3]/div[2]/div[3]/div[1]/div[2]/button[2]

        try:
            browser.find_element_by_xpath(driver_callbacks_selector).click()
            time.sleep(1)
            print("selected driver callbacks")
        except Exception:
            print ("Driver callbacks selection not needed")

        try:
            browser.find_element_by_xpath(set_selector).click()
            print("set the contact")
            print("waiting 5 seconds")
            time.sleep(5)
        except Exception:
            print ("set not needed")


                            #app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed > ul > li:nth-child(3) > button
        confirm_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed > ul > li:nth-child(3) > button'
        browser.find_element_by_css_selector(confirm_selector).click()
        time.sleep(1)
                                    #app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed > ul > li:nth-child(3) > button > i
        confirm_send_final_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed'
        browser.find_element_by_css_selector(confirm_send_final_selector).click()
        print("closing contact as resolved")
        time.sleep(1)


        core_process()
    except Exception:
        core_process()

login()
core_process()
