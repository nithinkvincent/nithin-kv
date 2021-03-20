# sample_size = (input("Hello"))
# print(sample_size)
Expected_items = []
Sorted_items = []
minimaldifference = float('inf')

with open ("Item.txt", "r") as myitem:
    data_red=myitem.readlines()

num_emp=int(data_red[0][-2]) # to select last member of the line

for i in range(4,len(data_red)):
    temp_spit = data_red[i].split(":")
    Expected_items.append([temp_spit[0],int(temp_spit[1])])

Sorted_items = sorted(Expected_items, key= lambda i:i[1]) 

for i in range(0,len(Sorted_items) - num_emp+1):
    difference = Sorted_items[i + num_emp - 1][1] - Sorted_items[i][1]
    if difference<minimaldifference:
        index=i
        minimaldifference = difference
myitem.close()

with open("out.txt","w") as write_data:

    write_data.write("The goodies selected for distribution are: \n \n")

    for i in range(index,index+num_emp):
        temp_data1 = str(Sorted_items[i][0] + " " + str(Sorted_items[i][1]) + "\n")
        write_data.write(temp_data1)

    write_data.write("\n")
    write_data.write("And the difference between the chosen goodie with highest price and the lowest price is ")
    write_data.write(str(minimaldifference))






# file_write = open("out.txt","w")
# file_write.write("The goodies selected for distribution are: \n \n")

# for i in range(index,index+num_emp):
#     temp_data=str(Sorted_items[i])
#     file_write.write(temp_data)
#     file_write.write("\n")

# file_write.write("\n")
# file_write.write("And the difference between the chosen goodie with highest price and the lowest price is ")
# file_write.write(minimaldifference)
