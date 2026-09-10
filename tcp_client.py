import socket



SERVER_HOST = "127.0.0.1"  # The computer running tcp_server.py
SERVER_PORT = 5000
BUFFER_SIZE = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"Connected to TCP server at {SERVER_HOST}:{SERVER_PORT}")
    print("Type /quit to end the chat.")

    while True:
        message = input("You: ")
        client_socket.sendall(message.encode("utf-8"))

        if message.lower() == "/quit":
            print("Chat ended.")
            break

        data = client_socket.recv(BUFFER_SIZE)

        if not data:
            print("Server disconnected.")
            break

        reply = data.decode("utf-8")
        print(f"Server: {reply}")

        if reply.lower() == "/quit":
            print("Chat ended by the server.")
            break
