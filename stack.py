class Node:
    
    def __init__(self, valor):
        self.value = valor
        self.previous = None
        

class Stack:
    
    def __init__(self, valor = None) -> None:
        
        if valor != None:
        
            new_node = Node(valor)
            self.top = new_node
            self.height = 1
            
        else:
            
            new_node = Node("")
            self.top = new_node
            self.height = 0
            
            
    def __repr__(self) -> str:
        
        string = "[ "
        node = self.top
        
        while node.previous:
            string += f"{str(node.value)} -> "
            node = node.previous
            
        string += f"{str(node.value)} ]"
        
        return string
            
            
    def push(self, valor):
        
        if self.height == 0:
            
            self.__init__(valor)
        
        else:
        
            new_node = Node(valor)
            new_node.previous = self.top
            self.top = new_node
            self.height += 1
            
            
    def pop(self):
        
        if self.height == 0:
            return None
        
        elif self.height == 1:
        
            nodo_pop = self.top
            self.top = Node("")
            self.height = 0
            return nodo_pop.value

        else:
            
            pop_node = self.top
            self.top = pop_node.previous
            self.height -= 1
            return pop_node.value
            
def main():
    pila = 0
    opc = 0
    
    while opc != "":
        print("1. Crear pila || 2. Mostrar pila || 3. Push || 4. Pop")
        opc = input("Ingrese una opción: ")
        
        match opc:
            
            case '1':
                
                if pila == 0:
                    
                    valor = input("Ingrese el valor del primer elemento: ")
                    pila = Stack(valor)
                    
                else:
                    
                    print("Ya existe una pila.")
                    return
                
            case '2':
                
                print(pila)
                print("Top: ", pila.top.value)
                print("Height: ", pila.height)
                
            case '3':
                
                valor = input("Ingrese el valor a introducir: ")
                pila.push(valor)
                print("Valor agregado")
                
            case '4':
                
                print("Elemento eliminado: ", pila.pop())
                
                
main()

