from Bio.PDB import *
#SMCRA
parser = PDBParser()
estructure = parser.get_structure("1BGA","1bga.pdb")
model = estructure[0]
chair_A = model['A']
residum_100 = chair_A[100]
carbono_alfa_atom = residum_100['CA']
atom_101 = estructure[0]['A'][101]['CA']
euclidian_h = carbono_alfa_atom - atom_101
print("distancia euclinidina %s" %euclidian_h)