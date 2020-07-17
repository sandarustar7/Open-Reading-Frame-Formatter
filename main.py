#Note: This is a work in progress. I put it together in about half a day, and its not really meant to be a good view of my coding, it was just meant to get the job done.

from Bio import SeqIO
import math
import os
import subprocess

DELETE_TEMPORARY_FILES = True
APPEND_INPUT_FILE = False

with open('ORFfinderstdout.txt', 'w+') as output:
    processResult = subprocess.run(['./ORFfinder', '-in', 'input.txt', '-s', '0', '-outfmt', '0'], stdout=output)

sequences = list(SeqIO.parse('ORFfinderstdout.txt', 'fasta'))


for sequence in sequences:
    id = sequence.id.split(':')
    id[0] = id[0].replace('lcl|','')
    id[1] = str(int(id[1]) + 1)
    id[2] = str(int(id[2]) + 1)
    endid = ':'.join(id)
    sequence.id = ""
 
    isPos = True
    nt = 0
    signed = int(id[2]) - int(id[1])
    if (signed < 0):
        isPos = False
        nt = math.fabs(signed - 1)
    else:
        isPos = True
        nt = math.fabs(signed + 1)
    

    if (isPos):
        sequence.description = id[0] + " + " + " FR " + id[1] + " " +  id[2] + " " + str(int(nt)) + '|' + str(int((nt/3) - 1))
    else:
        sequence.description = id[0] + " - " + " FR " + id[1] + " " +  id[2] + " " + str(int(nt)) + '|' + str(int((nt/3) - 1))

    #sequence.description = "unnamed protein product"
 

SeqIO.write(sequences, "outputformatted.txt", "fasta")

filenames = ['outputformatted.txt']

if APPEND_INPUT_FILE:
    filenames.append('input.txt')

#fileincrement = 0
#while os.path.exists(os.getcwd() + "//" + 'finaloutput' + str(fileincrement) + '.txt'):
#    fileincrement = fileincrement + 1

with open('output' + '.txt', 'w+') as output_file:
    for name in filenames:
        with open(name) as infile:
            for line in infile:
                output_file.write(line)
            output_file.write("\n")

if (DELETE_TEMPORARY_FILES):
    os.remove('./ORFfinderstdout.txt')
    os.remove('./outputformatted.txt')