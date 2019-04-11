from Bio import SeqIO

for fasta in SeqIO.parse("my_seq.fasta", "fasta"):
	print (fasta.id)
	print (fasta.seq)