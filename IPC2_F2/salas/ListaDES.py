import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class Salas:
    def __init__(self, cine, numero, asientos):
        self.cine = cine
        self.numero = numero
        self.asientos = asientos
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

def Salon(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    salitas = DoublyLinkedList()

    for cine in root.findall('cine'):
        nombre = cine.find('nombre').text

        salas_cat = cine.find('salas')
        for salina in salas_cat.findall('sala'):
            numero = salina.find('numero').text
            asientos = salina.find('asientos').text
            sala_data = Salas(nombre, numero, asientos)
            salitas.insert(sala_data)

    return salitas