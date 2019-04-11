# -*- coding: UTF-8 -*-
import re

seq1 = "AT.G"
seq2 = "ATCGAAAA"

busca = re.match(seq1, seq2)

if busca:
	print ("Identicas")
else:
	print ("Diferentes")