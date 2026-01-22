from linuxcleaner.core.cleaner import *

def start_cli():
    user_input = ''
    print('type help for get the commands list')

    while user_input != 'exit':
        user_input = str(input('> ')).lower()

        if user_input == 'help':
            print(
                'cl all : Clean All System and Packages cache\n'
                'cl sy  : Clean All System Cache\n'
                'cl pk  : Clean All Packages cache\n'
                'exit  : Close the program'
            )

        elif user_input == 'cl all':
            clearAllSystemCache()
            clearAllPackagesCache()

        elif user_input == 'cl sy':
            clearAllSystemCache()

        elif user_input == 'cl pk':
            clearAllPackagesCache()

        elif user_input == 'exit':
            break

    print('bye bye :)')


if __name__ == "__main__":
    start_cli()
