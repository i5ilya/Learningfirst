import threading
import time
import requests

start_time = time.time()
def fun1():
    print('fun1 starting...')
    try:
        response = requests.get('http://fakedomain')

        print("Status:", response.status_code)
        print("Content-type:", response.headers['content-type'])
        print('fun1 завершена')

    except Exception as error:
        print(f"The error '{error}' occurred")
        print('fun1 завершена')


def fun2():
    print('fun2 starting...')
    try:
        response = requests.get('https://github.com/DidierRLopes/')

        print("Status:", response.status_code)
        print("Content-type:", response.headers['content-type'])
        print('fun2 завершена')

    except Exception as error:
        print(f"The error '{error}' occurred")
        print('fun2 завершена')

def main():
    fun1()
    fun2()

if __name__ == '__main__':
    #print(time.strftime('%X'))
    # my_thread = threading.Thread(target=main)
    # my_thread.start()
    #print(time.strftime('%X'))

    thread1 = threading.Thread(target=fun1)
    thread2 = threading.Thread(target=fun2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('run next code')
    print("--- %s seconds ---" % (time.time() - start_time))