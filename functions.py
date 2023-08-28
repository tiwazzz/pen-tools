def byteToGb(getByte):
    covertedGb = int(getByte)
    covertedGb = round(covertedGb*(10**-9), 2) 
    return covertedGb

def byteToMb(getByte):
    covertedMb = int(getByte)
    covertedMb = round(covertedMb*(10**-8), 2)
    return covertedMb

def cpuChecker():
    return None