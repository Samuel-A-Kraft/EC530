import socket
import threading

def receive_connection(sock, addr):
    try:
        data = sock.recv(1024).decode()
        print(f"[Incoming] from {addr}: {data}")
    except Exception as e:
        print(f"[Socket error] {e}")
    finally:
        sock.close()

def launch_listener(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen()
    print(f"[Ready] Listening on port {port}")
    while True:
        client_sock, addr = server.accept()
        threading.Thread(target=receive_connection, args=(client_sock, addr)).start()

def deliver_message(target_ip, target_port, content):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))
        sock.send(content.encode())
        sock.close()
        print(f"[Sent] to {target_ip}:{target_port}")
    except Exception as e:
        print(f"[Delivery failed] {e}")
