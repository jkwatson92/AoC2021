import datetime
import pytz
##Pull values from file
my_file = open("day3-test.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

write_file=open("day3-log.txt", "a")
write_file.write("-------------------------------------------------- Day 3 Part 2 -------------------------------------------------------------------\n")
result=""


##remove matching index values from working list
def remove_values(value,position,current_list):
    for i in range (0,len(current_list)-1):
        current_value = current_list[i]
        if current_value[position]==value:
            print("remove this: ",value, " match found: ", current_value)
            current_list.remove(current_value)
    return current_list
global one_count
global zero_count
one_count=0
zero_count=0


##Compare column values
def find_values(content_list,mode):
    global one_count
    global zero_count
    
    for j in range(0,5):   
        print("j value: ",j)
        ##Iterate through string values

        for i in range(0,len(content_list)-1):
            ##Iterate through list values
            input_str=content_list[i]
            print("============================= NEW INPUT =====================================================")
            print("current string: ", input_str)
            if len(content_list)==1:
                print("final value: ", input_str) 
                break;
            
            else:
                if input_str[j]== "0":
                    zero_count+=1

                elif input_str[j]=="1":
                    one_count+=1             
            if one_count>zero_count:
                if mode=="oxygen":
                    ##content_list=remove_values(0,j,content_list)
                    find_values(content_list,"oxygen")
                elif mode=="CO2":
                    content_list=remove_values(1,j,content_list)
                    ##find_values(content_list,"CO2") 

            elif zero_count>one_count:
                if mode=="oxygen": 
                    content_list=remove_values(1,j,content_list)
                  ##  find_values(content_list,"oxygen")
                elif mode=="CO2":
                    content_list=remove_values(0,j,content_list)
                  ##  find_values(content_list,"CO2")

            elif zero_count==one_count:
                ##oxygen - keep 1's, CO2 - keep 0's
                if mode=="C02":
                    content_list=remove_values(1,j,content_list)
                   ## find_values(content_list,"CO2")

                elif mode=="oxygen":
                    content_list=remove_values(0,j,content_list)
                 ##   find_values(content_list,"oxygen")
            print("0 count: ", zero_count, "||  1 count: ", one_count)
            print("\n")
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
##Run the functions
find_values(content_list,"oxygen")
find_values(content_list,"CO2")

##epsilon_rate=int(flip_result(result),2)
##gamma_rate=int(result,2)
##power_consumption=gamma_rate*epsilon_rate
##
####log that shit
##current_time=datetime.datetime.now(pytz.timezone('America/New_York'))
##time_line= "current time [EST]: " + str(current_time)
##write_file.write("----------------------------------------------- " + time_line + " -----------------------------------------------\n")
##rate_values="gamma: " + str(gamma_rate) + " epsilon: " + str(epsilon_rate)
##write_file.write(rate_values + '\n')
##power_value ="power consumption: " + str(power_consumption)
##write_file.write(power_value + '\n')
write_file.close()
