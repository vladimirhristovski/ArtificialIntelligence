matrix = []
input_text = input().split()
n = int(input_text[0])
m = int(input_text[1])
k = 2
for i in range(n * m):
    matrix.append(int(input_text[k]))
    k += 1
k = 0
new_matrix = []
for a in range(n):
    if a != 0:
        new_matrix.append(new_list)
    new_list = []
    for b in range(m):
        new_list.append(matrix[k])
        k += 1
new_matrix.append(new_list)


def update_matrix(element, x, t):
    if t / 2 > x:
        return element * 2
    else:
        return element * 3


updated_matrix = [[update_matrix(new_matrix[x][y], x, n) for y in range(m)] for x in range(n)]
print(updated_matrix)
