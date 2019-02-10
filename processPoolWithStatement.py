import concurrent.futures
import datetime
import requests
import os
from subprocess import Popen, PIPE
import signal
URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://becollege.org/',
        'http://abc.net.au/']


def stop_process_pool(executor):
    print('Inside stop_process_pool')
    for pid, process in executor._processes.items():
        print(pid)
        print(process)
        process.terminate()
    check_processes_status(executor)
    executor.shutdown()


def check_processes_status(executor):
    print('Inside check_processes_status')
    import time
    time.sleep(3)
    for pid, process in executor._processes.items():
        print(pid)
        print(process)


# Retrieve a single page and report the url and contents
def load_url(url, **kwargs):
    timeout = None
    if kwargs['timeout'] is not None:
        timeout = kwargs['timeout']
    print(timeout)
    response = ''
    print('Loading URL {} '.format(url))
    try:
        if 'becollege' in url:
            import time
            time.sleep(35)
            print('Inside be college loop@@@@')
            response = requests.get(url, timeout=timeout)
        else:
            # import time
            # time.sleep(30)
            print('Inside else loop@@@@')
            response = requests.get(url, timeout=timeout)
    except Exception as e:
        response = ''
        print(e)
    finally:
        if '' not in response:
            return str(response.status_code)

def kill_processes(main_pid):
    print('Inside kill process')
    print('Main PID : '+str(main_pid))
    process = Popen(['ps', '-eo', 'pid,args'], stdout=PIPE, stderr=PIPE)
    stdout, notused = process.communicate()
    pidList = []
    for line in stdout.splitlines():
        pid, cmdline = line.split(' ', 1)
        if __file__.split('/')[-1] in cmdline and str(pid) !=str(main_pid):
            print pid
            print cmdline
            pidList.append(int(pid))
    print(pidList)
    for proc_id in pidList:
        os.kill(int(proc_id), signal.SIGTERM)

def jobs_processing_paralell(list_URL, timeout_to_request, timeout_function):
    output = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=len(list_URL)) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url, timeout=timeout_to_request): url for url in list_URL}
        try:
            for future in concurrent.futures.as_completed(future_to_url, timeout_function):
                data = future.result()
                output.append(data)
                print('Output inside loop:')
                print(data)
        except concurrent.futures._base.TimeoutError as exc:
            print('%r generated an exception: {}'.format(exc))
            executor.shutdown(wait=False)
        finally:
            return output

def exit_gracefully(pid):
    os.kill(pid,signal.SIGTERM)

def main():
    # We can use a with statement to ensure threads are cleaned up promptly
    time_start = datetime.datetime.now()
    print('started:  {}'.format(time_start))
    output = []
    TIMEOUT_FUNC = 10
    TIMEOUT_REQUEST = 5
    MAIN_PID = os.getpid()
    output = jobs_processing_paralell(list_URL=URLS, timeout_to_request=TIMEOUT_REQUEST, timeout_function=TIMEOUT_FUNC)
    print('Output here')
    print(output)
    kill_processes(MAIN_PID)
    if len(output) == 0:
        print('There is no response from the request!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return
    time_end = datetime.datetime.now()
    print('Time Taken :' + str(time_end - time_start))
    exit_gracefully(MAIN_PID)


if __name__ == "__main__":
    main()
