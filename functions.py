import psutil

def byteToGb(getByte):
    covertedGb = int(getByte)
    covertedGb = round(covertedGb*(10**-9), 2) 
    return covertedGb

def byteToMb(getByte):
    covertedMb = int(getByte)
    covertedMb = round(covertedMb*(10**-8), 2)
    return covertedMb

def getRamTotal():
    try:
        ramTotal = byteToGb(psutil.virtual_memory().total)
    except Exception as error:
        ramTotal = "**:octagonal_sign: libary not support**"
        print(f"Error Message: {error}")
    return ramTotal

def getRamSwap():
    try:
        swapRam = byteToGb(psutil.swap_memory().total)
    except Exception as error:
        swapRam = byteToGb(psutil.swap_memory().total)
        print(f"Error Message: {error}")
    return swapRam