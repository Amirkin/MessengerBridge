import thread
from telegamAnswer import TelegramAnswer
from whatappAnswer import whatsappAnswer
import layer
from threading import Thread


layer.telegram_answer = TelegramAnswer()

def run_telegram(a):
    print ("run_telegram")
    layer.telegram_answer.connect()
    layer.telegram_answer.send_main_session()
    layer.telegram_answer.recieve_message()


def run_whatsapp(a):
    w = whatsappAnswer()
    stack = w.create_stack()
    layer.telegram_answer.set_stack(stack)
    w.receive_message(stack)


def loop_whatsapp(a):
    w_thread = Thread(target=run_whatsapp, args=(0, ))
    w_thread.start()
    w_thread.join()




if __name__ == "__main__":
    thread.start_new_thread(run_telegram, (0,))

    thread.start_new_thread(loop_whatsapp, (0,))
    while True:
        pass

