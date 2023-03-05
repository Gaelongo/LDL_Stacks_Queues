class Node:
    
    def __init__(self, valor):
        self.value = valor
        self.previous = None
        self.next = None
        
        
class DoublyLinkedList:
    
    def __init__(self, valor = None) -> None:
        
        if valor != None:
            
            new_node = Node(valor)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        
        else:
            
            nodo_vacio = Node("")
            self.head = nodo_vacio
            self.tail = nodo_vacio
            self.length = 0
            
        
    def __repr__(self) -> str:
            
        lista = "["
        obj = self.head
            
        while obj.next:
                
            lista += "{} -> ".format(str(obj.value))
            obj = obj.next
                
        lista += "{}]".format(str(obj.value))
            
        return lista
        
        
    def append(self, valor):
            
        if self.length == 0:
            self.__init__(valor)
                
        else:
                
            new_node = Node(valor)
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            self.length += 1
            
            
    def pop(self):
        
        if self.length == 1:
            
            self.head = None
            self.tail = None
            self.length = 0
        
        elif self.length == 0:
            pass
        
        else:
            
            self.tail = self.tail.previous
            self.tail.next = None
            self.length -= 1
            
            
    def popFirst(self):
        
        if self.length == 1:
            
            self.head = None
            self.tail = None
            self.length = 0
            
        elif self.length == 0:
            pass
        
        else:
            
            self.head = self.head.next
            self.length -= 1
            
            
    def remove(self, valor):
        
        obj_remove = self.head
        
        while obj_remove.value != valor:
            
            obj_remove = obj_remove.next
            
        if obj_remove == self.head:
            
            self.popFirst()
            
        elif obj_remove == self.tail:
            
            self.pop()
            
        else:
            
            obj_ant = obj_remove.previous
            obj_ant.next = obj_remove.next
            
            
    def prepend(self, valor):
        
        if self.length == 0:
            
            self.__init__(valor)
            
        else:
            
            new_node = Node(valor)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            
            
    def get(self, index):
        
        if index < 0 or index > self.length-1:
            
            print("Índice inválido...")
            return
        
        else:
            
            current_node = self.head
            
            for i in range(0, index):
                
                current_node = current_node.next
            
            return current_node
        
        
    def insert(self, index, valor):
        
        if index > self.length or index < 0:
            
            print("Indice invalido")
            return
        
        elif index == 0:
            self.prepend(valor)
        
        elif index == self.length:
            self.append(valor)
            
        else:
            
            new_node = Node(valor)
            index_node = self.get(index)
            new_node.next = index_node
            prev_node = index_node.previous
            prev_node.next = new_node
            
            
    def set(self, index, valor):
        
        current_node = self.get(index)
        current_node.value = valor
        
    
    def removeByIndex(self, index):
        
        if index < 0 or index > self.length-1:
            
            print("Indice invalido.")
            return
        
        elif index == 0:
            self.popFirst()
            
        elif index == self.length-1:
            self.pop()
            
        else:
            
            delete_node = self.get(index)
            previous_node = delete_node.previous
            previous_node.next = delete_node.next
            
            
        
            
            
mi_lista = DoublyLinkedList()

print(mi_lista)
#mi_lista.append(4)
#print(mi_lista)

print("Head: ", mi_lista.head.value)
print("Tail: ", mi_lista.tail.value)
print("Length: ", mi_lista.length)