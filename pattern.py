def draw_door_mat(rows,columns):
    for i in range(1,rows,2):
        pattern = ".|."*i
        print(pattern.center(columns,'-'))
    welcom_line = "WELCOME".center(columns,'-')
    print(welcom_line)
    for i in range(rows-2,0,-2):
        pattern = ".|."*i
        print(pattern.center(columns,'-'))
rows = int(input())
columns = rows*3
draw_door_mat(rows,columns)
