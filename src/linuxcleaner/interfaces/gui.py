from customtkinter import * 
from PIL import Image
from linuxcleaner.core.gui_functions import selectGeneralCleaningOrganization

def start_gui():
    set_appearance_mode("dark")
    # config root
    root = CTk()
    root.title('LinuxCleaner')
    root.geometry('600x400')
    root.resizable(False, False)

    # color variables
    dark_green = '#006400'
    green = '#009900'

    # variables checkbox
    journalctl = StringVar(value='on') 
    varcrash = StringVar(value='on') 
    cache = StringVar(value='on') 
    fccache = StringVar(value='on') 
    apt = StringVar(value='off') 
    pacman = StringVar(value='off') 
    dnf = StringVar(value='off') 
    zypper = StringVar(value='off') 

    # labels configs
    tux_img = CTkImage(dark_image=Image.open('./assets/imgs/tux.png'), size=(100,100))
    title_label = CTkLabel(root, text='LinuxCleaner', font=('Arial', 50, 'bold', 'italic'), image=tux_img, compound='right')
    title_label.pack()

    #frames configs 
    main_frame = CTkFrame(root, fg_color='transparent')
    main_frame.pack(pady=15, padx=20, fill='both', expand=True)

    system_labels_frame = CTkFrame(main_frame, width=100, height=100)
    system_labels_frame.pack(side='left', padx=(0,10), fill='both', expand =True)

    packages_labels_frame = CTkFrame(main_frame, width=100, height=100)
    packages_labels_frame.pack(side='left', padx=(10,0), fill='both', expand=True)

    # menu system config GUI 
    system_cache_label = CTkLabel(system_labels_frame, text='System Cache', font=('Arial', 20))
    system_cache_label.pack(pady=5)


    system_journalctl = CTkCheckBox(system_labels_frame, text='journalctl --vacuum-time=7d', variable = journalctl, onvalue='on', offvalue='off', fg_color=dark_green,hover_color=green)
    system_journalctl.pack(pady=5)

    system_varcrash = CTkCheckBox(system_labels_frame, text='/var/crash/*', variable = varcrash, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
    system_varcrash.pack(pady=5)

    system_cache = CTkCheckBox(system_labels_frame, text='~/.cache/*', variable = cache, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
    system_cache.pack(pady=5)

    system_fccache = CTkCheckBox(system_labels_frame, text='fc-cache -r', variable = fccache, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
    system_fccache.pack(pady=5)

    # menu packages config GUI
    packages_manager_cache_label = CTkLabel(packages_labels_frame, text='Packages Cache', font=('Aria', 20))
    packages_manager_cache_label.pack(pady=5)


    packages_apt = CTkCheckBox(packages_labels_frame, text='apt', variable = apt, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
    packages_apt.pack(pady=5)

    packages_pacman = CTkCheckBox(packages_labels_frame, text='pacman', variable = pacman, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
    packages_pacman.pack(pady=5)

    packages_dnf = CTkCheckBox(packages_labels_frame, text='dnf', variable = dnf, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
    packages_dnf.pack(pady=5)

    packages_zypper = CTkCheckBox(packages_labels_frame, text='zypper', variable =zypper, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
    packages_zypper.pack(pady=5)

    #buttons
    execute_button = CTkButton(root, text='Clean', font=('Arial', 25, 'bold'), compound='right', fg_color = dark_green, hover_color=green, command=lambda: selectGeneralCleaningOrganization(journalctl, varcrash, cache, fccache, apt, pacman, dnf, zypper))
    execute_button.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    start_gui()
