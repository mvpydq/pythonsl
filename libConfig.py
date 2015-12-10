import urlparse


# get conf from file
def ini_file_conf(file_in):
    cfg_hash = {}
    file_obj = open(file_in, 'r')

    key = ""    
    last_key = ""
    count = 0
    current = cfg_hash
    key_map = {}
    for line in file_obj:
        if line == "\n" or line[0] == "#":
            continue
                
        if line[0] == "[" and line[-2] == "]":                        
            tmp_key = line[1:-2]
            level = tmp_key.count(".")
            has_child = tmp_key.count("@")
            if level == 0:
                cfg_hash[tmp_key] = {}                
                current = cfg_hash[tmp_key]
                key_map[level] = current
            else:                
                current = key_map[level - 1]
                if has_child > 0:                         
                    tmp = tmp_key.replace(".", "")
                    tmp = tmp.replace("@", "")
                    try:
                        current[tmp].append({})                    
                    except:
                        current[tmp] = []
                        current[tmp].append({})     
                    current = current[tmp][-1]
                    key_map[level] = current
    
                elif tmp_key.count(".") > 0:
                    tmp = tmp_key.replace(".", "")
                    current[tmp] = {}                
                    current = current[tmp] 
                    key_map[level] = current
                                        
            continue
            
        tmp = line.split("=")                                                
        if line[0] == "@":            
            item_key = tmp[0][1:].strip()
            
            if item_key not in current:
                current[item_key] = []
                            
            current[item_key].append(tmp[1].strip())                                    
        else:            
            current[tmp[0].strip()] = tmp[1].strip()
                    
    file_obj.close()    
    return cfg_hash


# get conf from string
def args_conf(args):
    conf = urlparse.parse_qs(args)
    for key in conf.keys():
        conf[key] = conf.get(key)[0]
    return conf