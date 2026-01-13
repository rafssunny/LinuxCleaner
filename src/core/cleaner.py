import subprocess

def detectTerminal():
    terminals = ['gnome-terminal', 'konsole', 'kitty', 'alacritty']
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

# system 
def clearAllSystemCache():
    subprocess.Popen([
        detectTerminal(),
        '--',
        'bash', '-c',
        """
        sudo journalctl --vacuum-time=7d; sudo rm -rf ~/.cache/*; sudo rm -rf /var/crash/*; fc-cache -r; echo; read -p "Cleaning completed";
        """
    ])

def getSelectedSystemCache(values_dict):
    on_variables = []
    for name, var in values_dict.items():
        if var.get() == 'on':
            on_variables.append(name)
    return on_variables

def clearSelectedSystemCache(journalctl, varcrash, cache, fccache):
    selected_variables = getSelectedSystemCache(
        {
            'sudo journalctl --vacuum-time=7d':journalctl,
            'sudo rm -rf /var/crash/*':varcrash,
            'sudo rm -rf ~/.cache/*':cache,
            'fc-cache -r':fccache
        }
    )
    expression = '; '.join(value for value in selected_variables) + '; echo; read -p "Cleaning completed";'
    subprocess.Popen([
        detectTerminal(),
        '--',
        'bash', '-c',
        expression
    ])

# packages 
def clearAllPackagesCache():
    subprocess.Popen()([
        detectTerminal(),
        '--',
        'bash', '-c',
        """
        sudo apt clean; sudo pacman -Sc; sudo dnf clean all; sudo zypper clean
        """
    ])

def clearSelectedPackagesCache():
    pass