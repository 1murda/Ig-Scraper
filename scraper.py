from time import sleep
from selenium.common.exceptions import NoSuchElementException
from driver_cfg import driver


def cls() -> None:
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')


def login() -> None:
    keep_trying: bool = True

    while keep_trying:
        cls()
        username: str = input("Enter your username: ")
        password: str = input("Enter your password: ")   

        try:
            cls()
            print("Logging in...")
            driver.get("https://www.instagram.com/accounts/login/")

            sleep(4)
            # enter the username
            username_input = driver.find_element("name", "username").send_keys(username)
            # enter the password
            password_input = driver.find_element("name", "password").send_keys(password)
            # click on the login button
            driver.find_element(
                "xpath", 
                '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[1]/div[3]/button'
                ).click()

            sleep(4)
            # check if the error message is displayed
            wrong_credentials_msg: str = driver.find_element(
                            "xpath",
                            "//*[@id='slfErrorAlert']"
                            )
            
        except NoSuchElementException:
            keep_trying = input("Wrong credentials, try again? (y/n): ").lower() == 'y'
        
        except Exception as e:
            print(e)
            keep_trying = input("Something went wrong, try again? (y/n): ").lower() == 'y'

        input("Login successful, press enter to continue...")
        keep_trying = False



def get_followers() -> None:
    pass

if __name__ == '__main__':
    login()