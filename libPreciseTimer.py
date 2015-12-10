import time
import threading


# a thread safe precise timer
class LibPreciseTimer:
    _pname = "default"
    # seconds
    _starts = 0
    _checks = 0
    # milliseconds
    _startms = 0
    _checkms = 0
    _mutex = threading.Lock()
    
    def __init__(self, name = "default"):
        self._pname = name
        
    def start(self):
        self._mutex.acquire()
        self._starts = int(time.time()) 
        self._startms = int(round(time.time() * 1000))        
        self._mutex.release()        
        
    def check(self): 
        self._mutex.acquire()
        self._checks = int(time.time()) 
        self._checkms = int(round(time.time() * 1000))        
        self._mutex.release()    
                
    def reset(self):
        self._mutex.acquire()
        self._starts = 0
        self._startms = 0
        self._checks = 0
        self._checkms = 0
        self._mutex.release()   
        
    def set_name(self, name):
        self._mutex.acquire()
        self._pname = name
        self._mutex.release()   
        
    def elapsed_sec(self):
        return self._checks - self._starts
    
    def elapsed_msec(self):
        return self._checkms - self._startms    