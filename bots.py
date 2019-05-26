from bot import OverPoll
import threading
def login(resp, auth):
    bot = OverPoll(resp, auth)
    
threading.Thread(target=login, args=("client","token")).start()
print("USER LOGIN SUCCES.!!")
