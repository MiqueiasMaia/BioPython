from Bio.Seq import Seq

myFirstSeq = Seq("CGTA")
#Sequencia complementar
seqComplement = myFirstSeq.complement()
print (seqComplement)

#Sequecia reversa complementar
serComplementReverse = myFirstSeq.reverse_complement()
print (serComplementReverse)