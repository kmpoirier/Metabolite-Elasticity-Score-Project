# Metabolite-Elasticity-Score-Project

cleanFeatureTable.py is a python file that:
- Reads featue_table_ex_meta.csv (metadata file)
- Loops through each organ type and post infection days
    - Separates by each organ type 
    - Groups by condition and calculates the median value of infected and median value of uninfected and adds 0.5 to every value
    - 𝑙𝑛 (𝑚𝑒𝑑𝑖𝑎𝑛 𝑖𝑛𝑓𝑒𝑐𝑡𝑒𝑑 + 0.5)/(𝑚𝑒𝑑𝑖𝑎𝑛 𝑢𝑛𝑖𝑛𝑓𝑒𝑐𝑡𝑒𝑑 + 0.5)
    - Calculates p values using Mann–Whitney U test comparing infected with uninfected of each metabolite
- Produces a txt file that includes logFC and p-value for timepoint 12 days and 89 days for each organ and saves it in a individual folders
- Note: before running this code, make sure to have a individual folders for each organ type (for example, organ type '1' should have its own folder
- Each organ folder should have a newratio_12.txt and newratio_89.txt

