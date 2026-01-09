from customtkinter import * 

set_appearance_mode("dark")

# config root
root = CTk()
root.title('LinuxCleaner')
root.geometry('600x400')
root.resizable(False, False)

# labels configs
title_label = CTkLabel(root, text='LinuxCleaner', font=('Arial', 50))
title_label.pack()

#frames configs 
main_frame = CTkFrame(root, fg_color='transparent')
main_frame.pack(pady=20, padx=20, fill='both', expand=True)

system_labels_frame = CTkFrame(main_frame, width=100, height=100)
system_labels_frame.pack(side='left', padx=(0,10), fill='both', expand =True)

packages_labels_frame = CTkFrame(main_frame, width=100, height=100)
packages_labels_frame.pack(side='left', padx=(10,0), fill='both', expand=True)

# menu system config
system_cache_label = CTkLabel(system_labels_frame, text='System Cache', font=('Arial', 15))
system_cache_label.pack()

system_tmp = CTkCheckBox(system_labels_frame, text='/tmp/*')
system_tmp.pack()

system_var_tmp = CTkCheckBox(system_labels_frame, text='/var/tmp/*')
system_var_tmp.pack()

system_cache = CTkCheckBox(system_labels_frame, text='~/.cache/*')
system_cache.pack()

system_logs = CTkCheckBox(system_labels_frame, text='/var/log')
system_logs.pack()

# menu packages config
packages_manager_cache_label = CTkLabel(packages_labels_frame, text='Packages Cache', font=('Aria', 15))
packages_manager_cache_label.pack()

packages_apt = CTkCheckBox(packages_labels_frame, text='/var/cache/apt/archives')
packages_apt.pack()

packages_pacman = CTkCheckBox(packages_labels_frame, text='/var/cache/pacman/pkg')
packages_pacman.pack()

packages_dnf = CTkCheckBox(packages_labels_frame, text='/var/cache/dnf')
packages_dnf.pack()

packages_zypper = CTkCheckBox(packages_labels_frame, text='/var/cache/zypp')
packages_zypper.pack()

#buttons
execute_button = CTkButton(root, text='Clean')
execute_button.pack(pady=30)

root.mainloop()