import system_cmd

def concat:
    ts =  bash("openssl  aes-128-cbc -d -in /Users/chy/Downloads/file_ts/v.f230.ts -out fijlde.ts -nosalt -iv 00000000000000000000000000000000 -K B8E34B28C9C05845D0973A12F2BA3B6A")
    return  ts

ts_list = [] 

for i in ts_list:
    concat(i)
    ts_list.add(i)
return ts_list
