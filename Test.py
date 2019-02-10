import psutil
def get_process(proc_name):
    """Get process given  string in
    process cmd line.
    """
    #LOG = log.getLogger(__name__)
    procList = []
    try:
        for pr in psutil.process_iter():
            for args in pr.cmdline():
                if proc_name in args:
                    print(args)
                    procList.append(pr.pid)
        return procList
    except BaseException as e:
        print("Error in fetching process: {}".format(e))
    return None

p = get_process('py')
print(p)