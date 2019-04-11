from Bio.Seq import Seq

mySeq = Seq("ATG")

seq_rna = mySeq.transcribe()
print(seq_rna)

seq_dna = seq_rna.back_transcribe()
print (seq_dna)