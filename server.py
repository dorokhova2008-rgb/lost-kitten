import socket
import threading

clients = []
client_lock = threading.Lock()

def remove_client(client_socket):
    with client_lock:
        if client_socket in clients:
            clients.remove(client_socket)
    try:
        client_socket.close()
    except:
        pass

def broadcast(message, sender_socket=None):
    with client_lock:
        current_clients = clients.copy()
    for client in current_clients:
        if client != sender_socket:
            try:
                client.sendall(message.encode("utf-8"))
            except:
                remove_client(client)

def handle_client(client_socket, client_addrs):
    print(f"client {client_addrs} is connected")
    try:
        client_socket.sendall("Добро пожаловать в чат!\n".encode("utf-8"))
        broadcast(
            f"Участник {client_addrs} присоединился к чату\n",
            client_socket
        )
        while True:
            try:
                data = client_socket.recv(1024)
            except ConnectionResetError:
                break
            if not data:
                break
            message = data.decode("utf-8").strip()
            if message == "":
                continue
            print(f"from client {client_addrs}: {message}")
            broadcast(
                f"{client_addrs}: {message}\n",
                client_socket
            )
    finally:
        remove_client(client_socket)
        broadcast(
            f"Участник {client_addrs} покинул чат\n",
            client_socket
        )
        print(f"client {client_addrs} off")

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind(("127.0.0.1", 5000))
socket_server.listen()
print("сервер ждет клиента на подключение")
try:
    while True:
        client_socket, client_addrs = socket_server.accept()
        with client_lock:
            clients.append(client_socket)
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_addrs),
            daemon=True
        )
        thread.start()
except KeyboardInterrupt:
    print("\nсервер выключен")
finally:
    with client_lock:
        current_clients = clients.copy()
        clients.clear()
    for client in current_clients:
        try:
            client.close()
        except:
            pass
    socket_server.close()