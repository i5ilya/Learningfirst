import threading
import time


#start_time = time.time()
lock = threading.Lock()
def fun1():
    print('fun1 starting...')
    '''
    Функция тормоз
    
    '''
    time.sleep(5)
    x = 5 * 1000
    return x

def fun2(x):
    print('fun2 starting...')
    lock.acquire()
    try:
        print('Lock acquired in the fun2')
    finally:
        lock.release()
        if x:
            y = x * 2
            print(f'fun2 завершена, y = {y}')



if __name__ == '__main__':
    #print(time.strftime('%X'))
    #my_thread = threading.Thread(target=main)
    #my_thread.start()
    #print(time.strftime('%X'))
    #thread1 = threading.Thread(target=fun1)
    thread2 = threading.Thread(target=fun2, args=(fun1(),))
    #thread1.start()
    thread2.start()
    #thread1.join()
    thread2.join()

    #print("--- %s seconds ---" % (time.time() - start_time))