lista = [7, 2, 1, 6, 8, 5, 3, 4]

def swap(um, dois):
    global lista
    temp = lista[um]
    lista[um] = lista[dois]
    lista[dois] = temp

def quicksort(inicio, fim):
    global lista
    if(inicio >= fim): return
    partition_idx = partition(inicio,fim)
    quicksort(inicio, partition_idx-1)
    quicksort(partition_idx+1,fim)

def partition(inicio, fim):
    global lista
    pivot = lista[fim]
    partition_idx = inicio
    for i in range(inicio,fim):
        if(lista[i] <= pivot):
            swap(i, partition_idx)
            partition_idx +=1
    swap(partition_idx,fim)
    return partition_idx

print(lista)
quicksort(0, len(lista)-1)
print(lista)
