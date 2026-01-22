from linuxcleaner.core.cleaner import *

#system
def chooseSystemCleaningType(journalctl, varcrash, cache, fccache, trash):
    if all(system.get() == 'on' for system in (journalctl, varcrash, cache, fccache, trash)):
            clearAllSystemCache()
    else:
        clearSelectedSystemCache(journalctl, varcrash, cache, fccache, trash)

# packages 
def choosePackagesCleaningType(apt, pacman, dnf, zypper, flatpak):
    if all(pkg.get() == 'on' for pkg in (apt, pacman, dnf, zypper, flatpak)):
        clearAllPackagesCache()
    else:
        clearSelectedPackagesCache(apt, pacman, dnf, zypper, flatpak)
        
# both 
def selectGeneralCleaningOrganization(journalctl, varcrash, cache, fccache, trash, apt, pacman, dnf, zypper, flatpak):
    chooseSystemCleaningType(journalctl, varcrash, cache, fccache, trash)
    choosePackagesCleaningType(apt, pacman, dnf, zypper, flatpak)