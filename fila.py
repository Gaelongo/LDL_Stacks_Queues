class Node:
    
    def __init__(self, valor):
        
        self.value = valor
        self.next = None
        

class Queue:
    
    def __init__(self, valor = ""):
        
        nodo = Node(valor)
        self.start = nodo
        self.end = nodo
        
        if valor == "":
            
            self.length = 0
            
        else:
        
            self.length = 1
            
            
    def __repr__(self) -> str:
        
        lista = "["
        obj = self.start
            
        while obj.next:
                
            lista += f"{obj.value} -> "
            obj = obj.next
                
        lista += f"{obj.value}]"
            
        return lista
    
    
    def append(self, valor):
        
        if self.length == 0:
            
            self.__init__(valor)
            
        else:
            
            nodo = Node(valor)
            self.end.next = nodo
            self.end = nodo
            self.length += 1
            
            
    def pop(self):
        
        if self.length == 1:
            
            return_node = self.start
            nodo_vacio = Node("")
            self.start = nodo_vacio
            self.end = nodo_vacio
            self.length = 0
            return return_node.value
        
        elif self.length == 0:
            
            print("No hay elementos en la lista.")
            return "None"
        
        else:
        
            return_node = self.start
            self.start = return_node.next
            self.length -= 1
            return return_node.value
            
            
def imprimirDatos(fila):
    
    print("Inicio: " + fila.start.value)
    print("Final: " + fila.end.value)
    print("Length: " + str(fila.length))
    
def main():
    
    opc = 0
    fila = 0
    
    while opc != "":
        
        print("1. Crear fila || 2. Mostrar fila || 3. Append || 4. Pop")
        opc = input("Ingrese una opción: ")
        
        match opc:
            
            case '1':
                
                if fila == 0:
                    
                    valor = input("Ingrese el primer valor de la fila: ")
                    fila = Queue(valor)
                    
                else:
                    
                    print("Ya existe una fila.")
                    
            case '2':
                
                print(fila)
                imprimirDatos(fila)
                
            case '3':
                
                valor = input("Ingrese el valor a ingresar: ")
                fila.append(valor)
                print("Valor agregado")
                
            case '4':
                
                print("Valor eliminado: " + fila.pop())
                
                
        
main()
        