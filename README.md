# Store IMGT CDR Loops
Python version = 3.9.5

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

## License

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
