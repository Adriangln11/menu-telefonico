import http.server
import urllib.parse

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        contact = Contact(name, number)
        self.contacts.append(contact)
        return "Contacto agregado con éxito."

    def search_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)

        if found_contacts:
            result = "Contacto encontrado:<br>"
            for contact in found_contacts:
                result += f"Nombre: {contact.name}, Número: {contact.number}<br>"
        else:
            result = "No se encontraron contactos con ese nombre."

        return result

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    phone_book = PhoneBook()

    def do_GET(self):
        if self.path == '/':
            content = """
            <html>
            <head>
                <meta charset="UTF-8">
                <link rel="stylesheet" href="https://bootswatch.com/5/darkly/bootstrap.min.css">
                <title>Miniproyectos | Menú Telefónico</title>
            </head>
            <body class="text-center">
                <h1 class="my-5">Menú Telefónico</h1>
                <main class="d-flex gap-5 justify-content-center">
                    <form method="POST" action="/add_contact" class="d-flex flex-column">
                        <h3>Agregar contacto</h3>
                        <label for="name">Nombre:</label>
                        <input type="text" id="name" name="name" required><br>
                        <label for="number">Número:</label>
                        <input type="text" id="number" name="number" required><br>
                        <input type="submit" value="Agregar contacto">
                    </form>
                    <form method="POST" action="/search_contact" class="d-flex flex-column">
                        <h3>Buscar contacto</h3>
                        <label for="search_name">Nombre:</label>
                        <input type="text" id="search_name" name="search_name" required><br>
                        <input type="submit" value="Buscar contacto">
                    </form>
                </main>
            </body>
            </html>
            """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        else:
            self.send_error(404, 'Archivo no encontrado')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)

        if self.path == '/add_contact':
            name = params['name'][0]
            number = params['number'][0]
            result = self.phone_book.add_contact(name, number)
        elif self.path == '/search_contact':
            name = params['search_name'][0]
            result = self.phone_book.search_contact(name)
        else:
            self.send_error(404, 'Archivo no encontrado')
            return

        content = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="https://bootswatch.com/5/darkly/bootstrap.min.css">
            <title>Resultado</title>
        </head>
        <body>
            <h1>Resultado</h1>
            <p>{result}</p>
            <a href="/">Volver al menú principal</a>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

def main():
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, MyRequestHandler)
    print('Server listening on port : 8000')
    httpd.serve_forever()

if __name__ == '__main__':
    main()
