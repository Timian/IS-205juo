# -*- coding: utf-8 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes løsning.
#         
#
#
import sys
import psutil
import platform
import subprocess
# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Jørn Utheim-Olsen', \

}

#
#  Oppgave 1
#    Leke med utskrift 
#    Skriv ut følgende "ascii art" i en funksjon (erstatte pass)
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#
#       \/_
#  \,   /( ,/
#   \\\' ///
#    \_ /_/
#    (./
#     '` 
def ascii_bird():
    print   r"       \/_"
    print   r"  \,   /( ,/"
    print   r"   \\\' ///"
    print   r"    \_ /_/"
    print   r"    (./"
    print   r"     '` "
ascii_bird() 
# over: print av ascci_bird

# 
#  Oppgave 2
#    bitAnd - x&y
#	 Implementer funksjonen som gjør en "bitwise" AND operasjon (erstatt pass)
#    Eksempel: bitAnd(6, 5) = 4
#		Forklaring: 6 binært er 110, mens 5 er 101. Hvis vi sammenligner bitvis
#					1 AND 1 gir 1, 1 AND 0 gir 0 og 0 AND 1 gir 0 => 100 binært
#					er 4 desimalt. Antagelse: posisjonsbasert tallsystem og 
#					den mest signifikante bit-en er lengst til venstre

#forklaring av kode:
# print x&y er oppgaven gjort med python sin bitwiseAnd operatør
def bitAnd(x, y):
    print x&y
    binara = bin(x)[2:]
    binarb = bin(y)[2:]
    binarc = ''
    iterator = 0
    
    for x in binara:
        if int(x) + int(binarb[iterator]) == 2:
            print "X[iterator] & Y[iterator]) ==2"
            binarc += ('1')
            print binarc
        else:
            binarc += '0'
        iterator += 1
    print "Her kommer endelig resultat etter bitwise x&y i binært"
    print binarc
    print "Her er endelig resultat etter bitwise x&y i character"
    print int(binarc, 2)
    return int(binarc, 2)
    
bitAnd(6, 5)


#
#  Oppgave 3
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
def bitXor(x, y):
    print x^y
    binara = bin(x)[2:] 
    binarb = bin(y)[2:]
    binarc = ''
    iterator = 0
    
    for x in binara:
        if int(x) + int(binarb[iterator]) ==2:
            binarc += '0'
        if int(x) + int(binarb[iterator]) == 1 and int(x) == 1:
            binarc += '1'
        if int(x) + int(binarb[iterator]) == 1 and int(x) == 0:
            binarc += '1'
        if int(x) + int(binarb[iterator]) == 0:
            binarc += '0'
        iterator +=1
    print "her er endelig resultat etter bitwise x^y i binært"
    print binarc
    print "Her er endelig resultat etter bitwise xŷ i character"
    print int(binarc, 2)
    return int(binarc, 2)
    
bitXor(4, 5)
        
        
        

	

#
#  Oppgave 4
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
#
def bitOr(x, y):
    print x|y
    binara = bin(x)[2:] 
    binarb = bin(y)[2:]
    binarc = ''
    iterator = 0
    
    for x in binara:
        if int(x) ==1 or int(binarb[iterator])==1:
            binarc += '1'
        else: 
            binarc += '0'
        iterator += 1
    print "her er endelig resultat etter bitwise x|y i binært"
    print binarc
    print "Her er endelig resultat etter bitwise x|ŷ i character"
    print int(binarc, 2)
    return int(binarc, 2)
        

#
#  Oppgave 5
#
#  Tips:
#    For å finne desimalverdien til et tegn kan funksjonen ord brukes, for eksempel
#      ord('A') , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
#
#	 Hvilke begrensninger vil en slik funksjon ha? (tips: prøv med bokstaven 'å', f.eks.)

#	 Forklar resultatet ascii8Bin('å')
#	 Hvilke faktorer påvirker resultatet? Forklar.
#
def ascii8Bin(letter):
    numlet=ord(letter)
    numbin='{0:08b}'.format(numlet)
    #print numbin
    return numbin
    #Unicode tegn som ÆØÅ er 2 bytes istedenfor ved de andre bokstavene er 1 bytes. Ascii=1byte Unicode=2byte0
    #ord kan ikke håndtere 2 bytes derfor vill ikke denne metoden fungere.

# 
#  Oppgave 6
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut: 
#                01001000
#                01101001
#	 Forklart hver linje i denne funksjonen (hva er list, hva gjør in)
#	 Skriv selv inn tester ved å bruke assert i funksjonen test()
#
def transferBin(string): 
    l = list(string)
    binl = []
    for c in l:
        print "Den binære representasjonen for %s" % c
        print ascii8Bin(c)
        binl.append(ascii8Bin(c))
    return binl
    # Kommentar til janis: pep-8 sier at man skal bruke 4 spaces, ikke tabs når det kommer til indentasjon --Kjetil A. Liknes
transferBin("hello")
        
#
#  Oppgave 7
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#    Skriv selv inn tester ved å bruke assert i funksjonen test()
def asciitohex(x):
    ascii = ord(x)
    return '{0:02x}'.format(ascii)
    

def transferHex(string):
    l = list(string)
    hexl = []
    for c in l:
        print "Den heksadesimale representasjonen for %s" % c
        print asciitohex(c)
        hexl.append(asciitohex(c))
    return hexl


#
# Oppgave 8
# 		Implementer en funksjon unicodeBin, som kan behandle norske bokstaver
# 		Kravspesifikasjon for denne funksjonen er den samme som for ascii8Bin funksjonen
def unicodeBin(character):
    utf8_byte_array = bytearray(character)
    uba = [] 
    
    for n in range(len(character)):
        uba.append("{0:08b}".format(utf8_byte_array[n]))

        uni_bin = ' '.join(uba)
    return uni_bin       

#
# Oppgave 9
# 	Studer python module psutils (må være obs på versjon)
#   Prøv å finne ut hvordan du kan finne ut og skrive ut følgende informasjon om din 
#   datamaskin-node:
#
# 			Brand and model
# 			Hard drive capacity
# 			Amount of RAM
# 			Model and speed of CPU
# 			Display resolution and size
# 			Operating system
#	
#	Forklar hvorfor man kan / ikke kan finne denne informasjon vha. psutil modulen.
#	Skriv en funksjon printSysInfo som skriver ut den informasjon som psutil kan finne.
#	Kan dere skrive en test for denne funksjonen?
#	Hvilke andre muligheter har man for å finne informasjon om maskinvare i GNU/Linux?
#

def printSysInfo():
    #harddrive capacity
    diskUse = psutil.disk_usage('/')
    print "Disk Capacity", diskUse.total/1000000000, "GB"
    #amount of RAM
    memram = psutil.virtual_memory()
    print "Memory total", memram.total/100000, "mb"
    #Model and speed of CPU
    with open('/proc/cpuinfo') as f:
        cores = 0
        for line in f:
            if "model name" in line:
                mname = line.replace(' ', '') #replace tab wiht nothing
                cores += 100
        print mname.strip('\n')
        print "number of cores: " + str(cores)
    #display resolution and size
    scrnsize = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]   
    print "Your screen resolution", scrnsize.strip('\n')
    #operating system (using psuntil)
    osp =platform.platform()
    print "Your platform:", osp
    
printSysInfo()
	


def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'
	assert transferBin('hello') == ['01101000', '01100101', '01101100', '01101100', '01101111']
	assert transferHex('hello') == ['68', '65', '6c', '6c', '6f']
	# Skriv her inn passende tester for tarnsferBin og transferHex funksjoner
	# fra oppgavene 6 og 7
	assert unicodeBin('å') == '11000011 10100101'
	# Dine egne tester
	return "Testene er fullført uten feil."
print test()


# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
#print test()
		

