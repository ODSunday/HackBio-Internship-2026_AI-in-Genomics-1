## Part 1: Simple Python Script for Printing Personal Information
The task for this section includes writing a simple Python script for printing the name, affiliation, and the name of the gene each team member loves most, and the name of the organism bearing the gene. The final output was to look like the following example: “Hi, my name is (name), a (position at one's institution). My favourite gene is (gene name) in (organism).”

Here is the solution:
```py
# Assign personal information to variables
name = "David Sunday"
affiliation = "Research Associate at the Federal University of Technology, Akure, Nigeria"
favourite_gene = "AKT1"
organism = "Homo sapiens"

# Import display, Markdown to display output in Markdown format so that scientific terms can appear in italics.
from IPython.display import display, Markdown

# Use the f-string to print out the desired information as specified in the task.
display(Markdown(f'"Hello, my name is {name}. I am a {affiliation}. My favourite gene is *{favourite_gene}*, which is found in *{organism}*."'))
```

## Part 2: Essay (Technical) Writing
The main objective of this section was to enable interns develop essential technical writing skills, focusing on clear and concise communication of complex scientific concepts. This includes learning how to document research findings, writing reports, and creating educational content that is accessible to both scientific and general audiences.

Hence, as a team, we selected a topic of interest from the list of the provided topics and wrote our essay as follows:

# From Sequence to Insight: How AI Turns Raw DNA into Biological Knowledge
### Introduction
Next-generation sequencing (NGS) can now produce complete genomes in days, but leaves researchers with overwhelming volumes of genomic datasets containing raw nucleotide bases A, T, G, and C. On their own, these letters do not immediately reveal which microbes are drug-resistant, which variants are clinically relevant, or how a protein will fold. Artificial intelligence (AI) has emerged as a powerful partner in genomics, learning patterns across large datasets to link DNA sequences to phenotypes, structures, and clinical outcomes [1]. This shift from reading genomes to understanding them is reshaping the fields of microbiology, oncology, and precision medicine.

### Why AI is Necessary
NGS generates massive high dimensional data that are difficult to interpret using classical rule-based bioinformatics alone. Studies on AI–NGS integration emphasise that the main bottleneck is no longer sequencing itself but the accurate and scalable analysis of reads, variants, and multi omics signals. Machine learning and deep learning models can exploit subtle non linear relationships in these data, improving speed and accuracy while coping with noise and incomplete annotations. In antimicrobial resistance (AMR) research, AI is increasingly seen as essential for handling the diversity of pathogens, resistance mechanisms, and clinical settings [1][2].

### What AI Actually Does to DNA
First, AI connects the genotype to the phenotype in microbial genomics and AMR prediction. Studies have shown that machine learning models trained on genomic features can predict resistance profiles, identify novel resistance markers, and support real time surveillance of emerging AMR threats [2][3]. These tools complement traditional susceptibility testing and have the potential to guide earlier and more targeted therapy.

Second, AI infers protein structure and function from protein sequence. The AlphaFold system, reported in Nature, uses deep neural networks to predict three dimensional protein structures from amino acid sequences with accuracy competitive with experimental methods in many cases. This breakthrough helps bridge the gap between the vast number of known sequences and the relatively small fraction of experimentally solved structures, enabling large scale structural bioinformatics and mechanistic insight [4].

Third, AI interprets the large data streams produced by NGS. Studies highlight AI driven advances in base calling, variant detection, error correction, and integrative analysis of cancer genomes, and other complex datasets [5][6]. These methods reduce noise, prioritise clinically important variants, and automate parts of the reporting process, making high throughput sequencing more actionable in research and clinical practice.

### Future Envision: What AI Could Do Next
Looking forward, AI is expected to act as an end to end co pilot for genomic medicine, from experimental design to bedside decision making. Future systems may jointly analyse genomes, transcriptomes, microbiomes, clinical records, and imaging to deliver individualised risk predictions, treatment recommendations, and forecasts. Generative models could design novel antimicrobials or synthetic biological circuits directly from desired functional properties, accelerating drug discovery and synthetic [1][6].

### Conclusion
AI is transforming raw DNA sequences into actionable biological knowledge, enabling rapid AMR prediction, accurate protein structure modelling, and scalable interpretation of complex NGS datasets. However, these models depend on data quality, can encode biases, and are often difficult to interpret or validate across diverse populations and laboratories. Used critically and transparently, AI will remain a powerful partner rather than a replacement for human expertise in understanding the genome.

### References
1.	Athanasopoulou K, Michalopoulou VI, Scorilas A, Adamopoulos PG. Integrating Artificial Intelligence in Next-Generation Sequencing: Advances, Challenges, and Future Directions. Curr Issues Mol Biol. 2025 Jun 19;47(6):470. doi: 10.3390/cimb47060470. PMID: 40699869; PMCID: PMC12191491.
2.	Ali T, Ahmed S, Aslam M. Artificial Intelligence for Antimicrobial Resistance Prediction: Challenges and Opportunities towards Practical Implementation. Antibiotics (Basel). 2023 Mar 6;12(3):523. doi: 10.3390/antibiotics12030523. PMID: 36978390; PMCID: PMC10044311.
3.	Hatim A N, Ammar Abdul Razzak M, Sriram T, Rajkumar Krishnan V, Desh NS. Artificial intelligence in Combating Antimicrobial Resistance. Arch Razi Inst. 2025 Jun 30;80(3):605-613. doi: 10.32592/ARI.2025.80.3.605. PMID: 41769288; PMCID: PMC12936619.
4.	Jumper J, Evans R, Pritzel A, Green T, Figurnov M, Ronneberger O, Tunyasuvunakool K, Bates R, Žídek A, Potapenko A, Bridgland A, Meyer C, Kohl SAA, Ballard AJ, Cowie A, Romera-Paredes B, Nikolov S, Jain R, Adler J, Back T, Petersen S, Reiman D, Clancy E, Zielinski M, Steinegger M, Pacholska M, Berghammer T, Bodenstein S, Silver D, Vinyals O, Senior AW, Kavukcuoglu K, Kohli P, Hassabis D. Highly accurate protein structure prediction with AlphaFold. Nature. 2021 Aug;596(7873):583-589. doi: 10.1038/s41586-021-03819-2. Epub 2021 Jul 15. PMID: 34265844; PMCID: PMC8371605.
5.	Srivastava A, Tripathi S, R R, Jani P, Singh M, Podder A, Mustafa M, Patwa MK. Implementation of AI for predicting antibiotic resistance patterns: A hospital-based study. Bioinformation. 2025 Oct 31;21(10):3636-3639. doi: 10.6026/973206300213636. PMID: 41623846; PMCID: PMC12859369.
6.	Davis L. Application of Artificial Intelligence in Genomic Data Interpretation. American Journal of Bioinformatics. 2022. 3(12):7-11. https://australiansciencejournals.com/bionformatics/article/view/1199/1293. 

