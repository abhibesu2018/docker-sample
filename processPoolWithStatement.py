import concurrent.futures
import datetime
import requests

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://becollege.org/',
        'http://abc.net.au/']


def stop_process_pool(executor):
    for pid, process in executor._processes.items():
        process.terminate()
    executor.shutdown()




# Retrieve a single page and report the url and contents
def load_url(url, timeout):
    print(timeout)
    response  = ''
    try:
        if 'becollege' in url:
            response = requests.get(url, timeout=0.01)
        else:
            response = requests.get(url, timeout=timeout)
    except Exception as e:
        response = ''
        print(e)
    finally:
        if '' not in response:
            return str(response.status_code)


# We can use a with statement to ensure threads are cleaned up promptly
time_start = datetime.datetime.now()
print(time_start)
output = []
with concurrent.futures.ThreadPoolExecutor(max_workers=len(URLS)) as executor:
# Start the load operations and mark each future with its URL
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=len(URLS))
    future_to_url = {executor.submit(load_url, url, 10): url for url in URLS}
    try:
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]

            data = future.result()
            output.append(data)
            print('Output inside loop:')
            print(data)
    except Exception as exc:
        print(exc)
        print('%r generated an exception: %s' % (url, exc))
        stop_process_pool(executor)
    else:
        print('%r page is %d bytes' % (url, len(str(data))))

    finally:
        print('Output here')
        print(output)
        time_end = datetime.datetime.now()
        print('Time Taken :' + str(time_end - time_start))
