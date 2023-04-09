# method that allows you to sort the vector of integers// método que permite ordenar o vetor de inteiros
# using insertion sort sort //usando a ordenação Insertion Sort
def insertionSort(v):
  # scrolls through all the elements of the vector starting // percorre todos os elementos do vetor começando
  # by the second element //pelo segundo elemento
  for i in range(len(v)):
    a= v[i] # the current value to be entered // o valor atual a ser inserido
    # begins to compare with the cell to the left of i // começa a comparar com a célula à esquerda de i
    j = i - 1
       
    # while vector[j] is out of order in relation to  the current //enquanto vetor[j] estiver fora de ordem em relação a atual
    
    while((j >= 0) and (v[j] > a)):
      # we move vector[j] to the right and decrement j// movemos vetor[j] para a direita e decrementamos j
      v[j + 1] = v[j]
      j = j - 1
       
      # we put current in its proper place // colocamos atual em seu devido lugar
      v[j + 1] = a
 
# main function of the program //função principal do programa
def main():
  # creates a list of integers // cria uma lista de inteiros
  val = [36, 78, 66, 87, 22, 99, 789, 96, 111, 254, 78, 965, 785, 745]
   
  # we display the vector in the original orderwe display the vector in the original order // exibimos o vetor na ordem original
  print("Original order:\n")
  for i in range(len(val)):
    print(val[i], end = "  ")
     
  # let's sort the vector now // vamos ordenar o vetor agora
  insertionSort(val)
     
  # we display the ordered vector // exibimos o vetor ordenado
  print("\n\nOrdenado:\n")
  for i in range(len(val)):
    print(val[i], end = "  ")
 
if __name__== "__main__":
  main()
