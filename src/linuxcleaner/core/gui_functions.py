from src.core.cleaner import *

#system
def chooseSystemCleaningType(journalctl, varcrash, cache, fccache):
    if all(system.get() == 'on' for system in (journalctl, varcrash, cache, fccache)):
            clearAllSystemCache()
    else:
        clearSelectedSystemCache(journalctl, varcrash, cache, fccache)

# packages 
def choosePackagesCleaningType(apt, pacman, dnf, zypper):
    if all(pkg.get() == 'on' for pkg in (apt, pacman, dnf, zypper)):
        clearAllPackagesCache()
    else:
        clearSelectedPackagesCache(apt, pacman, dnf, zypper)
        
# both 
def selectGeneralCleaningOrganization(journalctl, varcrash, cache, fccache, apt, pacman, dnf, zypper):
    chooseSystemCleaningType(journalctl, varcrash, cache, fccache)
    choosePackagesCleaningType(apt, pacman, dnf, zypper)