# Metabolite-Elasticity-Score-Project

## cleanFeatureTable.py is a python file that:
- Reads featue_table_ex_meta.csv (metadata file including feature table)
- Loops through each organ type and post infection days
    - Separates by each organ type 
    - Groups by condition and calculates the median value of infected and median value of uninfected and adds 0.5 to every value
    - 𝑙𝑛 (𝑚𝑒𝑑𝑖𝑎𝑛 𝑖𝑛𝑓𝑒𝑐𝑡𝑒𝑑 + 0.5)/(𝑚𝑒𝑑𝑖𝑎𝑛 𝑢𝑛𝑖𝑛𝑓𝑒𝑐𝑡𝑒𝑑 + 0.5)
    - Calculates p values using Mann–Whitney U test comparing infected with uninfected of each metabolite
- Produces a txt file that includes logFC and p-value for timepoint 12 days and 89 days for each organ and saves it in a individual folders
- Note: before running this code, make sure to have a individual folders for each organ type (for example, organ type '1' should have its own folder
- Each organ folder should have a newratio_12.txt and newratio_89.txt


## MElaS.Rmd is a R notebook that uses the code from (Zhou, et.al (2022)) with some midifications that:
- Reads in both newratio_12.txt and newratio_89.txt for each organ
- Calculate Elastic Score  
- Produces MElaS.txt file for each organ containing MElaS of each metabolite
  
### Paper and GitHub refrenced in this code:
Zhou, Q., Yu, L., Cook, J.R., Qiang, L. & Sun, L. 2023, Cell Metabolism, 35, 1661-167.e6, doi: 10.1016/j.cmet.2023.08.001.
https://github.com/zhouqz/GElaS

## MElaSPlots.Rmd is a R notebbok that:
- Reads in MElaS.txt for each organ
- Filters out the top and bottom MElaS score
- Makes plots for LogFC between 12 and 89 days of the top 10 metabolites with the highest elasticity scores
- Makes plots for LogFC between 12 and 89 days of the bottom 10 metabolites with the lowest elasticity scores
- Makes boxplot comparing peak areas of each top/bottom MElaS metabolites by post infection days and condition. A box plot is produced for each metabolite 









