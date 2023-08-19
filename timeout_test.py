import _thread
import utime

def test():
    # Simulate some work
    utime.sleep(1)

def execute_with_timeout():
    timeout = 0.5  # Timeout in seconds

    thread_done = False

    def execute_test():
        nonlocal thread_done
        test()
        thread_done = True

    thread_id = _thread.start_new_thread(execute_test, ())

    start_time = utime.time()
    while not thread_done and utime.time() - start_time < timeout:
        pass

    if thread_done:
        print("Operation completed successfully")
    else:
        _thread.exit()  # Abort the thread
        print("Operation aborted due to timeout")

execute_with_timeout()
