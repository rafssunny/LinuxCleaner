from src.core.cleaner import *

def chooseSystemCleaningType(journalctl, varcrash, cache, fccache):
    if journalctl.get() == 'on' and varcrash.get() == 'on' and cache.get() == 'on' and fccache.get() == 'on':
            clearAllSystemCache()
    else:
        clearSelectedSystemCache(journalctl, varcrash, cache, fccache)
        
def choosePackagesCleaningType(apt, pacman, dnf, zypper):
    if apt.get() == 'on' and pacman.get() == 'on' and dnf.get() == 'on' and zypper.get() == 'on':
        clearAllPackagesCache()
    else:
        pass

def selectGeneralCleaningOrganization(journalctl, varcrash, cache, fccache, apt, pacman, dnf, zypper):
        chooseSystemCleaningType(journalctl, varcrash, cache, fccache)
        choosePackagesCleaningType(apt, pacman, dnf, zypper)