import threading
import time
start_time = time.time()

def doubler(number):
    """
    A function that can be used by a thread
    """
    #print(threading.current_thread().name + '\n')
    print(number * 1000000)
    print()


if __name__ == '__main__':
    for i in range(5):
        #doubler(i)
        my_thread = threading.Thread(target=doubler, args=(i,))
        my_thread.start()
    print("--- %s seconds ---" % (time.time() - start_time))