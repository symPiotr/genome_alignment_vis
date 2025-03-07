add_library('pdf')

### Where output PDF should be saved
Output_name = "/Users/piotrlukasik/Processing_stuff/20250221_Promer-style_contig_alignment_plot/VFPs_vs_VFOLIH_evalue_1e-20.pdf"

### File with information on the Reference genome size, and coordinates of different genes, provided by the "process_gff.py" script based on a GFF
Reference_PRO_file = "/Users/piotrlukasik/bioinfo/20250307_Genome_comparison_vis/VFOLIH.pro"

### File with information on the coordinates/annotations of particular bases within the Query genome
Vis_data_file = "/Users/piotrlukasik/bioinfo/20250307_Genome_comparison_vis/VFPs_vs_VFOLIH.csv"

### How gene cotegories should be colored
Gene_colors  = {'rRNA': [200,0,0],
                'Metabolism': [250,250,0],
                'Biosynthesis': [255,0,255],
                'Genetic_information_processing': [0,200,0],
                'Other': [160,160,160]}
Gene_category_list = Gene_colors.keys()


size(2400, 4000)   ### drawing board width and height. Make sure to position manually the start_x and start_y positions relative to these numbers
beginRecord(PDF, Output_name)
background(255)

###

scale_x = 70    ### How many bps in a pixel
scale_y = 350   ### How many bps in a pixel
scale_tick = 10000
start_x = 150
start_y = 3750  ### Set 200 bp less than drawing board height!




### Function for setting FILL color, of contigs or legend
def SelectColor(taxon, opacity):
    if taxon in Gene_category_list:
        fill(Gene_colors[taxon][0],Gene_colors[taxon][1],Gene_colors[taxon][2],opacity)
    return("")

### Function for setting STROKE color, of contigs or legend
def SelectColor2(taxon, opacity):
    if taxon in Gene_category_list:
        stroke(Gene_colors[taxon][0],Gene_colors[taxon][1],Gene_colors[taxon][2],opacity)
    return("")



REFERENCE = loadTable(Reference_PRO_file, "csv") 
"""
genome_entry,TETULN,150282,
TETULN,16S_rRNA,rRNA,1,1482,+,
TETULN,rplU,riboprot,4861,5196,-,
"""

QUERIES = loadTable(Vis_data_file, "csv")

"""
genome_entry,TETUND2,140570
TETUND2,1,1.0,+,16S_rRNA,rRNA
TETUND2,71,72.67293051941795,+,16S_rRNA,rRNA
TETUND2,141,144.3458610388359,+,16S_rRNA,rRNA
"""


Reference_genome_name = REFERENCE.getRow(0).getString(1)
Reference_genome_size = REFERENCE.getRow(0).getInt(2)



### Draw QUERY positions and functions
baseline_y = start_y - 20
query_size = 0

f = createFont("Arial",16)
textAlign(RIGHT)
textFont(f,24)



for k in range(0, QUERIES.getRowCount()-1):
    Entry = QUERIES.getRow(k)
    if Entry.getString(0) == "genome_entry":
        if not k == 0:
            baseline_y -= query_size/scale_y
            stroke(0)
            strokeWeight(1)
            line(start_x,baseline_y,start_x+Reference_genome_size/scale_x,baseline_y)
        query_size =  Entry.getInt(2)
        fill(0)
        text(Entry.getString(1), start_x-10, baseline_y-query_size/2/scale_y)
    else:
        base_q = Entry.getFloat(1)
        base_r = Entry.getFloat(2)
        Orientation = Entry.getString(3)
        Gene_category = Entry.getString(5)
        Functionality = "Functional"
        
        
        if Gene_category in Gene_category_list:
            strokeWeight(2)
            SelectColor2(Gene_category,255)
            line(start_x + base_r/scale_x, baseline_y-base_q/scale_y-5, start_x + base_r/scale_x, baseline_y-base_q/scale_y+5)
        else:
            stroke(0)
            strokeWeight(1)
            line(start_x + base_r/scale_x, baseline_y-base_q/scale_y-1, start_x + base_r/scale_x, baseline_y-base_q/scale_y+1)

baseline_y -= query_size/scale_y





### Draw main frame
fill(0,0,0,0)
strokeWeight(2)
stroke(0)
rect(start_x, start_y, Reference_genome_size/scale_x, baseline_y-start_y)

strokeWeight(1)
for tick in range(0,Reference_genome_size,scale_tick):
    stroke(150)
    line(start_x+tick/scale_x, start_y+30, start_x+tick/scale_x, baseline_y)
    textFont(f,24)
    fill(0)
    textAlign(CENTER)
    text(str(tick/1000)+"k",start_x+tick/scale_x, start_y+55)
    



### Draw REFERENCE genes
for i in range(1, REFERENCE.getRowCount()):   ### For each gene entry for a reference:
    Entry = REFERENCE.getRow(i)
    Gene = Entry.getString(1)
    Gene_category = Entry.getString(2)
    Gene_start = Entry.getInt(3)
    Gene_end = Entry.getInt(4)
    Gene_orientation = Entry.getString(5)
    Gene_functionality = "Functional"

    ### Print some gene details to console
    print(Gene, Gene_category, Gene_start)# Gene_end, Gene_orientation)
    stroke(0)
    strokeWeight(0)

    """
    ### Draw a translucent boxe - extending from annotated Reference gene up.
    if Gene_category != "Other":
        SelectColor(Gene_category,30)
        strokeWeight(0)
        rect(start_x+Gene_start/scale_x, start_y, (Gene_end-Gene_start)/scale_x, -(start_y-baseline_y))
    """
    
    ### Draw a reference gene
    SelectColor(Gene_category,255)
    strokeWeight(0)
    if Gene_functionality == "Functional":
        if Gene_orientation == "+":
            rect(start_x+Gene_start/scale_x, start_y, (Gene_end-Gene_start)/scale_x, -15)
        else:
            rect(start_x+Gene_start/scale_x, start_y+15, (Gene_end-Gene_start)/scale_x, -15)


### Draw LEGEND
textFont(f,36)
fill(0)
textAlign(LEFT)
text("Annotated %s genome (%sbp)" % (Reference_genome_name, Reference_genome_size), start_x, start_y+100)

textFont(f,20)

legend_item_x = 200
for i in range(len(Gene_category_list)):
    SelectColor(Gene_category_list[i], 255)
    rect(legend_item_x,start_y+130,40,30)
    text(Gene_category_list[i], legend_item_x+50, start_y+160)
    legend_item_x += 300

println("Finished drawing plot!")
endRecord()
