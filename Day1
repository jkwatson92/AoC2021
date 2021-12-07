
##Pull values from file
my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()



##Convert to int then compare values to previous value

int_list = list(map(int, content_list))
def compare_values(int_list):
    increased=0
    decreased=0
    for x in range(0, len(int_list)-1):
        if int_list[x+1] - int_list[x] > 0:
            increased+=1

        else:
            decreased+=1
    print("increased: ",increased)
    ##answer day1 pt 1 = 1529
sum_list=[]
def build3value(int_list):
    i=0
    for i in range(0, len(int_list)-2):
        if int_list[i]!= None and int_list[i+1] != None and int_list[i+2] != None:
            sum_ints=int_list[i]+int_list[i+1] + int_list[i+2]
            i+=1
            sum_list.append(sum_ints)
            ##print(sum_ints)

        else:
            break
            
##Check range before running
build3value(int_list)
compare_values(sum_list)
##compare_values(int_list)


    
