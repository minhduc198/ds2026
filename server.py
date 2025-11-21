# server.py
import socket
import argparse
import os
from utils import receive_file

def start_server(host, port, save_dir):
    os.makedirs(save_dir, exist_ok=True)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print(f"[SERVER] Listening on {host}:{port} ...")

    conn, addr = server.accept()
    print(f"[SERVER] Connected by {addr}")

    saved_file = receive_file(conn, save_dir)
    print(f"[SERVER] Received file saved to: {saved_file}")

    conn.close()
    server.close()
    print("[SERVER] Closed connection.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="0.0.0.0")
    ap.add_argument("--port", type=int, default=9000)
    ap.add_argument("--save-dir", default="received")

    args = ap.parse_args()

    start_server(args.host, args.port, args.save_dir)

