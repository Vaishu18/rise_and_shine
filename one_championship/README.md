The project one_championship contains the following two files
1. solution_sql.sql 
2. data_parse.py

Problem statements
1. SQL: 

One Championship conducts events in a stadium, each event many people visit it and the stats are saved as these columns: id, event_name, people_count

Take leverage in adding sample data yourself.
Please write a query to display the records which have 3 or more consecutive events and the amount of people more than 100(inclusive).

**Solution**

*solution_sql.sql* contains the answer for this

2. Data Parsing: 

Write code to extract data from **data.csv**.

The data contains four columns. The first column is the person identifier. The second column is the datetime the person entered the floor. The third column is the floor the person accessed. The fourth column specifies the building the floor is in.

Each row is considered a floor access event. Your task it to output each floor access event in json format. Each event should comply with the schema located in **schema.json**.

You may use any programming language. When finished, upload code to your Github account and send us the link. Please include instructions on how to execute and test code. Good luck!

**Solution**

To run the program to parse the data you need the following external packages:
pandas
jsonschema

Command to execute:
**python data_parse.py <csv filepath> <schema filepath>**

The output will be displayed on the terminal console.

Eg:
python data_parse.py ./data.csv ./schema.json
