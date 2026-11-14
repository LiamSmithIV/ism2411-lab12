



import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

# Exercise 2
print("=== Exercise 2: Raw rows ===")
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