from customtkinter import * 
from PIL import Image

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
tmp = StringVar(value='on')
vartmp = StringVar(value='on')
cache = StringVar(value='on')
varlog = StringVar(value='on')
apt = StringVar(value='on')
pacman = StringVar(value='on')
dnf = StringVar(value='on')
zypp = StringVar(value='on')

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


system_tmp = CTkCheckBox(system_labels_frame, text='/tmp/*', variable = tmp, onvalue='on', offvalue='off', fg_color=dark_green,hover_color=green)
system_tmp.pack(pady=5)

system_var_tmp = CTkCheckBox(system_labels_frame, text='/var/tmp/*', variable = vartmp, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
system_var_tmp.pack(pady=5)

system_cache = CTkCheckBox(system_labels_frame, text='~/.cache/*', variable = cache, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
system_cache.pack(pady=5)

system_logs = CTkCheckBox(system_labels_frame, text='/var/log', variable = varlog, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
system_logs.pack(pady=5)

# menu packages config GUI
packages_manager_cache_label = CTkLabel(packages_labels_frame, text='Packages Cache', font=('Aria', 20))
packages_manager_cache_label.pack(pady=5)


packages_apt = CTkCheckBox(packages_labels_frame, text='/var/cache/apt/archives', variable = apt, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
packages_apt.pack(pady=5)

packages_pacman = CTkCheckBox(packages_labels_frame, text='/var/cache/pacman/pkg', variable = pacman, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
packages_pacman.pack(pady=5)

packages_dnf = CTkCheckBox(packages_labels_frame, text='/var/cache/dnf', variable = dnf, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
packages_dnf.pack(pady=5)

packages_zypper = CTkCheckBox(packages_labels_frame, text='/var/cache/zypp', variable =zypp, onvalue='on', offvalue='off', fg_color=dark_green, hover_color=green)
packages_zypper.pack(pady=5)

# warning label
warning_label = CTkLabel(root, text='Please close everything before starting the cleaning!', font=('Arial', 15, 'italic'))
warning_label.pack()

#buttons
execute_button = CTkButton(root, text='Clean', font=('Arial', 25, 'bold'), compound='right', fg_color = dark_green, hover_color=green)
execute_button.pack(pady=5)

root.mainloop()