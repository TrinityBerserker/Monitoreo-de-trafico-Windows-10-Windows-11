import subprocess
from scapy.all import sniff, IP
from collections import defaultdict
import time

# IP de la PC (puedes poner tu IP local manualmente o detectarla)
MY_IP = "192.168.1.100"  # Cambia por la IP de tu PC

# Umbral: cantidad de paquetes sospechosos por IP en intervalo de tiempo
PACKET_THRESHOLD = 20
TIME_WINDOW = 10  # segundos

# Diccionario para contar paquetes por IP en el intervalo
ip_packet_count = defaultdict(int)
first_timestamp = time.time()

def desconectar_red():
    print("Comportamiento sospechoso detectado. Desconectando red...")
    # Cambia "Wi-Fi" por el nombre exacto de tu adaptador de red
    adapter_name = "Wi-Fi"
    # Comando para deshabilitar adaptador de red en Windows
    subprocess.run(f'netsh interface set interface "{adapter_name}" admin=disable', shell=True)

def analizar_paquete(pkt):
    global first_timestamp
    if IP in pkt:
        ip_dst = pkt[IP].dst
        ip_src = pkt[IP].src
        
        current_time = time.time()
        # Reiniciar conteo si pasó más de TIME_WINDOW segundos
        if current_time - first_timestamp > TIME_WINDOW:
            ip_packet_count.clear()
            first_timestamp = current_time
        
        # Contar paquetes dirigidos a mi IP
        if ip_dst == MY_IP:
            ip_packet_count[ip_src] += 1
            if ip_packet_count[ip_src] > PACKET_THRESHOLD:
                desconectar_red()
                # Parar la captura después de desconectar
                return True

# Ejecutar sniffing
print(f"Monitoreando tráfico dirigido a {MY_IP}...")
sniff(prn=analizar_paquete, stop_filter=lambda x: False)
