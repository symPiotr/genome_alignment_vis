# genome_alignment_vis

This draft workflow makes a nucmer- or promer-like plot comparing genomes within two FASTA files, and visualizes the contigs using pre-defined colors.

Inputs include:  
  1) Reference FASTA file
  2) Reference GFF file made by the symCAP script
  3) Query FASTA file, with one or more genomes
  4) Query GFF file, for one genome - or concatenated GFFs for many or more genomes
  5) File with information on gene categories to be highlighted, genes in each category

The steps include:
  1) Converting Query and Reference GFFs to a simplified csv output: Python 3 script **process_gff_20250226.py**
  2) Conduct a tblastx-based comparison of Query vs Reference, parse the results, add query annotation information, and export ready-for-visualization file: Python 3 script **visualize_genome_comparisons_20250226.py**
  3) Visualize the resulting files: Processing 3 (Python mode) script **Promer_style_genome_comparison_alignment_20250221**
... and are described in more details below.

    
### process_gff_20250226.py
The script processes a GFF file, such as the one made by the symCAP script, to a simplified format for visualization.

Usage:
```
./process_gff_20250226.py              
This script processes a gff file - like the one produced by symCAP script -
and the second tab-delimited file with info on assignment of genes to pre-defned categories,
and returns to stdout a table to be used as an input of genome_plotting.
It direct the output to STDOUT - you probably want to redirect it to a file instead.
Usage: ./process_gff_20250226.py <gff_file> <categories_file>

./process_gff_20250226.py SMDICMUL.gff Sulcia_gene_categories.txt > SMDICMUL.pro 
```

Example input - `SMDICMUL.gff`:
```
##gff-version 3
##sequence-region  SMDICMUL 1 142701
SMDICMUL	HMMER_3.1b2	gene	1	645	.	+	0	ID=gene_001;locus_tag=SMDICMUL_001;gbkey=Gene;gene_biotype=protein_coding;gene=lipB;name=lipB;
SMDICMUL	HMMER_3.1b2	CDS	1	645	.	+	0	ID=product_001;Parent=gene_001;locus_tag=SMDICMUL_001;gbkey=CDS;gene=lipB;product=Octanoyltransferase;transl_table=11;codon_start=1
SMDICMUL	HMMER_3.1b2	gene	674	3217	.	+	0	ID=gene_002;locus_tag=SMDICMUL_002;gbkey=Gene;gene_biotype=protein_coding;gene=valS;name=valS;
SMDICMUL	HMMER_3.1b2	CDS	674	3217	.	+	0	ID=product_002;Parent=gene_002;locus_tag=SMDICMUL_002;gbkey=CDS;gene=valS;product=Valine--tRNA ligase;transl_table=11;codon_start=1
SMDICMUL	rnammer_1.2	gene	62387	62491	.	-	0	ID=gene_072;locus_tag=SMDICMUL_072;gbkey=Gene;gene_biotype=rRNA;gene=gene;name=gene;
SMDICMUL	rnammer_1.2	rRNA	62387	62491	.	-	0	ID=product_072;Parent=gene_072;locus_tag=SMDICMUL_072;gbkey=rRNA;product=product;note=inference:RNAmmer 1.2
```

Example input - `Sulcia_gene_categories.txt`:
```
lipB	Metabolism
valS	Genetic_information_processing
```

Example output - `SMDICSEM.pro`:
```
genome_entry,SMDICMUL,142701,
SMDICMUL,lipB,Metabolism,1,645,+,
SMDICMUL,valS,Genetic_information_processing,674,3217,+,
SMDICMUL,unnamed_gene,rRNA,62387,62491,-,
```



