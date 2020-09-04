import time
import threading
import concurrent.futures 


def do_something():
    print('Sleeping 1 second.......')
    time.sleep(1)
    print('Done sleeping..... ')

def do_something1(seconds):
    print(f'Sleeping {seconds}')
    time.sleep(seconds)
    print('Done')
    
def do_something2(second):
    print(f'Sleeping {second}')
    time.sleep(second)
    return 'Done'

def do_something3(second):
    print(f'Sleeping {second}')
    time.sleep(second)
    return f'Done {second}'


if __name__=='__main__':
    start = time.perf_counter()
    
    # t1 = threading.Thread(target=do_something)
    # t2 = threading.Thread(target=do_something)
    # t1.start()
    # t2.start()
    
    # t1.join()
    # t2.join()
    
    # threads = []
    
    # for _ in range(10):
    #     t = threading.Thread(target=do_something1, args=[6])
    #     t.start()
    #     threads.append(t)
    
    # for thread in threads:
    #     thread.join()     
    
    # with concurrent.futures.ThreadPoolExecutor() as executer:
    #     f1 = executer.submit(do_something2, 2)
    #     f2 = executer.submit(do_something2, 2)
    #     print(f1.result())
    #     print(f2.result())
    
    # with concurrent.futures.ThreadPoolExecutor() as executer:
    #     secs = [5,4,3,2,1]
    #     results = [executer.submit(do_something3,sec) for sec in secs]
    #     for f in concurrent.futures.as_completed(results):
    #         print(f.result())
    
    with concurrent.futures.ThreadPoolExecutor() as executer:
        secs = [5,4,3,2,1]
        results = executer.map(do_something3, secs)
        for f in results:
            print(f)

    end = time.perf_counter()
    
    print(end - start)

    