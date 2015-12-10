import socket
import math
import re
import urlparse


# get local ip
def get_local_ip():
    hostname = socket.getfqdn(socket.gethostname())    
    ip_addr = socket.gethostbyname(hostname)
    return ip_addr


# check local ip if in ip array
def is_valid_ip_from_arr(ip_arr):
    local_ip = get_local_ip()
    if local_ip in ip_arr:
        return True
    return False    


# check local ip if valid from file
def is_valid_ip_from_file(ip_file):
    try:
        fobj = open(ip_file)
        ip_arr = []
        for line in fobj:
            if not line:
                continue
            ip_arr.append(line.strip())
        return is_valid_ip_from_arr(ip_arr)
    except:
        return False


# convert ip string to array
def ip_str_to_arr(ip_str):
    try:
        res = str(ip_str).split(".")
        if len(res) != 4:
            return None
        return res
    except:
        return None


# convert ip to a number
def ip_str_to_num(ip_str):
    ip_arr = ip_str_to_arr(ip_str)
    if ip_arr is None:
        return -1
    
    ip_num = 0
    for i in range(0, 4):
        ip_num += int(ip_arr[i]) * int(math.pow(256, 3 - i))
        
    return ip_num


# compare ip string
def ip_str_compare(ip_str1, ip_str2):
    ip_num1 = ip_str_to_num(ip_str1)
    ip_num2 = ip_str_to_num(ip_str2)
    
    return ip_num_compare(ip_num1, ip_num2)


# compare ip num
def ip_num_compare(ip_num1, ip_num2):
    if ip_num1 > ip_num2:
        return 1
    elif ip_num1 == ip_num2:
        return 0
    return -1


# convert ip to location
def ip_to_loc(ip_str, loc_map, is_sort=True):
    if is_sort is False:
        key_map = sorted(loc_map.keys(), ip_num_compare, None, True)
    else:
        key_map = loc_map.keys()

    ip_num = ip_str_to_num(ip_str)
    for key in key_map:
        key = int(key)
        if ip_num >= key:
            return loc_map[key]
        
    return -1