from socket_cde import socket_client


def read_file(file):
    chunk_size = 50
    chunk_data = []
    with open(file) as f:
        for line in f:
            chunk_data.append(line)
            if len(chunk_data) == chunk_size:
                socket_client(chunk_data)
                chunk_data = []

        if chunk_data:
            socket_client(chunk_data)
