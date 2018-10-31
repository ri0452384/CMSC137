#an implementation of the 2d parity check
#by: Rayven Ingles, BSCS 4
#completed as a lab exercise for CMSC 137

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
###error calculation starts here###
error_count = 0
#row parity calculations
for j in range (0,5):
    row_parity = 0
    #b=""
    for i in range(0,9):
        #b+=a[9*j+i]
        if a[9*j+i] == "1":
            row_parity += 1
    #print(b)
    if row_parity % 2 == 1:
        error_count += 1

###column parity calculations###
for j in range(0,9):
    column_parity = 0
    #b=""
    for i in range(0,5):
        #b+= a[i*9+j]
        if a[i*9+j] == "1":
            column_parity += 1
    #print(b)
    if column_parity % 2 == 1:
        error_count += 1

print("Error count: ", error_count)
