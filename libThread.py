import threading


# simple base thread class
class BaseThread(threading.Thread):
    _tname = ""
    _lock = None
    _run_func = None
    _sync = True
    
    def __init__(self, name, rf = None, _sync = True):
        threading.Thread.__init__(self)
        self._tname = name
        self._lock = threading.Lock()
        self._run_func = rf
        self._sync = _sync
        
    def run(self):        
        if self._sync:
            self._lock.acquire()
            
        if callable(self._run_func):
            self._run_func(self.name)
            
        if self._sync:
            self._lock.release()
    
#def test(i):
    #print i
    
#threads = []
#for i in range(0,10):
    #threads.append(BaseThread("thread" + str(i), test))
    
#for t in threads:
    #t.start()
    
#for t in threads:
    #t.join()
    
    
        
        