import socket


HOST = "127.0.0.1"  # Listen only on this computer
PORT = 5001
BUFFER_SIZE = 1024


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))

    print(f"UDP server is listening on {HOST}:{PORT}")
    print("Waiting for messages...")

    while True:
        data, client_address = server_socket.recvfrom(BUFFER_SIZE)
        message = data.decode("utf-8")
        print(f"Client {client_address}: {message}")

        if message.lower() == "/quit":
            print("Chat ended by the client.")
            break

        reply = input("You: ")
        server_socket.sendto(reply.encode("utf-8"), client_address)

        if reply.lower() == "/quit":
            print("Chat ended.")
            break
