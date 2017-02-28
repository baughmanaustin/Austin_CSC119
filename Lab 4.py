power = 7
index = 0
total = 0
binary_number_list = []
is_binary = True

print('Welcome to Binary-Decimal Converter')
while(True):
    binary_number = input('Please enter an 8 digit binary number: ')

    binary_number_list = list(binary_number)

    if(len(binary_number_list) > 8 or len(binary_number_list) < 8):

        print('\nPlease input a number that is exactly 8 bits long.\n')

        continue

    else:

        for bit in binary_number_list:

            if(int(bit) != 1 and int(bit) != 0):

                is_binary = False

        if(is_binary == False):

            print('\nInvalid Binary Number, only use 0\'s and 1\'s\n')

            continue



    for num in range(len(binary_number_list)):

        total += (int(binary_number_list[index]) * (2**(power)))

        power -= 1

        index += 1
        
    print("\nYour number", binary_number, "equals", total, "in base ten.\n")
 










