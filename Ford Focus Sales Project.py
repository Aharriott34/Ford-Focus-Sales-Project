import sqlite3 as sql
import matplotlib.pyplot as plt
# Ford Focus US Sales website: https://carsalesbase.com/us-ford-focus/
# Ford Focus generations. Mk1:1998-2004, Mk2:2005-2011, Mk3:2012-2019

# Creating a class to input data for SQL.
class Cars:
    def __init__(self, year, units_sold, generation):
        self.year = year
        self.units_sold = units_sold
        self.generation = generation

    def __repr__(self):
        return f"Ford Focus - Year: {self.year}, Units Sold: {self.units_sold}, Generation: {self.generation}"

# Creating SQL database.
conn = sql.connect(':memory:')
curs = conn.cursor()

curs.execute("""CREATE TABLE Ford_Focus
               (year INTEGER,
                units_sold INTEGER,
                generation TEXT)""")

# Inserting class into SQL database.
def insert_item(data):
    with conn:
        curs.execute("INSERT INTO Ford_Focus VALUES (:year, :units_sold, :generation)", {"year": data.year, "units_sold": data.units_sold, "generation": data.generation})

# Mk1 Focus
year_1 = Cars(1999, 55846, "Mk1 Focus")
year_2 = Cars(2000, 286166, "Mk1 Focus")
year_3 = Cars(2001, 264414, "Mk1 Focus")
year_4 = Cars(2002, 243199, "Mk1 Focus")
year_5 = Cars(2003, 229353, "Mk1 Focus")
year_6 = Cars(2004, 208339, "Mk1 Focus")
# Mk2 Focus
year_7 = Cars(2005, 184825, "Mk2 Focus")
year_8 = Cars(2006, 177006, "Mk2 Focus")
year_9 = Cars(2007, 173213, "Mk2 Focus")
year_10 = Cars(2008, 195823, "Mk2 Focus")
year_11 = Cars(2009, 160433, "Mk2 Focus")
year_12 = Cars(2010, 172421, "Mk2 Focus")
year_13 = Cars(2011, 175717, "Mk2 Focus")
# Mk3 Focus
year_14 = Cars(2012, 245922, "Mk3 Focus")
year_15 = Cars(2013, 234570, "Mk3 Focus")
year_16 = Cars(2014, 219634, "Mk3 Focus")
year_17 = Cars(2015, 202478, "Mk3 Focus")
year_18 = Cars(2016, 168789, "Mk3 Focus")
year_19 = Cars(2017, 158385, "Mk3 Focus")
year_20 = Cars(2018, 113345, "Mk3 Focus")
year_21 = Cars(2019, 12480, "Mk3 Focus")

# Inserting information into SQL table.
item_1 = insert_item(year_1)
item_2 = insert_item(year_2)
item_3 = insert_item(year_3)
item_4 = insert_item(year_4)
item_5 = insert_item(year_5)
item_6 = insert_item(year_6)
item_7 = insert_item(year_7)
item_8 = insert_item(year_8)
item_9 = insert_item(year_9)
item_10 = insert_item(year_10)
item_11 = insert_item(year_11)
item_12 = insert_item(year_12)
item_13 = insert_item(year_13)
item_14 = insert_item(year_14)
item_15 = insert_item(year_15)
item_16 = insert_item(year_16)
item_17 = insert_item(year_17)
item_18 = insert_item(year_18)
item_19 = insert_item(year_19)
item_20 = insert_item(year_20)
item_21 = insert_item(year_21)

# Returns years from SQL.
def year_items():
    curs.execute("SELECT year FROM Ford_Focus;")
    data = curs.fetchall()
    return data

# Returns units sold from SQL
def sold_items():
    curs.execute("SELECT units_sold FROM Ford_Focus;")
    data = curs.fetchall()
    return data

# Returns generation from SQL.
def gen_items():
    curs.execute("SELECT generation FROM Ford_Focus;")
    data = curs.fetchall()
    return data

# Returns all data from SQL.
def all_items():
    curs.execute("SELECT * FROM Ford_Focus;")
    data = curs.fetchall()
    return data

# Returns a select number of data points (ordered by year).
def select(num):
    curs.execute("SELECT * FROM Ford_Focus;")
    data = curs.fetchmany(num)
    return data

# Total amount of units sold.
def units_sum():
    curs.execute("SELECT SUM(units_sold) FROM Ford_Focus;")
    data = curs.fetchall()
    return data

# Returns data for the most amount of units sold.
def most_sold():
    curs.execute("SELECT * FROM Ford_Focus ORDER BY units_sold DESC LIMIT 1 OFFSET 0;")
    data = curs.fetchone()
    return data

# Returns data for the least amount of units sold.
def least_sold():
    curs.execute("SELECT * FROM Ford_Focus ORDER BY units_sold LIMIT 1 OFFSET 0;")
    data = curs.fetchone()
    return data

# Sum of each generation of Ford Focus.
def genration1_sum():
    curs.execute("SELECT SUM(units_sold), generation FROM Ford_Focus WHERE generation LIKE '%Mk1%'")
    data = curs.fetchall()
    return data

def genration2_sum():
    curs.execute("SELECT SUM(units_sold), generation FROM Ford_Focus WHERE generation LIKE '%Mk2%'")
    data = curs.fetchall()
    return data

def genration3_sum():
    curs.execute("SELECT SUM(units_sold), generation FROM Ford_Focus WHERE generation LIKE '%Mk3%'")
    data = curs.fetchall()
    return data

# Splitting the generation and units sold per generation into two lists.
gen_total = []
gen_name = []
all_gen = [genration1_sum(),genration2_sum(),genration3_sum()]
for key in all_gen:
    key_1 = [x[0] for x in key]
    key_2 = [x[1] for x in key]
    gen_total.append(key_1)
    gen_name.append(key_2)

# Converting nested lists (gen_total, gen_name, year_items(), sold_items()) to a flat list.
fixed_list = [item for elem in gen_total for item in elem]
label = [item for elem in gen_name for item in elem]
years = [item for elem in year_items() for item in elem]
units_sold = [item for elem in sold_items() for item in elem]
pie_legend = ["Mk1:1998-2004", "Mk2:2005-2011", "Mk3:2012-2019"]

# Labels for the bar graph.
def labels(stats, figure):
    for index, value in enumerate(stats):
        figure.annotate(str(value), xy=(index, value), va="bottom", ha='center')


# Range list for line chart x-axis.
year_ticks = list(range(1999, 2020))
year_short = ["99", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]

# Creating subplots
plt.style.use('seaborn')
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)

# Creating pie chart.
fig.suptitle("Ford Focus Statistics")
ax1.set_title("Sales by Generation")
ax1.pie(fixed_list, labels=label,wedgeprops={'edgecolor': 'black'}, shadow=True, autopct='%1.1f%%', startangle=25)
ax1.legend(pie_legend, title="Generation by Year", loc=0, bbox_to_anchor=(1.0, 1.0), frameon=True)

# Creating bar graph
ax2.set_title("Sales by Generation")
ax2.bar(label, fixed_list)
ax2.set_xlabel("Generations")
ax2.set_yticks([0, 500000, 1000000, 1500000, 2000000])
ax2.set_yticklabels(["0", "500K", "1M", "1.5M", "2M"])
ax2.set_ylabel("Units Sold")
labels(fixed_list, ax2)

# Creating line graph.
ax3.set_title("Sales by Year")
ax3.plot(years, units_sold,linestyle="dashed", marker="o")
ax3.set_xlabel("Years (1999-2019)")
ax3.set_ylabel("Units Sold")
ax3.set_yticks([0, 50000, 100000, 150000, 200000, 250000, 300000])
ax3.set_yticklabels(["0", "50K", "100K", "150K", "200K", "250K", "300K"])
ax3.set_xticks(year_ticks)
ax3.set_xticklabels(year_short)


plt.tight_layout()
plt.savefig("Ford Focus Stats.png", bbox_inches='tight', dpi=300)
plt.show()

conn.commit()
conn.close()