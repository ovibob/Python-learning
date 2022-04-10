import sys

bitmap = """
 ....................................................................
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
 ....................................................................."""

print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()


for line in bitmap.splitlines(): # Loop over each line in the bitmap:
    for i, bit in enumerate(line): # Loop over each character in the line:
        if bit == ' ':
            print(' ', end='') # Print an empty space since there's a space in the bitmap
        else:
            print(message[i % len(message)], end='') # Print a character from the message:
    print() # print a new line


