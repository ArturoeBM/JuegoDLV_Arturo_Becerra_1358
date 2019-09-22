#Array2D
#Arrat2D(rows,cds)
"""
get_num_rows() #regresa numero de filas
get_num_cols()
clearing()
set_item(r,c,valor)
get_item(r,c)


(columna |,fila - (rows))
"""

class Array2D:
    def __init__(self,rows,cols): #estructura para constructor de la clase
        self.__data=[]
        self.__rows=rows
        self.__cols=cols
        for x in range(rows):
            tmp=[]
            for y in range(cols):
                tmp.append(None)
            self.__data.append(tmp)
    
    def to_string(self):
        print(self.__data)
    
    def Get_num_rows(self):
        return self.__rows
    
    def Get_num_cols(self):
        return self.__cols
    
    def Clearing(self,value):
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__data[i][j]=value
    def set_item(self,x,y,value):
        if x<self.__rows and x>=0 and y<self.__cols and y>=0:
            self.__data[x][y]=value
        else:
            print("te mamaste we")
    def get_item(self,x,y):
        return self.__data[x][y]
            
        
"""
def main():
    Arreglo=Array2D(5,5)
    Arreglo.to_string()
    print(f"Numero de renglones: {Arreglo.Get_num_rows()}")
    print(f"Numero de renglones: {Arreglo.Get_num_cols()}")
    Arreglo.Clearing(0)
    Arreglo.to_string()
    Arreglo.set_item(4,0,"ahhh perro")
    Arreglo.to_string()
    Arreglo.set_item(-1,5,1)
    Arreglo.set_item(1,6,1)
    print(f"el valor es: {Arreglo.get_item(4,0)}")
main()

"""
