from bot import OverPoll
import threading
def login(resp, auth):
    bot = OverPoll(resp, auth)

threading.Thread(target=login, args=("client1","token")).start()
threading.Thread(target=login, args=("client2","token")).start()
threading.Thread(target=login, args=("client3","token")).start()
print("USER LOGIN SUCCES.!!")
