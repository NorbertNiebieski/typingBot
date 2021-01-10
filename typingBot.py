from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class TypingBot:
    def __init__(self, sleep_time=5):

        self.typing_login = ""
        self.typing_password = ""

        # set depends of speed of your internet connection
        self.sleep_time = sleep_time

        # stats
        self.number_of_link_looked = 0
        self.number_of_new_course = 0
        self.number_of_had_course = 0
        self.number_of_not_free_course = 0
        self.number_of_unrecognized_course = 0
        self.number_of_checkout_problem = 0

        # web browser settings
        option = Options()

        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })

        self.driver = webdriver.Chrome(options=option)

    def log_to_nitro(self, typing_login, typing_password, printing=True):

        self.typing_login = typing_login
        self.typing_password = typing_password

        # go to udemy login page
        self.driver.get("https://www.nitrotype.com/login")
        sleep(1)
        self.driver.find_element_by_xpath("//button[@mode=\"primary\"]") \
            .click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(typing_login)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(typing_password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]") \
            .click()
        sleep(1)
        if self.driver.current_url == "https://www.nitrotype.com/garage":
            if printing:
                print("I have successfully logged into your Nitro account")
            return True
        else:
            if printing:
                print("Error! I was unable to login to your Nitro account")
            return False

    def invite_people_to_my_team(self, minimal_number_of_races=0, minimal_wpm=0):
        self.driver.get("https://www.nitrotype.com/friends")
        self.driver.find_elements_by_xpath("//button[@class=\"tab\"]")[2] \
            .click()
        number_of_recent_players = len(self.driver.find_elements_by_xpath("//tbody/tr[@class=\"table-row\"]"))
        print("I will check the " + str(number_of_recent_players) + " players you raced with in the last session")

        for i in range(0, number_of_recent_players):
            wpm = self.driver.find_elements_by_xpath("//td[@class=\"table-cell table-cell--speed\"]")[i] \
                .text
            wpm = int(wpm[:-3])
            number_of_races = self.driver.find_elements_by_xpath("//td[@class=\"table-cell table-cell--races\"]")[i] \
                .text
            number_of_races = int(number_of_races)
            text = self.driver.find_elements_by_xpath("//div[@class=\"prxs df df--align-center\"]")[i] \
                .text

            if (text.find("\n") == -1) and (minimal_number_of_races <= number_of_races) and (minimal_wpm <= wpm):
                self.driver.find_elements_by_xpath("//tbody/tr[@class=\"table-row\"]")[i] \
                    .click()
                try:
                    self.driver.find_element_by_xpath("//button[@class=\"btn btn--xs btn--light btn--top btn--thinner\"]") \
                        .click()
                except:
                    print("I can't invite player " + text + " to your team")
                else:
                    print("I sucesfuly invite player " + text + " to your team")

                self.driver.get("https://www.nitrotype.com/friends")
                self.driver.find_elements_by_xpath("//button[@class=\"tab\"]")[2] \
                    .click()

    def friend_requests(self, accept=True):
        self.driver.get("https://www.nitrotype.com/friends")
        try:
            if accept:
                self.driver.find_element_by_xpath("//button[contains(text(),\"Accept All\")]") \
                    .click()
            else:
                self.driver.find_element_by_xpath("//button[contains(text(),\"Ignore All\")]") \
                    .click()
        except:
            print("You don't have any friend requests!")

    def get_mystery_box(self):
        if self.driver.current_url == "https://www.nitrotype.com/garage":
            self.driver.get("https://www.nitrotype.com/garage")
        try:
            self.driver.find_element_by_xpath("//div[@class=\"mysteryBox\"]//button") \
                .click()
            self.driver.find_element_by_xpath("//button[contains(text(), \"Close\")]") \
                .click()
            print("I successfully took the mystery box!")
        except:
            print("I was unable to take the mystery box!")
