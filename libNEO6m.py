"""
By SiriusBrightstar: https://github.com/SiriusBrightstar
Initial Commit. 
This code can decode NMEA messages but this is still under development.
"""


def decode(coord):
    l = list(coord)
    for i in range(0,len(l)-1):
            if l[i] == "." :
                    break
    base = l[0:i-2]
    degi = l[i-2:i]
    degd = l[i+1:]
    #print(base,"   ",degi,"   ",degd)
    baseint = int("".join(base))
    degiint = int("".join(degi))
    degdint = float("".join(degd))
    degdint = degdint / (10**len(degd))
    degs = degiint + degdint
    full = float(baseint) + (degs/60)
    return full

def latitude(nmea):
    if nmea[0:6] == "$GPGGA":
        x = nmea.split(",")
        if x[7] == '0' or x[7]=='00':
            print ("Incorrect Data")
            return
        lati = decode(x[2])
        return lati

def longitude(nmea):
    if nmea[0:6] == "$GPGGA":
        x = nmea.split(",")
        if x[7] == '0' or x[7]=='00':
            print ("Incorrect Data")
            return
        lon = decode(x[4])
        return lon

def time(nmea):
    if nmea[0:6] == "$GPGGA":
        x = nmea.split(",")
        if x[7] == '0' or x[7]=='00':
            print ("Incorrect Data")
            return
        t = x[1][0:2] + ":" + x[1][2:4] + ":" + x[1][4:6]
        return t

def satellite(nmea):
    if nmea[0:6] == "$GPGGA":
        x = nmea.split(",")
        if x[7] == '0' or x[7]=='00':
            print ("Incorrect Data")
            return
        s = int(x[7])
        return s

def altitude(nmea):
    if nmea[0:6] == "$GPGGA":
        x = nmea.split(",")
        if x[7] == '0' or x[7]=='00':
            print ("Incorrect Data")
            return
        alt = x[9]
        return alt

def hemisphere(nmea):
    if nmea[0:6] == "$GPGGA":
        x = nmea.split(",")
        if x[7] == '0' or x[7]=='00':
            print ("Incorrect Data")
            return
        hemi = x[3]+x[5]
        return hemi
