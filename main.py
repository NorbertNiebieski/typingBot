import typingBot
import private_data


def main():

    # in the another python file you could do your on file with this string or write your login and password below
    typing_login = private_data.typing_login
    typing_password = private_data.typing_password

    sleeping_time = 5

    my_bot = typingBot.TypingBot(sleeping_time)

    my_bot.log_to_nitro(typing_login, typing_password)

    my_bot.get_mystery_box()

    choice = 1
    while choice != '2':
        choice = input("\n" + "1. Begin invite players you raced with in the last session" + "\n" +
                              "2. End program" + "\n" +
                       "\n" + "Your choice: ")
        if choice == '1':
            my_bot.invite_people_to_my_team()

    my_bot.friend_requests()


main()