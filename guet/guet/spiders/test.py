

def standard_info(info):
    if info is None:
        return ''
    
    if isinstance(info,str):
        info = info.strip()
        

    return info    


print(standard_info("123"))
print(standard_info(None))
print(standard_info([1,2,3,4]))