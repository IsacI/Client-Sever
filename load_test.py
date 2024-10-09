import threading
import time
import subprocess

def start_client():
    subprocess.call(['python', 'client.py'])

def main():
    num_clients = int(input("Quantos clientes você deseja simular? "))
    threads = []

    for _ in range(num_clients):
        thread = threading.Thread(target=start_client)
        thread.start()
        threads.append(thread)
        time.sleep(0.1)  # Pequena pausa entre a criação de threads

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
