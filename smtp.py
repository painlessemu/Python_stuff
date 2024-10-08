import sys, socket
size = 1024

def sendMessage(smtpServer, port, fromAddress,toAddress,message):
    IP = smtpServer
    PORT = int(port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Open socket on port
    s.connect((IP,PORT))
    #print the response
    print(s.recv(size).decode())
    s.send(b'HELO' + fromAddress.split('@'[1].encode() +b'\n'))
    print(s.recv(size).decode())
    #send Mail from
    s.send(b'MAIL FROM:<' + fromAddress.encode() + b'>\n')
    print(s.recv(size).decode())
    #send receipt to 
    s.send(b'RCPT TO:<' + toAddress.encode() + b'\n')
    print(s.recv(size).decode())
    #send data
    s.send(b"DATA\n")
    print(s.recv(size).decode())
    s.send(message.encode() + b'\n')
    s.send(b'\r\n.\r\n')
    #display reponse
    print(s.recv(size).decode())
    #send quit
    s.send(b'QUIT\n')
    #display response
    print(s.recv(size).decode())
    s.close()

    def main(args):
        smtpServer = args[1]
        port = args[2]
        fromAddress = args[3]
        toAddress = args[4]
        message = args[5]
        sendMessage(smtpServer, port, fromAddress, toAddress, message)

    if __name__ == "__main__":
        main(sys.argv)