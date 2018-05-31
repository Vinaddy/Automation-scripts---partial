#Consolidated script for Rider callbacks, Delivery partner callbacks and Mexico facturas
#This code has been tested for errors on multiple instances and hold the corrected time and data logic
#Please tag yourself to Rider callbacks, Delivery partner callbacks and Mexico facturas CTGs befoe running this script

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
import datetime
import emoji

browser = webdriver.Chrome()

def login():
    try:
        browser.get("https://bliss.uberinternal.com")
        browser.fullscreen_window()
        browser.find_element_by_id('user_email').send_keys('')
        browser.find_element_by_id('user_password').send_keys('')
        browser.find_element_by_id('user_submit').click()
        time.sleep(5)
        browser.find_element_by_css_selector("body").click()
        time.sleep(20)
    except Exception:
        time.sleep(5)
        login()

def get_a_contact():
    try:
        browser.get("https://bliss.uberinternal.com")
        browser.fullscreen_window()
        time.sleep(10)
    except Exception:
        time.sleep(5)
        get_a_contact()



def route_ticket_DPC():
    time.sleep(4)
    try:
        try:
            current_url2 = browser.current_url
            open("routed_tickets.csv",'a').write("\n"+current_url2)
            print("this ticket is being routed")
            print(current_url2)
        except Exception:
            current_url2 = browser.current_url

        set_selector = '//*[@id="app"]/div/div/main/div/div[3]/div[2]/div[2]/div[1]/div[2]/button'

        try:
            browser.find_element_by_xpath(set_selector).click()
        except Exception:
            print ("set not needed in re-routing")

        driver_callbacks_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span'
        current_issuetype = browser.find_element_by_css_selector(driver_callbacks_selector).text

        try:

            issue_type_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span'
            current_issuetype = browser.find_element_by_css_selector(issue_type_selector).text

            browser.find_element_by_css_selector(issue_type_selector).click()

            print("callbacks selector initiated")

            time.sleep(3)

            all_flows_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ol > li:nth-child(1) > a > span:nth-child(2)'

            browser.find_element_by_css_selector(all_flows_selector).click()

            print("all flows selected")

            time.sleep(1)

            for i in range(1,7):
                    try:
                        rider_arrow2_selector = "#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ul > li:nth-child(" + str(i) +")"
                        category = browser.find_element_by_css_selector(rider_arrow2_selector).text
                        #print("rider_arrow2_selector" + rider_arrow2_selector)
                        #print("category" + category)
                        if ("Rider" in category):
                            print("in the if second loop to select")
                            rider_arrow3_selector = rider_arrow2_selector + " > a > i"
                            print("rider_arrow3_selector" + rider_arrow3_selector)
                            browser.find_element_by_css_selector(rider_arrow3_selector).click()
                            print("cliked on rider arrow")
                            break
                    except Exception as e:
                        print("failed in setting issue type")
                        print(e)
            time.sleep(2)

            pickup_arrow_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ul > li:nth-child(15) > a.tree-picker__backtracker.text-uber-white.soft-tiny.soft-small--sides > i'

            browser.find_element_by_css_selector(pickup_arrow_selector).click()
            print("feedback arrow selected")
            time.sleep(1)

            dummy_issue_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ul > li:nth-child(2) > a.display--inline-block.soft-tiny.flex--one.tree-picker__item.soft-small--sides.text--truncate.primary-font--semibold.text-uber-black-60 > div'

            print("fare review arrow selected")
            browser.find_element_by_css_selector(dummy_issue_selector).click()
            time.sleep(2)

        except Exception:
            print("routing possibly failed")

        circle_routing_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed > ul > li:nth-child(1)'

        browser.find_element_by_css_selector(circle_routing_selector).click()
        time.sleep(2)

        print("before send as open")

        send_as_open_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed'
        browser.find_element_by_css_selector(send_as_open_selector).click()

        print("after send as open")

        time.sleep(2)
        complete_core()

    except Exception:
        current_url2 = browser.current_url
        open("failed_routing_tickets.csv",'a').write("\n"+current_url2)
        print("failed while routing the contact. refer sheet")
        print(current_url2)
        complete_core()

def route_ticket_MF(flag_cancelled):
    time.sleep(4)
    try:
        try:
            current_url2 = browser.current_url
            open("routed_tickets.csv",'a').write("\n"+current_url2)
            print("this ticket is being routed")
            print(current_url2)
        except Exception:
            current_url2 = browser.current_url

        set_selector = '//*[@id="app"]/div/div/main/div/div[3]/div[2]/div[2]/div[1]/div[2]/button'

        try:
            browser.find_element_by_xpath(set_selector).click()
        except Exception:
            print ("set not needed in re-routing")


        if(flag_cancelled == 0):
            try:

                issue_type_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span'
                current_issuetype = browser.find_element_by_css_selector(issue_type_selector).text

                browser.find_element_by_css_selector(issue_type_selector).click()

                print("callbacks selector initiated")

                time.sleep(3)

                all_flows_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ol > li:nth-child(1) > a > span:nth-child(2)'

                browser.find_element_by_css_selector(all_flows_selector).click()

                print("all flows selected")

                time.sleep(1)

                for i in range(1,7):
                    try:
                        rider_arrow2_selector = "#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ul > li:nth-child(" + str(i) +")"
                        category = browser.find_element_by_css_selector(rider_arrow2_selector).text
                        print("rider_arrow2_selector" + rider_arrow2_selector)
                        print("category" + category)
                        if ("Rider" in category):
                            print("in the if loop to select")
                            rider_arrow3_selector = rider_arrow2_selector + " > a > i"
                            print("rider_arrow3_selector" + rider_arrow3_selector)
                            browser.find_element_by_css_selector(rider_arrow3_selector).click()
                            print("cliked on rider arrow")
                            break
                    except Exception as e:
                        print("failed in setting issue type")
                        print(e)

                time.sleep(2)

                feedback_arrow_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ul > li:nth-child(8) > a.tree-picker__backtracker.text-uber-white.soft-tiny.soft-small--sides > i'

                browser.find_element_by_css_selector(feedback_arrow_selector).click()
                print("feedback arrow selected")
                time.sleep(1)

                dummy_issue_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ul > li:nth-child(9) > a'
                print("fare review arrow selected")
                browser.find_element_by_css_selector(dummy_issue_selector).click()
                time.sleep(2)

            except Exception:
                print("routing possibly failed")
        else:
            try:
                issue_type_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span'
                current_issuetype = browser.find_element_by_css_selector(issue_type_selector).text

                browser.find_element_by_css_selector(issue_type_selector).click()

                print("callbacks selector initiated")

                time.sleep(3)

                all_flows_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ol > li:nth-child(1) > a > span:nth-child(2)'

                browser.find_element_by_css_selector(all_flows_selector).click()

                print("all flows selected")

                time.sleep(1)

                for i in range(1,7):
                    try:
                        rider_arrow2_selector = "#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ul > li:nth-child(" + str(i) +")"
                        category = browser.find_element_by_css_selector(rider_arrow2_selector).text
                        print("rider_arrow2_selector" + rider_arrow2_selector)
                        print("category" + category)
                        if ("Rider" in category):
                            print("in the if second loop to select")
                            rider_arrow3_selector = rider_arrow2_selector + " > a > i"
                            print("rider_arrow3_selector" + rider_arrow3_selector)
                            browser.find_element_by_css_selector(rider_arrow3_selector).click()
                            print("cliked on rider arrow")
                            break
                    except Exception as e:
                        print("failed in setting issue type")
                        print(e)

                time.sleep(2)
                pickup_arrow_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ul > li:nth-child(15) > a.tree-picker__backtracker.text-uber-white.soft-tiny.soft-small--sides > i'

                browser.find_element_by_css_selector(pickup_arrow_selector).click()
                print("feedback arrow selected")
                time.sleep(1)

                dummy_issue_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ul > li:nth-child(2) > a.display--inline-block.soft-tiny.flex--one.tree-picker__item.soft-small--sides.text--truncate.primary-font--semibold.text-uber-black-60 > div'

                print("fare review arrow selected")
                browser.find_element_by_css_selector(dummy_issue_selector).click()
                time.sleep(2)

            except Exception:
                print("routing possibly failed")

        circle_routing_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed > ul > li:nth-child(1)'

        browser.find_element_by_css_selector(circle_routing_selector).click()
        time.sleep(2)

        print("before send as open")

        send_as_open_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed'
        browser.find_element_by_css_selector(send_as_open_selector).click()

        print("after send as open")

        time.sleep(2)
        complete_core()

    except Exception:
        current_url2 = browser.current_url
        open("failed_routing_tickets.csv",'a').write("\n"+current_url2)
        print("failed while routing the contact. refer sheet")
        print(current_url2)
        complete_core()

def route_ticket_RC():
    time.sleep(4)
    try:
        try:
            current_url2 = browser.current_url
            open("routed_tickets.csv",'a').write("\n"+current_url2)
            print("this ticket is being routed")
            print(current_url2)
        except Exception:
            current_url2 = browser.current_url

        set_selector = '//*[@id="app"]/div/div/main/div/div[3]/div[2]/div[2]/div[1]/div[2]/button'

        try:
            browser.find_element_by_xpath(set_selector).click()
        except Exception:
            print ("set not needed in re-routing")

        driver_callbacks_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span'
        current_issuetype = browser.find_element_by_css_selector(driver_callbacks_selector).text

        try:

            issue_type_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span'
            current_issuetype = browser.find_element_by_css_selector(issue_type_selector).text

            browser.find_element_by_css_selector(issue_type_selector).click()

            print("callbacks selector initiated")

            time.sleep(2)

            all_flows_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ol > li:nth-child(1) > a > span:nth-child(2)'

            browser.find_element_by_css_selector(all_flows_selector).click()

            print("all flows selected")

            time.sleep(1)

            for i in range(1,7):
                    try:
                        rider_arrow2_selector = "#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ul > li:nth-child(" + str(i) +")"
                        category = browser.find_element_by_css_selector(rider_arrow2_selector).text
                        #print("rider_arrow2_selector" + rider_arrow2_selector)
                        #print("category" + category)
                        if ("Rider" in category):
                            print("in the if second loop to select")
                            rider_arrow3_selector = rider_arrow2_selector + " > a > i"
                            print("rider_arrow3_selector" + rider_arrow3_selector)
                            browser.find_element_by_css_selector(rider_arrow3_selector).click()
                            print("cliked on rider arrow")
                            break
                    except Exception as e:
                        print("failed in setting issue type")
                        print(e)

            print("rider arrow selected")

            time.sleep(1)

            fare_review_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ul > li:nth-child(7) > a.tree-picker__backtracker.text-uber-white.soft-tiny.soft-small--sides > i'

            browser.find_element_by_css_selector(fare_review_selector).click()
            print("feedback arrow selected")
            time.sleep(1)

            dummy_issue_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span.position--relative > span > div > div > div.position--relative.tree-picker__transition-container > div > ul > li:nth-child(7) > a.display--inline-block.soft-tiny.flex--one.tree-picker__item.soft-small--sides.text--truncate.primary-font--semibold.text-uber-black-60 > div'

            print("fare review arrow selected")
            browser.find_element_by_css_selector(dummy_issue_selector).click()
            time.sleep(2)

        except Exception as e:
            print("routing possibly failed")
            print(e)

        circle_routing_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed > ul > li:nth-child(1)'

        browser.find_element_by_css_selector(circle_routing_selector).click()
        time.sleep(2)

        print("before send as open")

        send_as_open_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed'
        browser.find_element_by_css_selector(send_as_open_selector).click()

        print("after send as open")

        time.sleep(2)
        complete_core()

    except Exception:
        current_url2 = browser.current_url
        open("failed_routing_tickets.csv",'a').write("\n"+current_url2)
        print("failed while routing the contact. refer sheet")
        print(current_url2)
        complete_core()



def close_ticket_DPC(first_name, code):
    time.sleep(3)

    try:
        if(code > 0):
            line0 ="Sorry to hear about any inconvenience this experience may have caused, %s, and thank you for letting us know. "%(first_name.title())
            line1 = "Please expect to hear from us on this within 48 hours via SMS."
            line2 = "Feedback like yours helps us support and educate driver-partners to prevent such instances from repeating. On checking your trip, it looks like this fee was already refunded as Uber credits. You can see these under Menu > Payment > Uber credits and use them on future trips, or on UberEATS."
            line3 = "On checking it appears that your driver had already reached the pickup location requested by you when you cancelled. Since the cancellation fee is in place to compensate your driver for their fuel & time, we would not be able to issue a refund here. If you still feel you were charged unfairly, please let us know by replying to this message so that we can look into this."
            line4 = "On checking it appears that your driver had already reached the pickup location requested by you and waited for 5 minutes before cancelling. Since the cancellation fee is in place to compensate your driver for their fuel & time, we would not be able to issue a refund here. If you still feel you were charged unfairly, please let us know by replying to this message so that we can look into this. "
            line5 = "Please expect to hear from us on this within 24 hours via SMS."

            if(code == 1):
                text_reply = line0+line1
            if(code == 2):
                text_reply = line0+line2
            if(code == 3):
                text_reply = line0+line3
            if(code == 4):
                text_reply = line0+line4
            if(code == 5):
                text_reply = line0+line5

            text_input_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__composition-area.bg-white > div.message-container__reply-composer.position--relative > div.content-editable.position--relative > div.content-editable__textarea'
            browser.find_element_by_css_selector(text_input_selector).send_keys(text_reply)

        confirm_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed > ul > li:nth-child(3) > button'
        browser.find_element_by_css_selector(confirm_selector).click()
        time.sleep(1)

        confirm_send_final_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed'
        browser.find_element_by_css_selector(confirm_send_final_selector).click()

        time.sleep(2)

        complete_core()

    except Exception:
        time.sleep(3)
        complete_core()

    print("closed this ticket")

def close_ticket_MF(first_name,flag_cancelled):
    time.sleep(3)
    first_name = first_name.title()
    try:

        line1 = "Hi %s,"%(first_name)
        #line1 = str(line1)
        line2 = "\n\nThanks for your feedback."
        line3 = "\n\nPlease know that it is important for us to ensure that your experience with Uber is smooth and professional. We've recorded your feedback and will initiate appropriate action so this doesn't happen again."

        if(flag_cancelled ==1):
            line4 = "\n\nHope this helps!"
        elif(flag_cancelled == 101):
            line4 ="\n\nI reviewed the details and found that we've added the cancellation fee for this trip to your account as Uber credits. These will apply automatically on your upcoming trips with Uber. You can view these credits under the 'Payments' tab on your Uber app.\n\nHope this helps!"
        elif(flag_cancelled == 102):
            line4 = "We've charged a cancellation fee as the trip was cancelled 5 minutes after the driver arrived at the given pickup location. \nThe fee helps us appropriately compensate our driver partners for the time and fuel they spend to arrive at your pick-up location. \n\nIf you feel the fee was incorrectly charged, please:\n\n1. Go to the 'Trips' section of the app under 'Menu'\n2. Select the cancelled trip\n3. Scroll down and go to 'Help'\n4. Tap 'Problem with cancellation fee'\n5. Select the most appropriate reason\n\nHope this helps!"
        elif(flag_cancelled == 103):
            line4 = "\n\nHope this helps!"
        elif(flag_cancelled == 104):
            line3 = "\n\nI reviewed the details and found that the cancellation fee for this trip has been added to your account as Uber credits. These will apply automatically on your upcoming trips with Uber. You can view these credits under the 'Payments' tab on your Uber app."
            line4 = "\n\nPlease know that it is important for us to ensure that your experience with Uber is smooth and professional. We've recorded your feedback and will initiate appropriate action. \n\nHope this helps!"
        elif(flag_cancelled == 105):
            line4 = "\n\nIf you think you were incorrectly charged a cancellation fee, please:\n\n1. Go to the 'Trips' section of the app under 'Menu'\n2. Select the cancelled trip\n3. Scroll down and go to 'Help'\n4. Tap 'Problem with cancellation fee'\n5. Select the most appropriate reason\n\nHope this helps!"
        elif(flag_cancelled == 106):
            line4 = "\n\nHope this helps!"


        # if(flag_cancelled==1):
        #     line4 = "if you think there is an issue with cancellation please follow the following instructions"

        text_reply = line1+line2+line3+line4


        print("text_reply")
        #print(text_reply)

        text_input_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__composition-area.bg-white > div.message-container__reply-composer.position--relative > div.content-editable.position--relative > div.content-editable__textarea'
        browser.find_element_by_css_selector(text_input_selector).send_keys(text_reply)

        confirm_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed > ul > li:nth-child(3) > button'
        browser.find_element_by_css_selector(confirm_selector).click()
        time.sleep(1)

        confirm_send_final_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed'
        browser.find_element_by_css_selector(confirm_send_final_selector).click()

        time.sleep(2)

    except Exception:
        time.sleep(3)
        complete_core()

    print("closed this ticket")

def close_ticket_RC():
    time.sleep(3)

    try:
        confirm_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed > ul > li:nth-child(3) > button'
        browser.find_element_by_css_selector(confirm_selector).click()
        time.sleep(1)

        confirm_send_final_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed'
        browser.find_element_by_css_selector(confirm_send_final_selector).click()

        time.sleep(2)

    except Exception:
        time.sleep(3)
        complete_core()

    print("closed this ticket")

def close_ticket_RC_with_response(first_name, code):

    time.sleep(3)

    try:
        if(code > 0):
            line0 = "Sorry to hear about any inconvenience this experience may have caused, %s, and thank you for letting us know. "%(first_name.title())
            line1 = "Please expect to hear from us on this within 48 hours via SMS"
            line2 = "Please expect to hear from us on this within 24 hours via SMS."
            line3 = "We wish to inform you that a resolution for your issue has already been given to you via SMS"

            if(code == 1):
                text_reply = line0+line1
            if(code == 2):
                text_reply = line0+line2
            if(code == 3):
                text_reply = line0+line3

            text_input_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__composition-area.bg-white > div.message-container__reply-composer.position--relative > div.content-editable.position--relative > div.content-editable__textarea'
            browser.find_element_by_css_selector(text_input_selector).send_keys(text_reply)

        confirm_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed > ul > li:nth-child(3) > button'
        browser.find_element_by_css_selector(confirm_selector).click()
        time.sleep(1)

        confirm_send_final_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.action-pane.position--relative > div.message-container.position--relative.push-huge--bottom > div.message-container__toolbar.one-whole.position--absolute.text--right.soft-small--left > div.btn-group--mixed'
        browser.find_element_by_css_selector(confirm_send_final_selector).click()

        time.sleep(5)

        complete_core()

    except Exception:
        time.sleep(3)
        complete_core()

    print("closed this ticket and told rider he will hear from us in 48 hours via SMS")



def check_date_time(time_string):
    time_format = "%B:%d:%Y:%I:%M:%p"
    time_string_modified1 = time_string.replace(",","")
    time_string_modified = time_string_modified1.replace(" ",":")
    contact_date = datetime.datetime.strptime(time_string_modified, time_format)
    current_date = datetime.datetime.now()

    time_diff = current_date - contact_date

    time_diff_hrs = time_diff.days*24 + time_diff.seconds//3600

    print("the time difference of contact first raised and current time is " + str(time_diff_hrs))

    return time_diff_hrs

def text_has_emoji(text):
    for char in text:
        if char in emoji.UNICODE_EMOJI:
            return True
    return False



def core_process_DPC():
    try:


        first_name = ""
        full_name = ""
        failed_time_check = 0

        try:
            first_name_selector = '#context-pane > div > div > div > div:nth-child(1) > a > div > div.panel.square--bottom.borderless--bottom > div.soft-small--ends.block-context > h3'
            full_name = browser.find_element_by_css_selector(first_name_selector).text
            first_name = browser.find_element_by_css_selector(first_name_selector).text.split()[0]
            print(first_name)
        except Exception:
            first_name = ""
            full_name = "ignore"
            print("was not able to retreive first name")

        if(text_has_emoji(full_name)):
            route_ticket_DPC()

        page_source = browser.page_source
        soup = BeautifulSoup(page_source, "lxml")

        try:
            #time_first_raised_selector = "#app > div > div > main > div > div.contact-pane.push--right > div.conversation-pane.conversation-pane--scrollshadow-bottom > div:nth-child(1) > div.message-contact__container > div.legal.flush--line-height > a > span.tooltip.tooltip--bottom-left"
            time_of_first_contact = str(soup.find_all("span", class_= "tooltip tooltip--bottom-left")[0].text)
            #time_of_first_contact = float((soup.find_all("td", class_= "text--right borderless--top")[1].text)[1:])
            #time_of_first_contact = browser.find_element_by_css_selector(time_first_raised_selector).text
            print("time_of_first_contact" + time_of_first_contact)
        except Exception as e:
            print("failed in getting time of the contact")
            print(e)


        #time check code here
        try:
            time_check = check_date_time(time_of_first_contact)
            print("time check is " + str(time_check))
        except Exception:
            failed_time_check = 1


        if(time_check < 24):
            print("informed partner to wait for 48 hours")
            close_ticket_DPC(first_name,1)

        try:
            actual_fare_selector = '#context-pane > div > div > a > section > div.soft-small.desk-wide-soft-small--sides > div > div:nth-child(1)'
            actual_fare = float(browser.find_element_by_css_selector(actual_fare_selector).text[6:].replace(',',''))
        except Exception:
            actual_fare = 0
            print("failed in actual fare. Defaulting as zero")

        try:

            conversation_pane_selector = '#app > div > div > main'
            conversation_history = browser.find_element_by_css_selector(conversation_pane_selector).text
            #print("conversation_history")
            #print(conversation_history)

            words= conversation_history.split()
            #print("words in conversation history")
            #print(words)

        except Exception:
            print("failed to load conversation history. redirecting a new contact")
            time.sleep(2)
            route_ticket_DPC()


        content_checker = conversation_history.lower().split("date of your trip")

        if (full_name.lower() in content_checker[-1].lower()):
            print("routing this ticket because this was a reopen from closed ticket")
            route_ticket_DPC()

        try:
            content_checker2 = conversation_history.lower()
            syntaxes = content_checker2.count("date of your trip")
            print("syntaxes = " + str(syntaxes))
            driver_names = content_checker2.count(full_name.lower())-1
            print("driver_names = " + str(driver_names))

            if(syntaxes == driver_names):
                free_text = 0
            else:
                free_text = 1
        except Exception:
            print("failed in content checker")

        if(free_text == 1):
            print("routing this ticket because this was a reopen from closed ticket with text in between syntaxes")
            route_ticket_DPC()

        #print("demarkation")
        #print(content_checker[-1])

        print("demarkation")

        try:
            actual_fare_selector2 = '#context-pane > div > div > a > section > div.soft-small.desk-wide-soft-small--sides > div > div:nth-child(1)'
            browser.find_element_by_css_selector(actual_fare_selector2).click()
            time.sleep(1) #can_be_deleted
        except Exception:
            print("failed to click on fare")

        try:
            url_trip_uuid = browser.current_url
            trip_uuid = url_trip_uuid.split("/")[-1]
            print("trip_uuid" + trip_uuid)
        except Exception as e:
            print(e)

        go_back_selector = '#context-pane > div.position--fixed.one-whole.context-pane__header.bg-white > div.soft-small--sides.soft-small--bottom > ul > li:nth-child(1) > a > span'
        browser.find_element_by_css_selector(go_back_selector).click()

        time.sleep(1)

        #fetch rider details

        try:
            browser.find_element_by_css_selector(first_name_selector).click()
            time.sleep(1) #can_be_deleted
        except Exception as e:
            print("failed to click on rider name")
            print(e)

        try:
            for i in range (1,4):
                rider_notes_header_selector = "#context-pane > div.context__details.soft--sides > div:nth-child(" + str(i) +") > header > div > span > h4"
                table_header1 = browser.find_element_by_css_selector(rider_notes_header_selector).text

                #table notes processing
                reference_note =""
                status_string = ""
                trip_not_found = 0
                status_outcome_refund = ["already appeased","other - 1 sided refund", "refused destination - 2 sided refund","rider canceled - driver>100m and enroute - one sided refund","rider canceled - driver>100m and not enroute","rider canceled - driver>100m and not enroute - two sided refund","refused destination - 2 sided refund"]
                status_outcome_no_refund = ["rider canceled - driver within 100m - no refund"]
                status_outcome_driver_cancel = ["no refund - driver cancellation"]

                if(table_header1.lower() == "notes"):
                    rider_notes_selector = "#context-pane > div.context__details.soft--sides > div:nth-child("+str(i)+") > div > table"
                    rider_notes1 = browser.find_element_by_css_selector(rider_notes_selector).text
                    print("______rider notes 1 _____")


                    try:
                        all_notes_button_selector = "#context-pane > div.context__details.soft--sides > div:nth-child("+str(i)+") > header > div > a"
                        browser.find_element_by_css_selector(all_notes_button_selector).click()

                        all_notes_selector = "#context-pane > div.context__details--user-summary-hidden.push-huge--top.soft-huge--top.soft--sides > div > div > table"
                        rider_notes1 = browser.find_element_by_css_selector(all_notes_selector).text
                    except Exception:
                        print("no extra page of table notes found. Hence continuing")

                    print(rider_notes1)
                    browser.find_element_by_css_selector(go_back_selector).click()

                    if(rider_notes1.lower().count("status") == 0):
                        print("routing because there is notes but no relevant message")
                        route_ticket_DPC()

                    try:
                        status_string = rider_notes1.lower().split(trip_uuid)[0].split("status - ")[-1].split(" trip uuid")[0]
                        print("status_string is " + status_string)
                    except Exception:
                        trip_not_found = 1

                    if(trip_not_found ==1 and time_check > 48):
                        print("there are no notes about this trip")
                        route_ticket_DPC()

                    if(trip_not_found ==1 and 24 < time_check < 48):
                        print("there are no notes about this trip, informed partner to wait for 24 hours")
                        close_ticket_DPC(first_name,5)

                    if(time_check < 24):
                        print("informed partner to wait for 48 hours")
                        close_ticket_DPC(first_name,1)

                    if (status_string in status_outcome_refund):
                        print("status in status_outcome_refund")
                        close_ticket_DPC(first_name,2)

                    if (status_string in status_outcome_no_refund):
                        print("status in status_outcome_no_refund")
                        close_ticket_DPC(first_name,3)

                    if(status_string in status_outcome_driver_cancel):
                        print("status in status_outcome_driver_cancel")
                        close_ticket_DPC(first_name,4)

                    if((status_string not in status_outcome_refund) and (status_string not in status_outcome_no_refund) and (status_string not in status_outcome_driver_cancel)):
                        print("Incorrect status string. Hence routing")
                        route_ticket_DPC()
                    break
        except:
            print("failed while getting table notes")
            route_ticket_DPC()

        time.sleep(2)
        complete_core()
    except Exception as e:
        print("****************failed somewhere*****************")
        print(e)
        route_ticket_DPC()

def core_process_MF():

    print("new MF contact processing starts here")
    try:
        driver_callbacks_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span'
        current_issuetype = browser.find_element_by_css_selector(driver_callbacks_selector).text
    except Exception:
        current_issuetype = ""
    if("asked how to use facturas tool" not in current_issuetype.lower()):
        try:
            ctg_test_selector='#app > div > div > main > div > div.contact-pane.push--right > div.conversation-pane > div.contact-type-reassigner.bg-uber-white-10.soft--sides.soft-small--top.soft--bottom.display--flex.flex--column > div.contact-type-reassigner__panel.panel.bg-white.height-full.flex--one.display--flex.flex--column > div > div.position--relative > div.input-group.icon-input.left > input'
            browser.find_element_by_css_selector(ctg_test_selector).send_keys("asked how to use facturas tool")
            print("typed the issue type successfully")
            time.sleep(2)

        except Exception:
            get_a_contact()
        #contact_type_selector = '#app > div > div > main > div > div.contact-pane.push--right > div.conversation-pane.conversation-pane--scrollshadow-top.conversation-pane--scrollshadow-bottom > div.contact-type-reassigner.bg-uber-white-10.soft--sides.soft-small--top.soft--bottom.display--flex.flex--column > div.contact-type-reassigner__panel.panel.bg-white.height-full.flex--one.display--flex.flex--column > div > div.position--relative > div.contact-type-reassigner__search-results.panel.z-10.square--top.position--absolute.bg-white.panel.borderless--top > div'
        #app > div > div > main > div > div.contact-pane.push--right > div.conversation-pane.conversation-pane--scrollshadow-top.conversation-pane--scrollshadow-bottom > div.contact-type-reassigner.bg-uber-white-10.soft--sides.soft-small--top.soft--bottom.display--flex.flex--column > div.contact-type-reassigner__panel.panel.bg-white.height-full.flex--one.display--flex.flex--column > div > div.contact-type-reassigner__selector.flex--one.display--flex > div > div:nth-child(3) > div
        try:
            contact_type_selector= '#app > div > div > main > div > div.contact-pane.push--right > div.conversation-pane.conversation-pane--scrollshadow-bottom > div.contact-type-reassigner.bg-uber-white-10.soft--sides.soft-small--top.soft--bottom.display--flex.flex--column > div.contact-type-reassigner__panel.panel.bg-white.height-full.flex--one.display--flex.flex--column > div > div.position--relative > div.contact-type-reassigner__search-results.panel.z-10.square--top.position--absolute.bg-white.panel.borderless--top > div > span > b'
            text_right = browser.find_element_by_css_selector(contact_type_selector).click()
            print(text_right)

            time.sleep(2)

            print("your contact type is selected")
        except Exception:
            #current_url2 = browser.current_url
            #open("failed_selecting_facturas.csv",'a').write("\n"+current_url2)
            print("failed while selecting the issue type. refer sheet")
            #logging.exception("close_ticket_MF_log")
            get_a_contact()

        print("clicked on issue type")
        set_selector = '//*[@id="app"]/div/div/main/div/div[3]/div[2]/div[2]/div[1]/div[2]/button[2]'

        try:
            browser.find_element_by_xpath(set_selector).click()
            print("set the contact")
        except Exception:
            print ("set not needed")
    time.sleep(1)

    set_selector = '//*[@id="app"]/div/div/main/div/div[3]/div[2]/div[2]/div[1]/div[2]/button'

    try:
        browser.find_element_by_xpath(set_selector).click()
        print("set the contact")
    except Exception:
        print ("set not needed")
    first_name = ""
    full_name = ""
    name_avl = 0
    time.sleep(1)

    try:
        first_name_selector = '#context-pane > div > div > div > div:nth-child(1) > a > div > div.panel.square--bottom.borderless--bottom > div.soft-small--ends.block-context > h3'
        full_name = browser.find_element_by_css_selector(first_name_selector).text
        first_name = browser.find_element_by_css_selector(first_name_selector).text.split()[0]
        print(first_name)

    except Exception:
        first_name = ""
        full_name = "XXX"
        name_avl = 1
        print("a ticket without trip details")

    if(text_has_emoji(full_name)):
        route_ticket_MF(0)

    if(name_avl == 1):
        try:
            full_name_selector = '#context-pane > div.position--fixed.one-whole.context-pane__header.bg-white.soft-small--bottom > div.context-pane__user-summary.soft--sides > div > div.soft--left.flex--one > div:nth-child(1) > div:nth-child(1) > h3'
            full_name = browser.find_element_by_css_selector(full_name_selector).text
            first_name = full_name.split()[0]
        except Exception:
            first_name = ""
            full_name = "XXX"

    try:
        actual_fare_selector = '#context-pane > div > div > a > section > div.soft-small.desk-wide-soft-small--sides > div > div:nth-child(1)'
        actual_fare = float(browser.find_element_by_css_selector(actual_fare_selector).text[6:].replace(',',''))
    except Exception:
        actual_fare = 0
        print("failed in actual fare. Defaulting as zero")

    try:

        conversation_pane_selector = '#app > div > div > main'
        conversation_history = browser.find_element_by_css_selector(conversation_pane_selector).text
        #print("conversation_history")
        #print(conversation_history)

        words= conversation_history.split()
        #print("words in conversation history")
        #print(words)

    except Exception:
        print("failed to load conversation history. loading a new contact")
        time.sleep(5)
        route_ticket_MF(0)

    flag_cancelled = 0
    flag_rider_cancelled = 0
    flag_driver_cancelled = 0
    table_notes= ""
    if("CANCELLED BY".lower() in conversation_history.lower()):
        flag_cancelled = 1
        if("CANCELLED BY RIDER".lower() in conversation_history.lower()):
            flag_rider_cancelled = 1
        if("CANCELLED BY DRIVER".lower() in conversation_history.lower()):
            flag_driver_cancelled = 1

    try:
        actual_fare_selector2 = '#context-pane > div > div > a > section > div.soft-small.desk-wide-soft-small--sides > div > div:nth-child(1)'
        browser.find_element_by_css_selector(actual_fare_selector2).click()
    except Exception:
        print("failed to click on fare")

    try:
        table_notes_selector = '#context-pane > div.context__details.soft--sides > div.tableau.bg-white.position--relative.tableau__transition.push--bottom > div > table'
        table_notes = browser.find_element_by_css_selector(table_notes_selector).text
        print("table notes")
        print(table_notes)
        print("reop")

    except Exception:
        print("failed to extract content from table")

    try:
        all_notes_selector = '#context-pane > div.context__details.soft--sides > div.tableau.bg-white.position--relative.tableau__transition.push--bottom > header > div > a'
        browser.find_element_by_css_selector(all_notes_selector).click()
        table_notes2_selector = '#context-pane > div.context__details--user-summary-hidden.push-huge--top.soft-huge--top.soft--sides > div > div > table'
        table_notes2 = browser.find_element_by_css_selector(table_notes2_selector).text
        print("table notes2")
        print(table_notes2)
        print("There is a second page of table notes for this contact")
    except Exception:
        print("no table notes 2")
        table_notes2 = "XYZ"

    table_notes_final = table_notes+" "+table_notes2
    print("table notes " + table_notes_final)

    try:
        go_back_selector = '#context-pane > div.position--fixed.one-whole.context-pane__header.bg-white > div.soft-small--sides.soft-small--bottom > ul > li:nth-child(1) > a > span'
        browser.find_element_by_css_selector(go_back_selector).click()
    except Exception:
        print("tried to go back but failed")

    if("UPDATED CONTACT STATUS TO SOLVED" in conversation_history):
        print("routing this ticket because this was a reopen from closed ticket")
        route_ticket_MF(flag_cancelled)

    content_checker = conversation_history.lower().split("date of your trip")

    print(content_checker)
    print("demarkation")
    #print("demarkation")
    #print(content_checker[-1])

    if (full_name.lower() in content_checker[-1].lower()):
        route_ticket_MF(flag_cancelled)

    ##Core logic now for cancellations now

    if(flag_driver_cancelled == 1 and actual_fare > 0 and "INR automatically added to rider's account by Bliss" in table_notes_final):
        close_ticket_MF(first_name,101)
    elif(flag_driver_cancelled == 1 and actual_fare > 0):
        close_ticket_MF(first_name,102)
    elif(flag_driver_cancelled == 1 and actual_fare < 1):
        close_ticket_MF(first_name, 103)
    elif(flag_rider_cancelled == 1 and actual_fare > 1 and "INR automatically added to rider's account by Bliss" in table_notes_final):
        close_ticket_MF(first_name,104)
    elif(flag_rider_cancelled == 1 and actual_fare > 1):
        close_ticket_MF(first_name,105)
    elif(flag_rider_cancelled == 1 and actual_fare < 1):
        close_ticket_MF(first_name,106)
    else:
        close_ticket_MF(first_name,1)

    time.sleep(2)
    complete_core()

def core_process_RC():
    try:
        first_name = ""
        full_name = ""
        conversation_history =""
        try:
            first_name_selector = '#context-pane > div > div > div > div:nth-child(1) > a > div > div.panel.square--bottom.borderless--bottom > div.soft-small--ends.block-context > h3'
            full_name = browser.find_element_by_css_selector(first_name_selector).text
            first_name = browser.find_element_by_css_selector(first_name_selector).text.split()[0]
            print(first_name)
        except Exception:
            first_name = ""
            full_name = "ignore"
            print("was not able to retreive first name")


        #Time logic
        page_source = browser.page_source
        soup = BeautifulSoup(page_source, "lxml")

        try:
            #time_first_raised_selector = "#app > div > div > main > div > div.contact-pane.push--right > div.conversation-pane.conversation-pane--scrollshadow-bottom > div:nth-child(1) > div.message-contact__container > div.legal.flush--line-height > a > span.tooltip.tooltip--bottom-left"
            time_of_first_contact = str(soup.find_all("span", class_= "tooltip tooltip--bottom-left")[0].text)
            #time_of_first_contact = float((soup.find_all("td", class_= "text--right borderless--top")[1].text)[1:])
            #time_of_first_contact = browser.find_element_by_css_selector(time_first_raised_selector).text
            print("time_of_first_contact " + time_of_first_contact)
        except Exception as e:
            print("failed in getting time of the contact")
            print(e)


        #time check code here
        try:
            time_check = check_date_time(time_of_first_contact)
            print("time check is " + str(time_check))
        except Exception:
            failed_time_check = 1


        try:

            conversation_pane_selector = '#app > div > div > main'
            conversation_history = browser.find_element_by_css_selector(conversation_pane_selector).text
            #print("conversation_history")
            #print(conversation_history)

            words= conversation_history.split()
            #print("words in conversation history")
            #print(words)

        except Exception:
            print("failed to load conversation history. loading a new contact")
            time.sleep(2)
            get_a_contact()


        content_checker = conversation_history.lower().split("date of your trip")

        #print(content_checker)
        print("demarkation")
        #print("demarkation")
        #print(content_checker[-1])

        if (full_name.lower() in content_checker[-1].lower()):
            print("routing this ticket because this was a reopen from closed ticket")
            route_ticket_RC()

        try:
            content_checker2 = conversation_history.lower()
            syntaxes = content_checker2.count("date of your trip")
            print("syntaxes = " + str(syntaxes))
            driver_names = content_checker2.count(full_name.lower())-1
            print("driver_names = " + str(driver_names))

            if(syntaxes == driver_names):
                free_text = 0
            else:
                free_text = 1
        except Exception:
            print("failed in content checker")

        if(free_text == 1):
            print("routing this ticket because this was a reopen from closed ticket with text in between syntaxes")
            route_ticket_RC()


        if(time_check < 24):
            print("there are no notes about this trip and this was processed less than 24 hrs ago")
            print("closing this ticket with a relevant response")
            time.sleep(2)
            close_ticket_RC_with_response(first_name, 1)

        if(24 < time_check < 48):
            print("there are no notes about this trip and this was processed between 24 - 48 hours ago")
            print("closing this ticket with a relevant response")
            time.sleep(2)
            close_ticket_RC_with_response(first_name, 2)

        if(time_check > 48):
            print("This ticket hass been created more than 48 hours ago")
            print("closing this ticket with a relevant response")
            time.sleep(2)
            close_ticket_RC_with_response(first_name, 3)


        #close_ticket_RC()
        time.sleep(2)
        complete_core()
    except Exception as e:
        print(e)
        print("#################failed somwhere################")
        route_ticket_RC()

def complete_core():

    try:
        get_a_contact()
        print("new contact processing starts here, waiting 5 seconds for the contact to load")
        time.sleep(5)

        set_selector = '//*[@id="app"]/div/div/main/div/div[3]/div[2]/div[2]/div[1]/div[2]/button'

        try:
            browser.find_element_by_xpath(set_selector).click()
            print("set the contact")
        except Exception:
            print ("set not needed")
            #1 #app > div > div > main > div > div.contact-pane.push--right > header > div > div
            #app > div > div > main > div > div.contact-pane.push--right > header > div > div > div
            #app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span
            #app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span > span
            #app > div > div > main > div > div.contact-pane.push--right > header > div > div > div > span
            #app > div > div > main > div > div.contact-pane.push--right > header > div > h4
            #app > div > div > main > div > div.contact-pane.push--right > header > div
            #app > div > div > main > div > div.contact-pane.push--right > header > div
            #app > div > div > main > div > div.contact-pane.push--right > header > div.bg-white.soft-micro.z-10.layout__item.hard--left.seven-eighths > div
        issue_type_selector = '#app > div > div > main > div > div.contact-pane.push--right > header > div > div'
        current_issuetype = browser.find_element_by_css_selector(issue_type_selector).text

        try:

            if ("delivery partner callbacks" in current_issuetype.lower()):
                print("Working on a Delivery Partner callbacks contact")
                core_process_DPC()

            elif("rider callbacks" in current_issuetype.lower()):
                print("Working on a Rider callbacks contact")
                core_process_RC()

            elif("asked how to use facturas tool" in current_issuetype.lower()):
                print("Working on a Mexico Facturas contact")
                core_process_MF()

        except Exception:
            print("Unable to identify CTG")

    except Exception as e:
        print("failed to initiate the complete_core(). Restarting procecss.")
        complete_core()


login()
complete_core()
