#an implementation of the checksum algorithm
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

### function to calculate the bit sum and carry then return the 1s complement sum(carried one included)
def bit_add(first_bit, second_bit):
    answer = int(first_bit+second_bit)
    carry = 0
    if(answer > 255):
        carry = 1
        answer -= 256
    return int(answer + carry)

### ask for user input ###
a = input("> Data: ")
a = a.replace(" ", "")
check_input(a)
while len(a) != 40:
    print("Input must be a 40-bit string!")
    a = input("> Data: ")
    check_input(a)

bit_1 = int(a[0:8],2)
bit_2 = int(a[8:16],2)
bit_3 = int(a[16:24],2)
bit_4 = int(a[24:32],2)
checksum_bit = int(a[32:40],2)

### addition between first 2 bytes
first_sum = bit_add(bit_1,bit_2)
### add the third one to the existing sum
sum_1 = int(first_sum)
second_sum = bit_add(sum_1,bit_3)
### add the last byte
sum_2 = int(second_sum)
third_sum = bit_add(sum_2,bit_4)
### add the checksum byte
sum_3 = int(third_sum)
final_sum = bit_add(sum_3,checksum_bit)
answer=bin(final_sum)
### only time this will be accepted is when the sum is the 1s complement of 0.
if(answer == "0b11111111"):
    print("Accept data.")
else:
    print("Discard data.")
