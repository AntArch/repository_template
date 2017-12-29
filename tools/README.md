# Tools

These are tools for managing the notebooks in this repository.

- ``generate_contents.py``: this will generate a markdown table of contents for use in the README and in the Index.ipynb notebook

- ``add_navigation.py``: this script adds navigation links at the top and bottom of each notebook.

- ``export_all_as_md_pdf_and_odp.py``: this script exports everything as pdf and odp files. Requires a local install of pandoc and odpdown (use the follwing 'source activate py2_etl_lrs' then run in this environment)

when chained together they can be used to export and convert to pptx (powerpoint).

I set up a new conda env for this (py27) whihc is a basic environment.

This also needs odpdown installing:

> pip install odpdown

source activate py27 && python add_navigation.py && python export_all_as_md_pdf_and_odp.py

source activate py27 && python add_navigation.py && python export_all_as_md_pdf_and_odp.py && python generate_contents.py && cd ../notebooks/exports && touch delme.pptx && rm *.pptx && soffice --headless --convert-to pptx *.odp && rm *.odp && cd ../../tools


pandoc -f markdown  -N -V /home/beckant/git_shares/RoSRepositories/lr-workshop-master-material/notebooks/exports/20171222_workbook_export.md  --toc -o /home/beckant/git_shares/RoSRepositories/lr-workshop-master-material/notebooks/exports/20171222_workbook_export.docx

pandoc -f markdown -t latex -N -V geometry:margin=1in /home/beckant/git_shares/RoSRepositories/lr-workshop-master-material/notebooks/exports/20171222_workbook_export.md --latex-engine=xelatex --toc -o /home/beckant/git_shares/RoSRepositories/lr-workshop-master-material/notebooks/exports/20171222_workbook_export.pdf
