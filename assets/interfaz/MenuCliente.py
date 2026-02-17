from assets.utilidades import limpiar_pantalla

class MenuCliente:
    def __init__(self, servicio_autenticacion, servicio_producto):
        self.servicio_autenticacion = servicio_autenticacion
        self.producto_service = servicio_producto

    def iniciar(self):
        while True:
            limpiar_pantalla()
            print("\n---SISTEMA DE SUPERMERCADO PYTHON---")
            print("1. Ver productos") 
            print("2. Mis compras")
            print("3. Salir")          
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("\n---Listado de productos---")
                self.mostrar_listado()

            elif opcion == "2":
                print("\n---Historial de compras---")
            elif opcion == "3":
                print("\nCerrando sesión cliente...")
                break
            else:
                print("\nOpción inválida. Intente nuevamente.")

    def mostrar_listado(self):
            print("\n--- LISTADO DE PRODUCTOS ---")
            # llamar metodo obtener_todos() producto_service
            productos = self.producto_service.obtener_todos()

            if not productos: #validar que haya productos
                print("No hay productos cargados en el sistema.")
                return

            # Imprimimos con formato para que se vea ordenado
            print(f"{'ID':<5} | {'Nombre':<20} | {'Precio':<10} | {'Stock':<5}")
            print("-" * 50)
            
            for p in productos:
                # mostrar solo si el producto está activo
                if p.activo == "True":
                    print(f"{p.id:<5} | {p.nombre:<20} | ${p.precio:<9} | {p.stock:<5}")