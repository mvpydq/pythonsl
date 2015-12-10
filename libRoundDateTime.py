import math
import libTime
import datetime


# a util class to get round time
class LibRoundDateTime:
    TIME_UNIT_MINUTE = 1
    TIME_UNIT_HOUR = 2
    
    MODEL_EALIER = 1
    MODEL_LATER = 2
    
    ROUND_BASE = 5
    ROUND_TIME_FORMAT = "%Y%m%d_%H%M"
    
    _start = 0
    _round_time = 0
    _unit = 0
    _model = 0
    _current = None
    _time_format = ""
    
    def __init__(self, s, r, u, m, sf):
        self._start = s
        self._round_time = r
        self._unit = u
        self._model = m
        self._time_format = sf
        self.round_init()
        
    def round_init(self):
        self._round_time = math.ceil(int(self._round_time) / self.ROUND_BASE) * self.ROUND_BASE
        minute = int(libTime.strConvertByDefined(self._start, "%M", self._time_format))
        if int(self._model) == self.MODEL_EALIER:
            _startMinute = int(math.floor(minute / self._round_time) * self._round_time)
        else:
            _startMinute = int(math.ceil(minute / self._round_time) * self._round_time)
        _startMinute = "%02d" % _startMinute
            
        _currentStr = libTime.strConvertByDefined(self._start, "%Y%m%d %H", self._time_format) + _startMinute        
        self._current = libTime.strToDateTime(_currentStr, "%Y%m%d %H%M")
        
    def next(self):
        res = self._current.strftime(self.ROUND_TIME_FORMAT)
        if self._unit == self.TIME_UNIT_MINUTE:
            self._current = self._current + datetime.timedelta(minutes=self._round_time)
        else:
            self._current = self._current + datetime.timedelta(hours=self._round_time)
        return res
        
        
# lib = LibRoundDateTime("20151209 13:07", 5, LibRoundDateTime.TIME_UNIT_HOUR, LibRoundDateTime.MODEL_LATER, "%Y%m%d %H%M")
# print lib.next()
# print lib.next()
# print lib.next()
# print lib.next()

        
        
    