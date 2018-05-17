import socket

HOST = '127.0.0.1'   
PORT = 50007 

# 建立 連線導向 Socket(Server)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)			# 允許排隊數
    conn, addr = s.accept()	# 回傳新的 socket
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)	# client中斷連線的話, data為空值
            if not data: 
                print(data)
                print(type(data))
                break
            conn.sendall(data)
