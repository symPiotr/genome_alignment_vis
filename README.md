# genome_alignment_vis

The workflow makes a nucmer- or promer-like plot comparing genomes within two FASTA files, and visualizes the contigs using pre-defined colors.
Inputs include:
  a) Reference FASTA file
  b) Reference GFF file made by the symCAP script
  c) Query FASTA file, with one or more genomes
  d) Query GFF file, for one genome - or concatenated GFFs for many or more genomes
  d) File with information on gene categories to be highlighted, genes in each category

The steps include:
  1) Convert Query and Reference GFFs to simplified, comma-delimited output: script **process_gff_20250226.py**
  2) Conduct a blast-based comparison of Query vs Reference, and parse the results: script **visualize_genome_comparisons.py**
  3) Visualize the resulting files using Processing **Promer_style_genome_comparison_alignment_20250221**


