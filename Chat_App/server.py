import socket
import threading
server = socket.socket()
server.bind(("localhost", 12345))
server.listen(2)
print("Server started...")
clients = []
def handle_client(conn):
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            for c in clients:
                if c != conn:
                    c.send(msg.encode())
        except:
            break
    conn.close()
    clients.remove(conn)
# accept clients
while True:
    conn, addr = server.accept()
    print("Connected:", addr)
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn,), daemon=True).start()
