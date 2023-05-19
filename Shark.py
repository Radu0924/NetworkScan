import pyshark
import signal

stop_capturing = False

def packet_callback(pkt):
    with open('Pachete.txt', 'a') as f:
        f.write(str(pkt) + '\n')

capture = pyshark.LiveCapture(interface=None)

def stop_capture(signum, frame):
    global stop_capturing
    stop_capturing = True

signal.signal(signal.SIGINT, stop_capture)  # Setează semnalul SIGINT pentru a opri capturarea (Ctrl+C)

try:
    for packet in capture.sniff_continuously():
        packet_callback(packet)
        print(str(packet))  # Afișează informațiile pachetului în timp real

        if stop_capturing:
            break
except KeyboardInterrupt:
    pass

with open('Pachete.txt', 'r') as f:
    while True:
        line = f.readline()
        if line:
            print(line.strip())  # Afișează informațiile din fișier în timp real
        else:
            break
