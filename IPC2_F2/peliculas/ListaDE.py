import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class Movie:
    def __init__(self, categoria, titulo, director, anio, fecha, hora, imagen, precio):
        self.categoria = categoria
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.fecha = fecha
        self.hora = hora
        self.imagen = imagen
        self.precio = precio
        self.next = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev

            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.head
            self.head.prev = new_node
    
    def __iter__(self):
        return self.loop()
    
    def loop(self):
        if self.head is not None:
            actual = self.head
            while True:
                yield actual.data
                actual = actual.next
                if actual == self.head:
                    break
        
def Es_cine(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    peli = DoublyCircularLinkedList()

    for categoria in root.findall('categoria'):
        nombre = categoria.find('nombre').text

        peliculas = categoria.find('peliculas')
        for pelicula in peliculas.findall('pelicula'):
            titulo = pelicula.find('titulo').text
            director = pelicula.find('director').text
            anio = pelicula.find('anio').text
            fecha = pelicula.find('fecha').text
            hora = pelicula.find('hora').text
            imagen = pelicula.find('imagen').text
            precio = pelicula.find('precio').text
            pelicula_data = Movie(nombre, titulo, director, anio, fecha, hora, imagen, precio )
            peli.insert(pelicula_data)

    return peli

def register_new_movie(file_path, nombre, titulo, director, anio, fecha, hora):
    tree = ET.parse(file_path)
    root = tree.getroot()

    categories = root.findall('categoria')
    target_category = None

    for category in categories:
        if category.find('nombre').text == nombre:
            target_category = category
            break

    if target_category is None:
        target_category = ET.SubElement(root, 'categoria')
        nombre_element = ET.SubElement(target_category, 'nombre')
        nombre_element.text = nombre
        peliculas_element = ET.SubElement(target_category, 'peliculas')
    else:
        peliculas_element = target_category.find('peliculas')

    pelicula_element = ET.SubElement(peliculas_element, 'pelicula')
    titulo_element = ET.SubElement(pelicula_element, 'titulo')
    director_element = ET.SubElement(pelicula_element, 'director')
    anio_element = ET.SubElement(pelicula_element, 'anio')
    fecha_element = ET.SubElement(pelicula_element, 'fecha')
    hora_element = ET.SubElement(pelicula_element, 'hora')

    titulo_element.text = titulo
    director_element.text = director
    anio_element.text = anio
    fecha_element.text = fecha
    hora_element.text = hora

    xml_string = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")

    with open('Pelis.xml', 'w') as file:
        file.write(xml_string)
