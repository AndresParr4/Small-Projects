lista = [1,2,3,4,5,6,7,8,9]

def encontrar_carta(carta_index):

    position = 0

    while True:

        if lista[position] == carta_index:
            return position
        
        position += 1

        if len(lista) == position:

            return("La carta no se encuentra")
        

print(encontrar_carta(int(input("Carta: "))))

def binary_search(carta_index):
    lista.sort()
    lo, hi = 0, len(lista) - 1
    while lo <= hi:
        mid = (lo +hi) // 2
        mid_number = lista[mid]
        if mid_number == carta_index:
            return mid
        elif mid_number > carta_index:
            hi = mid - 1
        elif mid_number < carta_index:
            lo = mid + 1
    return -1

print(binary_search(int(input("Carta: "))))


def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)

"""
The Method - Revisited
Here's a systematic strategy we've applied for solving the problem:

1-State the problem clearly. Identify the input & output formats.
2-Come up with some example inputs & outputs. Try to cover all edge cases.
3-Come up with a correct solution for the problem. State it in plain English.
4-Implement the solution and test it using example inputs. Fix bugs, if any.
5-Analyze the algorithm's complexity and identify inefficiencies, if any.
6-Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

"""

    







        
        