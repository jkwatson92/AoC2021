##Pull values from file
my_file = open("day2.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

x_pos=0
y_pos=0
##Forward = +x, down = +y, up= -y

for i in range(0,len(content_list)-1):
    
    movement=[int(j) for j in content_list[i].split() if j.isdigit()]
   
    if "forward" in content_list[i]:
        x_pos+=movement[0]

    elif "up" in content_list[i]:
        y_pos-=movement[0]

    elif "down" in content_list[i]:
        y_pos+=movement[0]

print("x: ", x_pos, " y: ", y_pos)
print("multiplied: ", x_pos*y_pos)        
        
        
