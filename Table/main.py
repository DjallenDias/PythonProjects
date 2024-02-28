import table

# The values and keys to the dictionary
chaves = ['names', 'ages']
valores = [['john', 'mary'],[18,20]]

# Creating the dict and showing
itable = table.ItemTable(chaves, valores)
itable.show_table()

print(itable.sum_all_columns())
print(itable.mean_all_columns())

# Filter condition
def cond(line):
    if line["ages"] > 19:
        return True
        
    else: return False

# Show the table filtered based on the above function
print(itable.filter_line(cond))

itable.add_line(["peter",30])
itable.show_table()

print(itable.sum_all_columns())
print(itable.mean_all_columns())

itable.add_column("sex",["m","f","m"])
itable.show_table()

itable.rem_column("sex")
itable.show_table()

itable.rem_line(-1)
itable.show_table()



csv_chaves, csv_valores = table.csv_reader("csv path") # Function to open a csv

csvtable = table.ItemTable(csv_chaves,csv_valores)
csvtable.show_table()