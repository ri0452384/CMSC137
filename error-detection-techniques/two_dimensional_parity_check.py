def check_input(input_string) :
    ###loop through input string###
    for character in input_string:
        if not (character == "0" or character == "1"):
            print("Input must be a bit string!")
            input_string = input("> Data: ")
            check_input(input_string)

### ask for user input ###
a = input("> Data: ")
a = a.replace(" ", "")
check_input(a)
while len(a) != 45:
    print("Input must be a 45-bit string!")
    a = input("> Data: ")
    check_input(a)
###test print
### print(a[0:8],"parity:",a[9])
### print(a[9:17],"parity:",a[18])
### print(a[18:26],"parity:",a[27])
### print(a[27:35],"parity:",a[36])
### print(a[36:44],"parity:",a[44])
###
###error calculation###
error_count = 0
###row parity calculation###
row_one_count=0
if a[9]=="1":
    row_one_count += 1
if a[18]=="1":
    row_one_count += 1
if a[27]=="1":
    row_one_count += 1
if a[36]=="1":
    row_one_count += 1
if a[44]=="1":
    row_one_count += 1
if row_one_count % 2 == 1:
    error_count += 1
###column parity calculation###
b = a[36:45]
column_one_count = 0
for character in b:
    if(character =="1"):
        column_one_count += 1
if column_one_count % 2 == 1:
    error_count += 1

print("Error count: ", error_count)