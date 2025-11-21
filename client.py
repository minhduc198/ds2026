# client.py
import socket
import argparse
from utils import send_file

def send(host, port, filepath):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print(f"[CLIENT] Connected to {host}:{port}")
    print(f"[CLIENT] Sending: {filepath}")

    send_file(client, filepath)

    print("[CLIENT] File sent successfully.")
    client.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("file", help="Path to file cần gửi")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=9000)

    args = ap.parse_args()

    send(args.host, args.port, args.file)



