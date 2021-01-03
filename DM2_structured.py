"""
@Author: Srivatsa Kundurthy

This program automatically sends DMs to a list of usernames populated in a text
file
"""
# Import necessary modules

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# read usernames to list


class DM:
    def __init__(self, username, password, message):
        self.username = username
        self.password = password
        self.message = message

        #read text file with username input to a list
        text_file = open('t_usernames.txt', 'r')
        global lines
        lines = text_file.read().split('\n')
        print(lines)
        text_file.close()

        global lines_length
        lines_length = len(lines)
        print(lines_length)

    def messenger(self):

        browser = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
        browser.get('https://www.instagram.com/direct/inbox/')
        sleep(2)

        # log in with username and password
        form_data = []

        box_user = browser.find_elements_by_css_selector("form input")[0]

        form_data.append(box_user)

        box_pass = browser.find_elements_by_css_selector("form input")[1]

        form_data.append(box_pass)

        print(form_data)

        box_user.send_keys(self.username)

        box_pass.send_keys(self.password)

        box_pass.send_keys(Keys.ENTER)

        sleep(4)

        # escape first popup

        esc_pop_1 = browser.find_elements_by_css_selector('button')[1]

        esc_pop_1.click()

        sleep(1)

        # escape second popup

        esc_pop_2 = browser.find_element_by_xpath('//button[text() = "Not Now"]')

        esc_pop_2.click()

        sleep(2)

        #auto DM

        def send(k, x):
            if k == 0:  # first user is different
                # click new DM button
                click_new = browser.find_elements_by_css_selector('button')[1]

                click_new.click()

                sleep(2)

                # Type in username

                type_user = browser.find_elements_by_css_selector('div input')[1]

                type_user.send_keys(x)

                sleep(2)

                # Choose user (hit check)

                pick_user = browser.find_elements_by_css_selector('div button')[5]

                pick_user.click()

                sleep(2)

                # Click next button to select and proceed

                next_send = browser.find_elements_by_css_selector('div button')[4]

                next_send.click()

                sleep(2)

                # Type in message and press enter

                type_message = browser.find_elements_by_css_selector('textarea')[0]

                type_message.send_keys(self.message)

                type_message.send_keys(Keys.ENTER)

            else:  # for the rest of the users

                click_new = browser.find_elements_by_css_selector('div button')[1]

                click_new.click()

                sleep(1)

                type_user = browser.find_elements_by_css_selector('div input')[2]

                type_user.send_keys(x)

                sleep(2)

                pick_user = browser.find_elements_by_css_selector('div button')[10]

                pick_user.click()

                sleep(1.5)

                next_send = browser.find_elements_by_css_selector('div button')[9]

                next_send.click()

                sleep(2)

                type_message = browser.find_elements_by_css_selector('textarea')[0]

                type_message.send_keys(self.message)
                sleep(.5)
                type_message.send_keys(Keys.ENTER)

        for k in range(lines_length):  # i takes value defined above
            global x
            x = lines[k]
            print(x)
            send(k, x)
            sleep(4)

        sleep(2)

        browser.close()

