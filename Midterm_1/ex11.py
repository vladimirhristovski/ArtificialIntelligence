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

updated_matrix = [[new_matrix[x][y] * 2 for y in range(m)] for x in range(n)]
print(updated_matrix)
