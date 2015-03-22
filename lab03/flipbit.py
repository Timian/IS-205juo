# -*- coding: utf-8 -*-

#letter = raw_input()
 
def flipbit(var):
    ba = ' '.join(format(x, 'b') for x in bytearray(var)) #translate the text over to bit
    bb = '0'+ba #puts in an extra zero
    splitba = bb.split(' ') #splits it and then it goes throug the IF statement that starts on line 9, there it will be printed out in 16bit characters
    flippedarray = []
  #  print ba
    if len(splitba) == 2: #
    #    print "16bit" #prints the text 16 bit
    #    print len(splitba)
        prefix = splitba[0]
        suffix = splitba[1]
        placeholder = '0'
        if suffix[2] == '0':
            placeholder = suffix[:2] + '1' + suffix[3:]
        else:
            placeholder = suffix[:2] + '0' + suffix[3:]
        flippedarray.append(prefix)
        flippedarray.append(placeholder)
        return flippedarray
    else: #this part is where it goes trough to be translated into 8bits.
    #    print "8bit" #prints the text 8bits
        placeholder = '0'
        if bb[2] == '0':
            print bb
            placeholder = bb[:2] + '1' + bb[3:]
        else:
            placeholder = bb[:2] + '0' + bb[3:]
        return placeholder
if __name__ == '__main__': #prints everything out to the users screen
    flipped = flipbit(letter)
    strflipped = ' '.join(flipped)
    print flipped
    if len(flipped) == 2:
        a = flipped[0]
        b = flipped[1]
        unia = chr(int(a.decode("utf-8"),2))
        unib = chr(int(b.decode("utf-8"),2))
        unified = unia + unib
        print unified
    else:
        print chr(int(str(flipped),2)) #
