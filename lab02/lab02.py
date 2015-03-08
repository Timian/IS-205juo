import re
import math
import operator

# Regular expression used to validate and parse Roman numbers
roman_re = re.compile("""^
   ([M]{0,9})   # thousands
   ([DCM]*)     # hundreds
   ([XLC]*)     # tens
   ([IVX]*)     # units
   $""", re.VERBOSE)

# This array contains valid groups of digits and encodes their values.
# The first row is for units, the second for tens and the third for
# hundreds. For example, the sixth element of the tens row yields the
# value 50, as the first is 0.
d2r_table = [
	['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
	['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
	['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
	['M' * i for i in xrange(0,10) ]]


def romantodeci(roman):
	"""Converts a roman number, encoded in a string, to a decimal number."""
	roman = roman.upper()
	match = roman_re.match(roman)

	if not match:
		raise ValueError

	thousands, hundreds, tens, units = match.groups()
	result =  d2r_table[3].index(thousands) * 1000
	result += d2r_table[2].index(hundreds) * 100
	result += d2r_table[1].index(tens) * 10
	result += d2r_table[0].index(units)
	return result


def decitoroman(dec):
	"""Converts a positive decimal integer to a roman number."""
	#if dec == 0:
	#    return ''

	digit = 0
	rem = dec#100
	result = ''
	# Length in digits of the number dec
	dec_len = int(math.ceil(math.log10(dec)) + 1) #3

	# Scan the number digit-by-digit, starting from the MSD (most-significant
	# digit)
	while dec_len > 0:
		# Let's take the current digit
		factor = 10 ** (dec_len - 1) #100
		digit = rem / factor #1

		# And remove it from the number
		rem = rem - digit * factor #0??

		if dec_len == 4:
			# Thousands
			result = result + digit * 'M'

		elif dec_len >= 5:
			# bigger than Thousands
			result = result + digit * '''Learning time: Roman doesn\'t use that\
			 high numbers\n'''

		else:
			# Look in the look-up table
			result = result + d2r_table[dec_len - 1][digit]

		dec_len -= 1

	return result

#print decitoroman(13100)
#print "Skriv lab2.romanmath('*forste tall*', '*operator*', '*andre tall*')"

ops = {"+": operator.add,
	   "-": operator.sub,
	   "*": operator.mul,
	   "/": operator.div}

def romanmath(par1, op, par2):
	#operator takes the parameters par1 and par2 to decimal
	return decitoroman(ops[op](romantodeci(par1), romantodeci(par2)))
