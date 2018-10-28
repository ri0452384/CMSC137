#an implementation of the single-dimensional parity check
#by: Rayven Ingles, BSCS 4
#completed as a lab exercise for CMSC 137

def check_input(input_string) :
    ###loop through input string###
    for character in input_string:
        if not (character == "0" or character == "1"):
            print("Input must be a bit string!")
            input_string input("> Input again: ")
            check_input(input_string)

### ask for user input ###
a = input("> Input A: ")
check_input(a)
while len(a) != 8:
    print("Input a must be an 8-bit string!")
    a = input("> Input A: ")
    check_input(a)
b = input("> Input B: ")
check_input(b)
while len(b) != 9:
    print("Input b must be a 9-bit string!")
    b = input("> Input A: ")
    check_input(b)

one_count=0
for character in a:
    if(character == '1'):
        one_count+=1

if((one_count % 2)==1):
    parity = "1"
else:
    parity = "0"

codeword = a+parity

###calculate syndrome###
one_count=0
for character in b:
    if(character == '1'):
        one_count+=1
if((one_count % 2)==1):
    accept_status = "discarded"

print("@Sender\n"+codeword)
if((one_count % 2)==1):
    accept_status = "discarded"
else:
    accept_status = b[0:8]
print("@Receiver\nData Word:"+accept_status)
