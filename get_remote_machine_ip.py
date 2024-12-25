# Sometimes, you need to translate a machine's hostname into its corresponding IP address,
# for example, a quick domain name lookup. This recipe introduces a simple function to do
# that
import socket
def get_remote_machine_info():
    remote_host = 'www.google.com'
    try:
        print ("IP address of %s: %s" %(remote_host,
        socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print ("%s: %s" %(remote_host, err_msg))
if __name__ == '__main__':
    get_remote_machine_info()