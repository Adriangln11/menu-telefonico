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
        print("Contacto agregado con éxito.")

    def search_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)

        if found_contacts:
            print("Contacto encontrado:")
            for contact in found_contacts:
                print(f"Nombre: {contact.name}, Número: {contact.number}")
        else:
            print("No se encontraron contactos con ese nombre.")

def main():
    phone_book = PhoneBook()

    while True:
        print("\nMenú Telefónico")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            name = input("Ingrese el nombre del contacto: ")
            number = input("Ingrese el número del contacto: ")
            phone_book.add_contact(name, number)
        elif choice == "2":
            name = input("Ingrese el nombre a buscar: ")
            phone_book.search_contact(name)
        elif choice == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
