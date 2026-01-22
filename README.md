# Linux Cleaner
The goal of Linux Cleaner is to **make system cache cleaning easier**, since it is common to forget to clean our cache, which ends up taking up a large amount of disk space.
The program also includes the option to clean the cache of the system’s package managers, further helping to free up storage.

## Interfaces
The program provides both a **GUI** and a **CLI**, allowing the user to choose whichever is more comfortable for them.

## Stack
The program was developed entirely in **Python**. It uses the **subprocess** library to run system-level processes and the **customtkinter** and **Pillow** libraries for the GUI.

## How to install
Clone the repository and install the package using pip:

```bash
git clone https://github.com/rafssunny/LinuxCleaner.git
cd LinuxCleaner
python3 -m venv venv #or python -m venv venv
source venv/bin/activate
pip install .
```
After installation, the linux-cleaner command will be available system-wide.

## How to use
- CLI MODE
  ``linux-cleaner cli``
- GUI MODE
  ``linux-cleaner gui``
---

* *The program is open source, so feel free to contribute to the code :)*

---
## References
- ["OS Linux Icon"](https://www.iconarchive.com/show/simply-styled-icons-by-dakirby309/OS-Linux-icon.html) by dAKirby309 
