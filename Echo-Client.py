import socket
import sys
from Crypto.Cipher import AES

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


# Encryption of message
def do_encrypt(message):
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(message)
    return ciphertext

# Decryption of message
def do_decrypt(ciphertext):
    obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    message = obj2.decrypt(ciphertext)
    return message

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 65432)
print >>sys.stderr, 'connecting to %s port %s' % server_address
s.connect(server_address)
try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    print >> sys.stderr, 'original: "%s"' % message
    print >> sys.stderr, 'encrypting message ...'
    message (message)
    print >> sys.stderr, 'sending "%s"' % message
    s.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = s.recv(16)
        amount_received += len(data)
        print >> sys.stderr, 'received "%s"' % data
        print >> sys.stderr, 'decrypting message ...'
        data = do_decrypt(data)
        print >> sys.stderr, 'decrypted: "%s"' % message

finally:
    print >> sys.stderr, 'closing socket'
    s.close()
