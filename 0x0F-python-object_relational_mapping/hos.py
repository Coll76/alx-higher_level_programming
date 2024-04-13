import socket
import getpass
def main():
    hos = socket.gethostname()
    user = getpass.getuser()
    print('user', hos)
    print('host: ', user)
if __name__ == '__main__':
    main()

