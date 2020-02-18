def printSize(total_bytes):
    size_kb=total_bytes/1024
    size_mb=size_kb/1024
    size_gb=size_mb/1024
    UNIT=""
    str_sizze=""
    if total_bytes<1024:
        UNIT="Bytes"
        str_sizze=total_bytes
    elif size_kb<1024:
        UNIT="KB"
        str_sizze=size_kb
    elif size_mb<1024:
        UNIT="MB"
        str_sizze=size_mb
    else:
        UNIT="GB"
        str_sizze=size_gb
    str_sizze="%.2f"%str_sizze
    print(f"Total Size : {str_sizze} {UNIT}")
def getSize(total_bytes):
    size_kb=total_bytes/1024
    size_mb=size_kb/1024
    size_gb=size_mb/1024
    UNIT=""
    str_sizze=""
    if total_bytes<1024:
        UNIT="Bytes"
        str_sizze=total_bytes
    elif size_kb<1024:
        UNIT="KB"
        str_sizze=size_kb
    elif size_mb<1024:
        UNIT="MB"
        str_sizze=size_mb
    else:
        UNIT="GB"
        str_sizze=size_gb
    str_sizze="%.2f"%str_sizze
    return UNIT,str_sizze

if __name__=="__main__":
    print("import getbytes.py and run printSize(total bytes)")