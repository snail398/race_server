#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import socket
import time
 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8080))
serversocket.listen(5)
print ('Server is waiting for connections.')
while True:
    conn, addr = serversocket.accept()
    data = conn.recv(1024)
     
    print ('Connection:', addr)
    print ('------------------------------')
    print ("Request Data from Browser")
    print ('------------------------------')
    print (data)
     
    conn.send(data)
    conn.close()
    # Делаем задержку, чтобы цикл не сильно загружал процессор
    time.sleep(0.1)