from src.core.cleaner import *

user_input = ''
print('type help for get the commands list')

while user_input != 'exit':
    user_input = str(input('> ')).lower()
    if user_input == 'help':
        print('cl all  :  Clean All System and Packages cache\ncl sy  :  Clean All System Cache\ncl pk  :  Clean All Packages cache\nexit : Close the program')
    elif user_input == 'cl all':
        clearAllSystemCache()
        clearAllPackagesCache() 
    elif user_input == 'cl sy':
        clearSelectedSystemCache:()
    elif user_input == 'cl pk':
        clearAllPackagesCache()
    elif user_input == 'exit':
        break
print('bye bye :)')
