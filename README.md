# Open-Reading-Frame-Formatter

This is basically a formatter that will take cDNA stored in an input file and do some processing on it to return a formatted text file.

This project uses the Open Reading Frame Finder from https://www.ncbi.nlm.nih.gov/orffinder/, and the python library Biopython. 
Due to restrictions from the Open Reading Frame Formatter, this will only work on Linux (I actually cheated a bit by using WSL2)

This project was designed to help my sister during her internship and remove some stupid copying and pasting that would be otherwise required.

Run main.py, with input data placed in input.txt, and with ORFfinder in the same directory as main.py. Input data can have multiple cDNA strands as long as it's formatted with FASTA 