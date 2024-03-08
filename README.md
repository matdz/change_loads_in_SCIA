## XML - SCIA Engineer

## Context
Immagina di avere un modello SCIA delle fondazioni di un ponte. L'ingegnere che ha calcolato la struttura ti fornisce le reazioni da inserire per calcolare le fondazioni ma dopo una settimana i carichi sono cambiati e bisogna rifare tutto. Questo script permette di aggiornare i carichi sulle fondazioni automatiamente.

## First thing
- Create a copy of the SCIA model
- File > Export to > XML file
- Add "Point forces in node" and "Moment in node" and click on "Export"
- Save the xml file, open it, select everything, copy it and paste it in data.txt

## Python script: first_step.py
Edit the node in "node_scia" and run the python script.

## CSV file: output.csv
Open the file output.csv, select everything and paste it in column A in phases.xlsx.

## Excel file: phases.xlsx
Write, in column H, the load cases you would like to change. The excel automatically detects the force load and the moment in the node and insert them in a table.
From column P to V, add the load cases and the values you would like to have, in kN and kNm.
From column X to AB, be sure that the table is selected.
You can copy the text from column AE.

## Python script: second_step.py
You can paste the text in data_2.txt.
Check the value of node_scia and run second_step.py.
Copy the XML file you created before and give a new name. You can remove the text inside.
Open data_3.txt, select everything, copy the text and paste it in new XML file. Close all the files.

## Last step
In SCIA Engineer, you can open the copy of your model and go to File > Update from > XML file.
Your loads are now updated!



