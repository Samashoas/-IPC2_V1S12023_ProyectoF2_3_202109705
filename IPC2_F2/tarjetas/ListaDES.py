import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class Tarjetas:
    def __init__(self, tipo, numero, titular, fecha):
        self.tipo = tipo
        self.numero = numero
        self.titular = titular
        self.fecha = fecha
        self.next = None
        self.prev = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def __iter__(self):
        return self.loop()
    
    def loop(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

def Trade_card(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    tarjetitas = DoublyLinkedList()

    for tarjetina in root.findall('tarjeta'):
        tipo = tarjetina.find('tipo').text
        numero = tarjetina.find('numero').text
        titular = tarjetina.find('titular').text
        fecha = tarjetina.find('fecha_expiracion').text
        tarjeta_data = Tarjetas(tipo, numero, titular, fecha)
        tarjetitas.insert(tarjeta_data)

    return tarjetitas