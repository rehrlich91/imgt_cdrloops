# Store IMGT CDR Loops

## Purpose and Use
This program takes CDR loop FASTA data from the IMGT database, sorts and stores the CDR loop information for variable genes (e.g. alpha and beta). For the latest data go to the IMGT database (https://www.imgt.org/genedb/) and enter the following in the ```Identification``` panel: ```Species```: Homo sapiens, ```Gene type```: Variable, ```Functionality```: Functional, ```Molecular componenet```: TR. Next, under ```Localization``` in ```Locus```, select the gene family of interest. In the example shown here, TRA and TRB are used. Lastly, press the ```Submit``` botton. 

The following page will contain a table of all TCR genes. Scroll to the end of the table and select the box next to "Select all genes". Below this box will be a ```Choose your display``` table, here select the following: for ```IMGT/GENE-DB allele reference sequences in FASTA format```: F+ORF+in-frame P amino acid sequences with IMGT gaps, ```IMGT label extraction from IMGT/LIGM-DB reference sequences (F+ORF+all P)```: Amino acid sequence, and press ```Submit```. 

The results of the query are shown next. Here the user simply copies and pastes the fasta text to a new text file (e.g. trav_alignment_imgt.txt). To store the following files in dictionaries do the following:

``` console
python extractCDRs.py -alpha trav_alignment_imgt.txt -beta trbv_alignment_imgt.txt
```

and to view the dictionaries:

``` console
python view_results.py -alpha alpha_genes.pickle -beta beta_genes.pickle
```
