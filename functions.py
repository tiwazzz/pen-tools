import platform
import cpuinfo
import psutil

aboutCpuInfo = cpuinfo.get_cpu_info()

def byteToGb(getByte):
    covertedGb = float(getByte)
    covertedGb = round(covertedGb*(10**-9), 2) 
    return covertedGb

def byteToMb(getByte):
    covertedMb = float(getByte)
    covertedMb = round(covertedMb*(10**-8), 2)
    return covertedMb
    
def getActsClockSpeed():
    try:
        actHz = byteToGb(aboutCpuInfo['hz_actual'])
    except Exception as error:
        actHz = "**:octagonal_sign: libary not support**"
        print(f"Error Message: {error}")
    return actHz

def getAdsClockSpeed():
    try:
        adsHz = byteToGb(aboutCpuInfo['hz_advertized'])
    except Exception as error:
        adsHz = "**:octagonal_sign: libary not support**"
        print(f"Error Message: {error}")
    return adsHz

def getCpuL1():
    try:
        cpuL1cache = byteToMb(aboutCpuInfo['l1_data_cache_size'])
    except Exception as error:
        cpuL1cache = "**:octagonal_sign: libary not support**"
        print(f"Error Message: {error}")
    return cpuL1cache

def getCpuL2():
    try:
        cpuL2cache = byteToMb(aboutCpuInfo['l2_cache_size'])
    except Exception as error:
        cpuL2cache = "**:octagonal_sign: libary not support**"
        print(f"Error Message: {error}")
    return cpuL2cache

def getCpuL3():
    try:
        cpuL3cache = byteToMb(aboutCpuInfo['l3_cache_size'])
    except Exception as error:
        cpuL3cache = "**:octagonal_sign: libary not support**"
        print(f"Error Message: {error}")
    return cpuL3cache

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

def getDiskRaw():
    try:
        if platform.uname == "Windows":
            diskTotal = byteToGb(psutil.disk_usage("C://"))
        else:
            diskTotal = byteToGb(psutil.disk_usage("/"))
    except Exception as error:
        diskTotal = "**:octagonal_sign: libary not support**"
        print(f"Error Message: {error}")
    return diskTotal

def getDiskTotal():
    diskTotal = getDiskRaw['total']
    diskTotal = byteToGb(diskTotal)
    return diskTotal

# def getDiskUsage():
#     diskUsed = getDiskRaw['used']
#     diskUsed = byteToGb(diskUsed)
#     return diskUsed

print(psutil.disk_usage("/").free)