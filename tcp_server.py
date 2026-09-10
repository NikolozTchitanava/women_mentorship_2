import socket


HOST = "127.0.0.1"  # Listen only on this computer
PORT = 5000
BUFFER_SIZE = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Allow the server to restart without waiting for the port to be released.
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"TCP server is listening on {HOST}:{PORT}")
    print("Waiting for a client...")

    connection, client_address = server_socket.accept()

    with connection:
        print(f"Client connected from {client_address}")

        while True:
            data = connection.recv(BUFFER_SIZE)

            # Empty data means that the client disconnected.
            if not data:
                print("Client disconnected.")
                break

            message = data.decode("utf-8")
            print(f"Client: {message}")

            if message.lower() == "/quit":
                print("Chat ended by the client.")
                break

            reply = input("You: ")
            connection.sendall(reply.encode("utf-8"))

            if reply.lower() == "/quit":
                print("Chat ended.")
                break
