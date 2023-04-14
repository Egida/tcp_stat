import socket
import time
import ssl
import sys
import os

def tcp_connect(host: str, port: int, return_timestamp: bool = False, use_ssl: bool = False):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        start_connect = time.time()
        sock.connect((host, port))
        if use_ssl:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            sock = ctx.wrap_socket(sock)
        end_connect = time.time()
        timestamp = end_connect - start_connect

        if return_timestamp:
            return timestamp
        
        return True
    except TimeoutError:
        return False

def main():
    try:
        os.system("")

        args = sys.argv

        if len(args) < 3:
            print(f"USAGE: {args[0]} [HOST] [PORT] -ssl")
            return
        
        try:
            host = socket.gethostbyname(args[1])
        except Exception:
            print(f"Error: Unable to resolve hostname ({args[1]})")
            return
        
        try:
            port = int(args[2])
            if any([port < 1, port > 65535]):
                raise ValueError
        except ValueError:
            print(f"Error: Port must be integer (1-65535)")
            return

        use_ssl = False
        if "-ssl" in [v.lower() for v in args]:
            use_ssl = True

        print(f"Validating port: {port}...")

        port_validated = False

        for i in range(5):
            print(f"Validating port ({port}) for {i + 1} time(s)...")
            connect_try = tcp_connect(host, port)
            if connect_try:
                print(f"Port ({port}) seems to be valid.")
                port_validated = True
                break
            print(f"Invalid port ({port}). Re-validating...")

        if not port_validated:
            print(f"Port doesn't seem to be open. Ignoring...")

        print(f"Initializing TCP ping on {host}:{port}...\n\nHost Status:")

        while True:
            try:
                timestamp = tcp_connect(host, port, True, use_ssl)
            except Exception as e:
                print(f"\u001b[31;1mX\u001b[0;0m Error: {e}")
                time.sleep(1)
                continue
            
            if timestamp:
                print(f"\u001b[32;1m✔\u001b[0;0m Online: {(timestamp * 1000):.2f} ms")
            else:
                print("\u001b[31;1mX\u001b[0;0m Timeout")

            time.sleep(1)

    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
