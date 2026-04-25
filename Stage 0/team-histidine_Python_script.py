# TASK:
"""
Write a simple Python script for printing the names, affiliation, and the names of the genes you love most, and the name of the organism bearing the gene. 
The final output should be something like, “Hi, my name is Adewale Ogunleye, a researcher at the University of Tübingen. My favourite gene is lexA in Escherichia coli.”
"""

# SOLUTION
# Assign personal information to variables
name = "David Sunday"
affiliation = "Research Associate at the Federal University of Technology, Akure, Nigeria"
favourite_gene = "AKT1"
organism = "Homo sapiens"

# Import display, Markdown to display output in Markdown format so that scientific terms can appear in italics.
from IPython.display import display, Markdown

# Use the f-string to print out the desired information as specified in the task.
display(Markdown(f'"Hello, my name is {name}. I am a {affiliation}. My favourite gene is *{favourite_gene}*, which is found in *{organism}*."'))
