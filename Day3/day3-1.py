import datetime
import pytz
##Pull values from file
my_file = open("day3.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

write_file=open("day3-log.txt", "a")
result=""
one_count=0
zero_count=0
##Compare column values
for j in range(0,12):   

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
epsilon_rate=int(flip_result(result),2)
gamma_rate=int(result,2)
power_consumption=gamma_rate*epsilon_rate

##log that shit
current_time=datetime.datetime.now(pytz.timezone('America/New_York'))
time_line= "current time [EST]: " + str(current_time)
write_file.write("----------------------------------------------- " + time_line + " -----------------------------------------------\n")
rate_values="gamma: " + str(gamma_rate) + " epsilon: " + str(epsilon_rate)
write_file.write(rate_values + '\n')
power_value ="power consumption: " + str(power_consumption)
write_file.write(power_value + '\n')
write_file.close()
