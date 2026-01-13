from src.core.cleaner import *

def chooseSystemCleaningType(journalctl, varcrash, cache, fccache):
    if journalctl.get() == 'on' and varcrash.get() == 'on' and cache.get() == 'on' and fccache.get() == 'on':
            clearAllSystemCache()
    else:
        clearSelectedSystemCache(journalctl, varcrash,cache, fccache)
        
def choosePackagesCleaningType():
    pass

