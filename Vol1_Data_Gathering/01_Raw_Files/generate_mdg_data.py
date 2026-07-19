import os
import pandas as pd
import numpy as np

# 1. Create the local data directory
folder_name = "MDG_Sales_Data"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Define date range for July 2026 (31 days) and product list
dates = pd.date_range(start="2026-07-01", end="2026-07-31").strftime("%d/%m/%Y").tolist()
products = ["Sunsilk Expert", "Dove Nutritive", "Omo Active", "Domestos Ultra"]

# ==========================================
# FILE 1: Marjane California (CA)
# Embedded Issues: Trailing spaces, Case-sensitivity, Null values, Negative revenues
# ==========================================
data_ca = []
for dt in dates:
    for prod in products:
        # Issue 1: Random trailing spaces added to product names
        prod_name = prod + "   " if np.random.rand() > 0.7 else prod
        
        # Issue 2: Random lower-casing for Omo Active
        if "Omo" in prod and np.random.rand() > 0.5:
            prod_name = "omo active"
            
        units = np.random.randint(80, 250)
        
        # Issue 3: Random null/missing values in Units_Sold (approx. 8% of rows)
        units_val = np.nan if np.random.rand() > 0.92 else units
        
        # Calculate revenue, handle null values gracefully
        revenue = units * 30 if not np.isnan(units_val) else 4500
        
        # Issue 4: Outliers / Negative values in Revenue (approx. 5% of rows)
        if np.random.rand() > 0.95:
            revenue = -revenue
            
        target = np.random.randint(3000, 8000)
        data_ca.append([dt, prod_name, units_val, revenue, target])

df_ca = pd.DataFrame(data_ca, columns=["Date", "Product", "Units_Sold", "Revenue", "Target"])
df_ca.to_excel(os.path.join(folder_name, "Sales_Marjane_California.xlsx"), index=False)


# ==========================================
# FILE 2: Carrefour Tamaris (TA)
# Embedded Issues: Date formatting inconsistencies, Currencies appended as text
# ==========================================
data_ta = []
for dt in dates:
    # Issue 1: Inconsistent date formats (switching between DD/MM/YYYY and US Text format)
    dt_val = pd.to_datetime(dt, format="%d/%m/%Y").strftime("%B %d, %Y") if np.random.rand() > 0.7 else dt
    for prod in products:
        units = np.random.randint(70, 200)
        
        # Issue 2: Numbers dirty text format by appending " DH" currency label
        revenue = f"{units * 30} DH" 
        
        target = np.random.randint(2500, 6000)
        data_ta.append([dt_val, prod, units, revenue, target])

df_ta = pd.DataFrame(data_ta, columns=["Date", "Product", "Units_Sold", "Revenue", "Target"])
df_ta.to_excel(os.path.join(folder_name, "Sales_Carrefour_Tamaris.xlsx"), index=False)


# ==========================================
# FILE 3: LabelVie Anfa (AN)
# Embedded Issues: Duplicate rows, High data density
# ==========================================
data_an = []
for dt in dates:
    for prod in products:
        units = np.random.randint(90, 280)
        revenue = units * 30
        target = np.random.randint(3500, 9000)
        data_an.append([dt, prod, units, revenue, target])
        
        # Issue 1: Fully duplicated rows to simulate system sync errors (approx. 15% rate)
        if np.random.rand() > 0.85:
            data_an.append([dt, prod, units, revenue, target])

df_an = pd.DataFrame(data_an, columns=["Date", "Product", "Units_Sold", "Revenue", "Target"])
df_an.to_excel(os.path.join(folder_name, "Sales_LabelVie_Anfa.xlsx"), index=False)

print("\n" + "="*80)
print("🚀 SUCCESS: MDG Sales Dataset Generated Locally!")
print("📁 Target Directory: './MDG_Sales_Data'")
print("📊 Volume: 3 Files (~124 rows each, ~370+ total rows) with clean ETL challenges.")
print("="*80 + "\n")