# utils.py
import os
import struct

BUFFER_SIZE = 4096

def send_file(sock, filepath: str):
    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    # Gửi metadata: tên file + kích thước file
    sock.sendall(struct.pack("!I", len(filename)))
    sock.sendall(filename.encode())

    sock.sendall(struct.pack("!Q", filesize))

    # Gửi nội dung file
    with open(filepath, "rb") as f:
        while chunk := f.read(BUFFER_SIZE):
            sock.sendall(chunk)


def receive_file(sock, save_dir="."):
    # Nhận metadata
    filename_length = struct.unpack("!I", sock.recv(4))[0]
    filename = sock.recv(filename_length).decode()

    filesize = struct.unpack("!Q", sock.recv(8))[0]

    save_path = os.path.join(save_dir, filename)

    with open(save_path, "wb") as f:
        remaining = filesize
        while remaining > 0:
            chunk = sock.recv(min(BUFFER_SIZE, remaining))
            if not chunk:
                break
            f.write(chunk)
            remaining -= len(chunk)

    return save_path
