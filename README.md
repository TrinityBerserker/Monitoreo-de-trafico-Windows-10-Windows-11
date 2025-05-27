# Monitoreo-de-trafico-Windows-10-Windows-11

Primero, instala scapy:

pip install scapy

# 🚨 Monitor de tráfico y desconexión automática de red en Windows

Este script en Python monitorea el tráfico de red dirigido a la IP local de la computadora y, al detectar un comportamiento inusual (por ejemplo, un volumen excesivo de paquetes desde una misma IP), desconecta automáticamente el adaptador de red para proteger la seguridad del equipo.

## ⚙️ Características

- 🕵️‍♂️ Monitoreo en tiempo real del tráfico IP entrante usando **Scapy**.  
- 🚫 Detección de posibles ataques o tráfico sospechoso basado en un umbral configurable.  
- 🔌 Desconexión automática del adaptador de red en Windows 10 y 11 mediante comandos `netsh`.  

## 📋 Requisitos

- 🐍 Python 3.x  
- 📦 Paquete `scapy` (instalable con `pip install scapy`)  
- 🛠️ Ejecutar el script con permisos de administrador (requerido para deshabilitar el adaptador de red)  

## ⚙️ Configuración

1. ✍️ Edita la variable `MY_IP` en el script para colocar la IP local de tu computadora (puedes obtenerla con `ipconfig` en CMD).  
2. 🔍 Cambia el nombre del adaptador de red en la función `desconectar_red()`. El nombre debe coincidir con el mostrado en `netsh interface show interface` (por ejemplo, `"Wi-Fi"`).  
3. 🎛️ Ajusta el umbral (`PACKET_THRESHOLD`) y el intervalo de tiempo (`TIME_WINDOW`) para definir qué se considera tráfico sospechoso.

## 🚀 Uso

1. 🔑 Abre una consola de comandos con privilegios de administrador.  
2. ▶️ Ejecuta el script con `python nombre_del_script.py`.  
3. 📡 El script comenzará a monitorear el tráfico y desconectará la red si detecta actividad sospechosa.


