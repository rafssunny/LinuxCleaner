import sys
from linuxcleaner.interfaces.cli import start_cli
from linuxcleaner.interfaces.gui import start_gui


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  linux-cleaner cli")
        print("  linux-cleaner gui")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "cli":
        start_cli()
    elif mode == "gui":
        start_gui()
    else:
        print(f"Unknown mode: {mode}")
        print("Use 'cli' or 'gui'")
