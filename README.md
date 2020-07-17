# Open-Reading-Frame-Formatter

This is basically a formatter that will take cDNA stored in an input file and do some processing on it to return a formatted text file.

This project uses the Open Reading Frame Finder from https://www.ncbi.nlm.nih.gov/orffinder/, and the python library Biopython. 
Due to restrictions from the Open Reading Frame Formatter, this will only work on Linux (I actually cheated a bit by using WSL2)

This project was designed to help my sister during her internship and remove some stupid copying and pasting that would be otherwise required.

The command to run ORFfinder is "./ORFfinder -in input.txt -s 0 -outfmt 0 &> output.txt". For some reason, ORFfinder's output option did not work for me, so I used this.
