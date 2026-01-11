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

def clearSystemCache():
        execute_cleaning = subprocess.Popen([
            detectTerminal(),
            "--",
            "bash", "-c",
            """
            sudo journalctl --vacuum-time=7d; sudo rm -rf ~/.cache/*; sudo rm -rf /var/crash/*; fc-cache -r
            """
        ])

def clearSelected():
    pass
