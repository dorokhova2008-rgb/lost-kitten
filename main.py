import socket
import threading

stop_event = threading.Event()

def receive_client(client_socket):
    while not stop_event.is_set():
        try:
            data = client_socket.recv(1024)
            if not data:
                print("\nСервер отключился")
                stop_event.set()
                break
            print(f"\nServer message: {data.decode('utf-8')}")
            print("Write a message: ", end="", flush=True)
        except:
            stop_event.set()
            break

def send_client(client_socket):
    while not stop_event.is_set():
        try:
            message = input("Write a message: ")
            if message.lower() == "exit":
                stop_event.set()
                break
            client_socket.send(message.encode("utf-8"))
        except:
            stop_event.set()
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5000))

receive_thread = threading.Thread(
    target=receive_client,
    args=(client_socket,),
    daemon=True
)
send_thread = threading.Thread(
    target=send_client,
    args=(client_socket,),
    daemon=True
)
receive_thread.start()
send_thread.start()
while not stop_event.is_set():
    stop_event.wait(0.2)
client_socket.close()
print("Клиент завершил работу")