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


