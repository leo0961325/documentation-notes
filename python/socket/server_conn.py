from concurrent import futures as cf
import socket

def handle(new_sock, address):
    while True:
        recv = new_sock.recv(1024)
        if not recv: break
        s = recv.decode('utf-8', errors='replace')
        print('Recv: ', s)
        new_sock.sendall(recv)
    new_sock.close()
    print('Disconnect')

servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsock.bind(('0.0.0.0', 50007))
servsock.listen(5)
print('Serving at ', servsock.getsockname())

with cf.ThreadPoolExecutor(20) as e:
    try:
        while True:
            new_sock, address = servsock.accept()
            e.submit(handle, new_sock, address)
    except KeyboardInterrupt:
        pass
    finally:
        servsock.close()
