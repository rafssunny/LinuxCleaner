from src.core.cleaner import *

def chooseSystemCleaningType(value1, value2, value3, value4):
    if value1.get() == 'on' and value2.get() == 'on' and value3.get() == 'on' and value4.get() == 'on':
            clearAllSystemCache()
    else:
        clearSelectedSystemCache()
        
def choosePackagesCleaningType():
    pass
