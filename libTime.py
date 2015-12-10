import time
import pytz
import datetime

DATE_FLAG = "%Y%m%d"
DATE_ONLY = "%Y-%m-%d"
DATETIME_FLAG = "%Y%m%d%H%M"
FULL_DATETIME = "%Y-%m-%d %H:%M:%S"
TIME_FLAG = "%H%M"
TIME_ONLY = "%H:%M:%S"


# get china time zone
def get_timezone():
    return pytz.timezone('Asia/Shanghai')


# time string format detect, maybe not correct
def simple_format_detect(time_str):
    tmp = time_str.split(" ")
    if len(tmp) > 2:
        return "unknown"
    
    if len(tmp) == 2:
        if len(tmp[0].split("-")) == 3:
            date = "%Y-%m-%d"
        else:
            date = "%Y%m%d"
        
        hour_len = len(tmp[1].split(":"))
        if hour_len == 3:
            hour = "%H:%M:%S"
        elif hour_len == 2:
            hour = "%H:%M"
        elif hour_len == 1:
            if len(tmp[1]) == 6:
                hour = "%H%M%S"
            elif len(tmp[1]) == 4:
                hour = "%H%M"
            else:
                return "unknown"
            
        return date + " " + hour            
    else:
        date_tmp = time_str.split("-")
        if len(date_tmp) > 3:
            return "unknown"        
        if len(date_tmp) == 3:
            return "%Y-%m-%d"
        if len(date_tmp) == 2:
            return "%Y-%m"        
        
        time_tmp = time_str.split(":")
        if len(time_tmp) == 3:
            return "%H:%M:%S"        
        if len(time_tmp) == 1:
            if len(time_str) == 12:
                return "%Y%m%d%H%M"
            elif len(time_str) == 8:
                return "%Y%m%d"                       
            return "unknown"  
        
        return "unknown"


# convert time string to timestamp
def str_to_timestamp(time_str, tformat=FULL_DATETIME):
    try:        
        stime = time.strptime(time_str, tformat)
    except:
        tformat = simple_format_detect(time_str)
        if tformat == "unknown":
            return 0
        
        try:
            stime = time.strptime(time_str, tformat)
        except:
            return 0
        
    return int(time.mktime(stime))


# convert time string to datetime
def str_to_datetime(time_str, tformat=FULL_DATETIME):
    try:        
        dt = datetime.datetime.strptime(time_str, tformat)
    except:
        tformat = simple_format_detect(time_str)
        if tformat == "unknown":
            return None
        
        try:
            dt = datetime.datetime.strptime(time_str, tformat)
        except:
            return None
        
    return dt    


# convert time string to time
def str_to_time(time_str, tformat=FULL_DATETIME):
    try:        
        t = time.strptime(time_str, tformat)
    except:
        tformat = simple_format_detect(time_str)
        if tformat == "unknown":
            return None
        
        try:
            t = time.strptime(time_str, tformat)
        except:
            return None
        
    return t    


# convert timestamp to datetime
def timestamp_to_datetime(timestamp):
    dt = datetime.datetime.utcfromtimestamp(timestamp)
    dt = dt + datetime.timedelta(hours=8)
    return dt


# convert time string format by self defined
def str_convert_by_defined(time_str, to_format, from_format=FULL_DATETIME):
    dt = str_to_datetime(time_str, from_format)
    if dt is None:
        return "frominvalid"
    try:
        return dt.strftime(to_format)
    except:
        return "toinvalid"


# convert time string format to date flag format
def str_to_dateflag(time_str, from_format=FULL_DATETIME):
    return str_convert_by_defined(time_str, DATE_FLAG, from_format)


# convert time string format to date int format
def str_to_dateint(time_str, from_format=FULL_DATETIME):
    return str_convert_by_defined(time_str, DATE_ONLY, from_format)


# convert time string format to date time flag format
def str_to_datetimeflag(time_str, from_format=FULL_DATETIME):
    return str_convert_by_defined(time_str, DATETIME_FLAG, from_format)


# convert time string format to full date time format
def str_to_fulldatetime(time_str, from_format=FULL_DATETIME):
    return str_convert_by_defined(time_str, FULL_DATETIME, from_format)


# convert time string format to time flag format
def str_to_timeflag(time_str, from_format=FULL_DATETIME):
    return str_convert_by_defined(time_str, TIME_FLAG, from_format)


# convert time string format to time only format
def str_to_timeonly(time_str, from_format=FULL_DATETIME):
    return str_convert_by_defined(time_str, TIME_ONLY, from_format)