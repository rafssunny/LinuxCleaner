import subprocess

# find the first terminal available
def detectTerminal():
    terminals = ['gnome-terminal', 'konsole', 'kitty', 'alacritty', 'wezterm', 'ghostty', 'foot', 'tilix', 'terminator', 'guake', 'yakuake']
    for t in terminals:
        try:
            resultado = subprocess.run(
                ['which', t],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            if resultado.returncode == 0:
                return t
        except:
            pass

# select values to clear
def getSelectedValues(values_dict):
    on_variables = []
    for name, var in values_dict.items():
        if var.get() == 'on':
            on_variables.append(name)
    return on_variables

def clearSelectedValues(selected_variables):
    expression = '; '.join(value for value in selected_variables) + '; echo; read -p "Cleaning completed";'
    subprocess.Popen([
        detectTerminal(),
        '--',
        'bash', '-c',
        expression
    ])

# system 
def clearAllSystemCache():
    subprocess.Popen([
        detectTerminal(),
        '--',
        'bash', '-c',
        """
        sudo journalctl --vacuum-time=7d; rm -rf ~/.cache/*; sudo rm -rf /var/crash/*; fc-cache -r; rm -rf ~/.local/share/Trash/*; echo; read -p "Cleaning completed";
        """
    ])

def clearSelectedSystemCache(journalctl, varcrash, cache, fccache, trash):
    selected_variables = getSelectedValues(
        {
            'sudo journalctl --vacuum-time=7d':journalctl,
            'sudo rm -rf /var/crash/*':varcrash,
            'rm -rf ~/.cache/*':cache,
            'fc-cache -r':fccache,
            'rm -rf ~/.local/share/Trash/*':trash
        }
    )
    clearSelectedValues(selected_variables)

# packages 
def clearAllPackagesCache():
    subprocess.Popen([
        detectTerminal(),
        '--',
        'bash', '-c',
        """
        sudo apt clean; sudo pacman -Sc; sudo dnf clean all; sudo zypper clean; flatpak uninstall --unused; echo; read -p "Cleaning completed";
        """
    ])

def clearSelectedPackagesCache(apt, pacman, dnf, zypper, flatpak):
    selected_variables = getSelectedValues(
        {
            'sudo apt clean':apt,
            'sudo pacman -Sc':pacman,
            'sudo dnf clean all':dnf,
            'sudo zypper clean':zypper,
            'flatpak uninstall --unused':flatpak
        }
    )
    clearSelectedValues(selected_variables)