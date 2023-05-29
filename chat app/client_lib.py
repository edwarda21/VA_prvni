import socket
def socket_connect(in_socket, in_host = socket.gethostname(), in_port = 2205):
    in_socket.connect(in_host, in_port)

