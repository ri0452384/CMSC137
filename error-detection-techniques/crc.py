#an implementation of the 7-bit CRC
#by: Rayven Ingles, BSCS 4
#completed as a lab exercise for CMSC 137

### function to check for input
def check_input(input_string) :
    input_string = input_string.replace(" ", "")
    ###loop through input string###
    for character in input_string:
        if not (character == "0" or character == "1"):
            print("Input must be a bit string!")
            input_string = input("> Data: ")
            check_input(input_string)

### function to perform the XOR of two 4-bit numbers, always drops the first 0 bit
def perform_XOR(bit_1,bit_2):
    answer = ""
    ##bitwise XOR operation goes here
    for i in range(0,len(bit_1)):
        if bit_1[i] == bit_2[i]:
            answer += '0'
        else:
            answer += '1'
    return answer[1:4]

### ask for user input ###
a = input("> Data: ")
a = a.replace(" ", "")
check_input(a)
while len(a) != 7:
    print("Input must be a 7-bit string!")
    a = input("> Data: ")
    check_input(a)
### this can change depending on the agreed value

### agreed divisor between coder and decoder
divisor = "1011"
### pop the first 4 bits from input string
dividend = a[0:4]
a = a[4:7]

while len(a) > 0:
    #perform XOR of the first_dividend and the divisor
    #implement a check of the leftmost bit of the augmented data then determine whether to use the divisor, or '0000' in the XOR
    if dividend[0]=="1":
        dividend = perform_XOR(dividend,divisor)
    else:
        dividend = perform_XOR(dividend,"0000")
    answer=dividend

    #add the first bit from the remaining input string to the remainder making it the new dividend
    dividend = dividend+a[0]
    a = a[1:]
### only time the dataword will be accepted is when the syndrome is 000.
if(answer == "000"):
    print("Accept data.")
else:
    print("CRC error detected.")
