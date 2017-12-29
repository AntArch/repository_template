
# coding: utf-8

# # This should currently be run under virtual env py2_lrs_etl
# 
# > source activate py2_lrs_etl

# In[1]:

import os
import re
import itertools
import nbformat
import shutil
import time



NOTEBOOK_DIR = os.path.join(os.path.dirname(__file__), '..', 'notebooks')


# regular expression filter to subset the files by naming pattern

REG = re.compile(r'(\d\d)\.(\d\d)-(.*)\.ipynb')


# In[2]:

#  Set current directory as working directory - when working in jupyter
# (Change this if appropriate)
#NOTEBOOK_DIR = os.getcwd()
#print(NOTEBOOK_DIR)
#NOTEBOOK_DIR = os.path.abspath(os.path.join(os.path.dirname(NOTEBOOK_DIR), 'notebooks'))
#print(NOTEBOOK_DIR)


# In[3]:

def iter_notebooks():
    return sorted(nb for nb in os.listdir(NOTEBOOK_DIR) if REG.match(nb))

# This is deprecated
def export_ipynb_to_md(fileLoc,output_md):
    
    #fileLoc = os.path.join( NOTEBOOK_DIR, nb )[:-5]
    print(fileLoc)
    # convert notebook to markdown and clear any output cells
    cLS = 'jupyter nbconvert --to markdown --ClearOutputPreprocessor.enabled=True ' +fileLoc+'ipynb'
    os.system(cLS)
    # strip any navigation text
    cLS = "sed -i '/^</d' " +fileLoc+"md"
    os.system(cLS)
    cLS = "sed -i '/^| /d' " +fileLoc+"md"
    os.system(cLS)
    # strip any svg issue
    cLS = "sed -i '/^!\[svg/d' " +fileLoc+"md"
    os.system(cLS)
    # write files to new file
    cLS = "cat " +fileLoc+"md >>  " +output_md
    os.system(cLS)
    #delete source md file (if exists)
    try:
        os.remove(fileLoc+'md')
    except OSError:
        pass

def export_ipynb_to_md_odp(fileLoc,output_md):
    
    #fileLoc = os.path.join( NOTEBOOK_DIR, nb )[:-5]
    print(fileLoc)
    # convert notebook to markdown and clear any output cells: this is a bit unfortunate as I now want to keep some of these output cells
    #cLS = 'jupyter nbconvert --to markdown --ClearOutputPreprocessor.enabled=True ' +fileLoc+'ipynb'
    ##### I really want this to work but it doesn't (well it does in the terminal but not as cLS)
    ##### jupyter nbconvert --to markdown --ExtractOutputPreprocessor.enabled=True 05.00-Proof-of-concept.ipynb
    #cLS = 'jupyter nbconvert --to markdown --ExtractOutputPreprocessor.enabled=True ' +fileLoc+'ipynb'
    cLS = 'jupyter nbconvert --to markdown ' +fileLoc+'ipynb'
    print(cLS)
    os.system(cLS)
    # strip any navigation text
    cLS = "sed -i '/^</d' " +fileLoc+"md"
    os.system(cLS)
    cLS = "sed -i '/^| \[/d' " +fileLoc+"md"
    os.system(cLS)
    # strip any svg issue
    cLS = "sed -i '/^!\[svg/d' " +fileLoc+"md"
    os.system(cLS)
    #convert the relative image paths to absolute
    ## those in the figures folder
    cLS = "sed -i s@\(figures@\(" +NOTEBOOK_DIR+"/figures@g "+fileLoc+"md"
    os.system(cLS)
    ## those created inline
    cLS = "sed -i 's@!\[png\](@!\[png\](" +NOTEBOOK_DIR+"/@g' "+fileLoc+"md"
    os.system(cLS)    
    # write files to new file
    cLS = "cat " +fileLoc+"md >>  " +output_md
    os.system(cLS)
    # strip out tables which aren't currently supported and place in temporary file
    #cLS = "sed '/^|/d' " +fileLoc+"md > delme.md"
    #cLS = "sed '/^|/d' " +fileLoc+"md > "+fileLoc+"delme.md"
    os.system(cLS)


    # create the odp_output name
    output_odp = os.path.join( NOTEBOOK_DIR, 'exports',os.path.basename(fileLoc)+'odp' )

    # provide location and name of the ODP template
    odp_template = os.path.join( os.path.dirname(NOTEBOOK_DIR), 'tools','discreet-dark.odp' )

    # export as ODP presentation using odpdown
    #cLS = "odpdown --break-master=Discreet_25_20Dark1 --content-master=Discreet_25_20Dark delme.md "+odp_template+" "+output_odp
    cLS = "odpdown --break-master=Discreet_25_20Dark1 --content-master=Discreet_25_20Dark " +fileLoc+"md "+odp_template+" "+output_odp
    os.system(cLS)
    
    # export as ODP presentation to powerpoint
    #cLS = "soffice --headless --convert-to pptx "+output_odp
    #cLS = "cd ../notebooks/exports && soffice --headless --convert-to pptx "+output_odp+" && rm *.odp && cd ../../tools"
    #print(cLS)
    #os.system(cLS)
       
    #delete source md file (if exists)
    try:
        os.remove(fileLoc+'md')
    except OSError:
        pass
    #delete temporary file (if exists)
    try:
        os.remove('delme.md')
    except OSError:
        pass


# In[7]:

#get timestamp
timestr = time.strftime("%Y%m%d")

# create the timestamped markdown output name
output_md = os.path.join( NOTEBOOK_DIR, 'exports',timestr+'_workbook_export.md' )


#delete markdown file (if exists)
try:
    os.remove(output_md)
except OSError:
    pass

# Export all the ipynb as a markdown and concatenate into a single date stamped markdown file
for nb in iter_notebooks():
    print('Converting file: '+nb)
    fileLoc = os.path.join( NOTEBOOK_DIR, nb )[:-5]
    #export_ipynb_to_md(os.path.join( NOTEBOOK_DIR, nb )[:-5])
    #export_ipynb_to_md(fileLoc, output_md )
    export_ipynb_to_md_odp(fileLoc, output_md )




# # ODP export
# 
# Clean up the markdown prior to export
# 
# Manually remove the following:
# 
# * make sure there are no ### headers
# 

# In[5]:

#Convert markdown to ODP

# stip out tables which aren't yet supported

# strip out tables which aren't currently supported and place in temporary file
cLS = "sed '/^|/d' " +output_md+" > delme.md"
os.system(cLS)

# create the timestamped pdf output name
output_odp = os.path.join( NOTEBOOK_DIR, 'exports',timestr+'_workbook_export.odp' )

# provide location and name of the ODP template
#odp_template = os.path.join( os.path.dirname(NOTEBOOK_DIR), 'tools','discreet-dark_arb.odp' )
odp_template = os.path.join( os.path.dirname(NOTEBOOK_DIR), 'tools','discreet-dark.odp' )

# export as ODP presentation using odpdown
#cLS = "odpdown --break-master=Discreet_25_20Dark1 --content-master=Discreet_25_20Dark " +output_md+" "+odp_template+" "+output_odp
cLS = "odpdown --break-master=Discreet_25_20Dark1 --content-master=Discreet_25_20Dark delme.md "+odp_template+" "+output_odp
os.system(cLS)

#delete temporary file (if exists)
try:
    os.remove('delme.md')
except OSError:
    pass

#!!odpdown --break-master=Discreet_25_20Dark1 --content-master=Discreet_25_20Dark {output_md} {odp_template} {output_odp} 


# # PDF export
# 
# 

# In[ ]:

#Convert markdown to PDF

# create the timestamped pdf output name
output_pdf = os.path.join( NOTEBOOK_DIR, 'exports',timestr+'_workbook_export.pdf' )

cLS = "pandoc -f markdown -t latex -N -V geometry:margin=1in " +output_md+" --latex-engine=xelatex --toc -o "+output_pdf
print(cLS)
os.system(cLS)
#!!pandoc -f markdown -t latex -N -V geometry:margin=1in {output_md} --latex-engine=xelatex --toc -o {output_pdf}


# In[ ]:



