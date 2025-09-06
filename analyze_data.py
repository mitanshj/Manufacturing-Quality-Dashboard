# analyze_data.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Starting analysis...")

# --- 1. Load the Dataset ---
try:
    df = pd.read_csv('quality_data.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: 'quality_data.csv' not found. Please run 'create_data.py' first.")
    exit()

# --- 2. Apply the Quality Check Logic ---
NOMINAL_DIAMETER = 20.0
TOLERANCE = 0.05
UPPER_LIMIT = NOMINAL_DIAMETER + TOLERANCE
LOWER_LIMIT = NOMINAL_DIAMETER - TOLERANCE

def classify_bolt(diameter):
    if diameter > UPPER_LIMIT:
        return 'Rejected (Too Large)'
    elif diameter < LOWER_LIMIT:
        return 'Rejected (Too Small)'
    else:
        return 'Accepted'

df['Status'] = df['Diameter_mm'].apply(classify_bolt)
print("Quality classification complete.")

# --- 3. Analyze and Print Summary ---
status_counts = df['Status'].value_counts()
print("\n--- Quality Control Summary ---")
print(status_counts)
print("-----------------------------\n")

# --- 4. Visualize and Save the Results ---

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=['#4CAF50', '#FF5722', '#F44336'])
plt.title('Overall Quality Control Status')
plt.ylabel('')
plt.savefig('quality_pie_chart.png') # Save the chart as an image
print("Saved pie chart to 'quality_pie_chart.png'")

# Bar Chart
plt.figure(figsize=(10, 6))
sns.countplot(x='Status', data=df, order=['Accepted', 'Rejected (Too Small)', 'Rejected (Too Large)'], palette=['green', 'orange', 'red'])
plt.title('Count of Bolts by Quality Status')
plt.xlabel('Status')
plt.ylabel('Number of Bolts')
plt.savefig('quality_bar_chart.png') # Save the chart as an image
print("Saved bar chart to 'quality_bar_chart.png'")

print("\nAnalysis finished.")