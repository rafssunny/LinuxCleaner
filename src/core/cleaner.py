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

def getSelectedSystemCache(values_dict):
    on_variables = []
    for name, var in values_dict:
        if var.get() == 'on':
            on_variables.append(name)
    return on_variables

def clearAllSystemCache():
    subprocess.Popen([
        detectTerminal(),
        "--",
        "bash", "-c",
        """
        sudo journalctl --vacuum-time=7d; sudo rm -rf ~/.cache/*; sudo rm -rf /var/crash/*; fc-cache -r; echo; read -p Cleaning completed;
        """
    ])

def clearSelectedSystemCache():
    selected_variables = getSelectedSystemCache(
        {
            'journalctl':journalctl,
            'varcrash':varcrash,
            'cache':cache,
            'fccache':fccache
        }
    )
