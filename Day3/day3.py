##Pull values from file
my_file = open("day3-test.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

write_file=open("day3.log", "w")

result=""
one_count=0
zero_count=0

##def edit_list(current_list, value, pos):
##    ##removes the elements from the list that are in the given position with the given value
##    for i in range(0, len(current_list)-1):
##        current=current_list[i]
##        if current[pos]==value:
##            current_list.remove(current)
##    return current_list

##Compare column values
def find_values():
    result=""
    one_count=0
    zero_count=0
    for j in range(0,5):   
        
        for i in range(0,len(content_list)-1):
            input_str=content_list[i]

            if input_str[j]== "0":
                zero_count+=1

            elif input_str[j]=="1":
                one_count+=1       
                     
        if one_count>zero_count:
            result+="1"

        elif zero_count>one_count:
            result+="0"
        one_count=0
        zero_count=0
##Find epsilon rate by flipping bits
def flip_result(result):
    flipped=""
    for i in range(0, len(result)):
        if result[i]=="0":
            flipped+="1"
        else:
            flipped+="0"
    return flipped
find_values()
epsilon_rate=flip_result(result)
print(type(epsilon_rate), " value: ", epsilon_rate)
##gamma_rate=int(result,2)
##power_consumption=gamma_rate*epsilon_rate
##write_file.write("gamma: ", gamma_rate, " epsilon: ", epsilon_rate)
##write_file.write("power consumption: ", power_consumption)

##ones_list=content_list.copy()
##zeroes_list=content_list.copy()
##for i in range(0, len(content_list)-1):
##    input_str=content_list[i]
##    if input_str[0]=="1":
##        zeroes_list.remove(content_list[i])
##
##    elif input_str[0]=="0":
##        ones_list.remove(content_list[i])

write_file.write(ones_list)
write_file.write("---------------")
write_file.write(zeroes_list)
write_file.close()


