# ISM2411 Lab 12 — Read a Sales CSV, Write a Cleaned Report
# Name: Liam Smith 
#
# Reflection 1:
# Python is better because of its repeatability. Once the script is written, it can be reused the next day with just one command. 
# Python also allows for handling much larger files than Excel. Furthermore, Python prevents the redoing of filters and formulas necessary in Excel. 
# Excel can be better because you can see all data at once and is more friendly to those without coding knowledge. 

# Reflection 2:
# A company could use a script to track daily sales and then total revenue. Then, add one line to a log with the date and new total. Append is the right tool because you can see the history/log of the dates and see if any date is missing.  

import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

# Exercise 1
print("=== Exercise 1: File check ===")
with open(SALES_FILE, newline="") as f:
    print(f"{SALES_FILE} opened successfully")

# Exercise 2
print("\n=== Exercise 2: Raw rows ===")
with open(SALES_FILE, newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Exercise 3
print("\n=== Exercise 3: Header skipped ===")
with open(SALES_FILE, newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# Exercise 4
print("\n=== Exercise 4: Line totals ===")
total_revenue = 0.0
with open(SALES_FILE, newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

# Exercise 5
print("\n=== Exercise 5: Filter and write ===")
original_count = 0
written_count = 0
with open(SALES_FILE, newline="") as infile, open(CLEANED_FILE, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        original_count += 1
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        if line_total > 100:
            writer.writerow([row[0], f"{price:.2f}", quantity, f"{line_total:.2f}"])
            written_count += 1
print(f"Wrote {written_count} of {original_count} rows to {CLEANED_FILE}")

# Exercise 6
print("\n=== Exercise 6: DictReader ===")
dict_total = 0.0
with open(SALES_FILE, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        dict_total += line_total
        print(f"{row['product']}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${dict_total:.2f}")
# csv.reader accesses columns by position (row[1]), which works for files with no header or a fixed layout but breaks if columns move.
# DictReader accesses columns by name (row["price"]), which is easier to read and still works if columns are reordered, so I'd use it whenever the file has a header.

# Exercise 7
print("\n=== Exercise 7: Summary by product ===")
summary = {}
with open(SALES_FILE, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        line_total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + line_total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# Exercise 8
print("\n=== Exercise 8: Append to run log ===")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as log:
    log.write(f"{timestamp} | Total revenue: ${total_revenue:.2f}\n")
print(f"Logged this run to {LOG_FILE}")