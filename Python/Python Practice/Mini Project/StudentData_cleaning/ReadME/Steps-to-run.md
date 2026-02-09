Steps to run this project:



1\. Add your student raw data csv in your "**data -> input data**" folder.

If the data is in excel format you can convert it to csv through "**excel\_to\_csv.py**" file.

2\. Make changes in the config file, "**config -> config.json**" according to your recruitments (Changing the graduation year and allowed-locations)

3\. In "**main.py**" file mention your input csv file path and your desired output csvs name.

4\. The output will be stored in "**data -> output data**" folder and two csvs; valid\_students and invalid\_students will be stored separately.



---------------------------------------------------------------------------

**Config file**



--> This file is used to specify the requirements without changing it directly in the code



Entries to change:

"**allowed\_year**" - This entry specifies the graduation year which we are considering for recruitment

"**allowed\_locations**" - This specifies the college locations which will be considered for recruitment

"**csv\_column\_mapping**" - This is used to specify the column headers which are used in our input csv and assigning it to our defined names



You can make changes in this config file according to your specifications



---------------------------------------------------------------------------

**main.py**



--> This main file is run to make the automated process activate



Entries to change:

Mention the **input csv** and **output csvs** path and the names by which you want to save the output csvs

