import socket
import threading
client = socket.socket()
client.connect(("localhost", 12345))
def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg:
                print("\nFriend:", msg)
        except:
            break
threading.Thread(target=receive, daemon=True).start()
while True:
    message = input()
    # exit condition
    if message.lower() == "exit":
        print("Exiting chat...")
        client.close()
        break
    client.send(message.encode())
