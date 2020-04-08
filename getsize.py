#!/usr/bin/env python

def printSize(total_bytes):  #print the size in both binary and decimal equivalent
    size_bin_kb=total_bytes/1024
    size_bin_mb=size_bin_kb/1024
    size_bin_gb=size_bin_mb/1024
    UNIT=""
    str_sizze=""
    if total_bytes<1024:
        UNIT="Bytes"
        str_sizze=total_bytes
    elif size_bin_kb<1024:
        UNIT="KB(binary)"
        str_sizze=size_bin_kb
    elif size_bin_mb<1024:
        UNIT="MB(binary)"
        str_sizze=size_bin_mb
    else:
        UNIT="GB(binary)"
        str_sizze=size_bin_gb
    str_sizze="%.2f"%str_sizze
    print(f"Total Size : {str_sizze} {UNIT}")
    #now for printing the decimal size 

    size_dec_kb=total_bytes/1000
    size_dec_mb=size_dec_kb/1000
    size_dec_gb=size_dec_mb/1000
    UNIT=""
    str_sizze=""
    if total_bytes<1000:
        UNIT="Bytes"
        str_sizze=total_bytes
    elif size_bin_kb<1000:
        UNIT="KB (Decimal)"
        str_sizze=size_dec_kb
    elif size_bin_mb<1000:
        UNIT="MB(Decimal)"
        str_sizze=size_dec_mb
    else:
        UNIT="GB(Decimal)"
        str_sizze=size_dec_gb
    str_sizze="%.2f"%str_sizze
    print(f"Total Size : {str_sizze} {UNIT}")

def getSizeDecimal(total_bytes): #return Size in Human Equivlanet system
    size_dec_kb=total_bytes/1000
    size_dec_mb=size_dec_kb/1000
    size_dec_gb=size_dec_mb/1000
    UNIT=""
    str_sizze=""
    if total_bytes<1000:
        UNIT="Bytes"
        str_sizze=total_bytes
    elif size_dec_kb<1000:
        UNIT="KB (Decimal)"
        str_sizze=size_dec_kb
    elif size_dec_mb<1000:
        UNIT="MB(Decimal)"
        str_sizze=size_dec_mb
    else:
        UNIT="GB(Decimal)"
        str_sizze=size_dec_gb
    str_sizze="%.2f"%str_sizze
    return UNIT,str_sizze

def getSizeBinary(total_bytes): #return the size in Binary Equivalent Size
    size_bin_kb=total_bytes/1024
    size_bin_mb=size_bin_kb/1024
    size_bin_gb=size_bin_mb/1024
    UNIT=""
    str_sizze=""
    if total_bytes<1024:
        UNIT="Bytes"
        str_sizze=total_bytes
    elif size_bin_kb<1024:
        UNIT="KB(binary)"
        str_sizze=size_bin_kb
    elif size_bin_mb<1024:
        UNIT="MB(binary)"
        str_sizze=size_bin_mb
    else:
        UNIT="GB(binary)"
        str_sizze=size_bin_gb
    str_sizze="%.2f"%str_sizze
    return UNIT,str_sizze

if __name__=="__main__":
    print("import getbytes.py and run printSize(total bytes)")
    r=input("Enter the total size in bytes")
    printSize(r)