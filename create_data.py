# create_data.py
import csv
import random
import datetime

# --- Parameters ---
NOMINAL_DIAMETER = 20.0
TOLERANCE = 0.05
TOTAL_BOLTS = 1000
FAILURE_RATE = 0.05 # 5% of bolts will be defective

# --- Data Generation ---
header = ['Timestamp', 'Bolt_ID', 'Diameter_mm']
data = []
start_time = datetime.datetime.now()

for i in range(TOTAL_BOLTS):
    bolt_id = f'BOLT-{i+1:04d}'
    time_stamp = (start_time + datetime.timedelta(seconds=i*5)).strftime('%Y-%m-%d %H:%M:%S')
    
    if random.random() < FAILURE_RATE:
        diameter = NOMINAL_DIAMETER + random.choice([-1, 1]) * (TOLERANCE + random.random() * 0.1)
    else:
        diameter = NOMINAL_DIAMETER + random.uniform(-TOLERANCE, TOLERANCE)
        
    data.append([time_stamp, bolt_id, round(diameter, 4)])

# --- Writing to CSV file ---
with open('quality_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print(f"Success! {TOTAL_BOLTS} data points created in 'quality_data.csv'")