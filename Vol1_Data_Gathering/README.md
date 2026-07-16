
### MDG Modern Trade Sales Analytics Platform > **Enterprise-Grade FMCG Sales Engineering & Business Intelligence Suite
** This repository showcases an end-to-end modern data analytics platform designed to ingest, clean, consolidate, and visualize complex Modern Trade sales transactions (simulating FMCG distribution networks for giants).

The project is structured into modular developmental phases to solve real-world data quality and business integration challenges.

---

  ## 🗺️ Table of Contents (Project Roadmap)

### 🧹 [Vol 1: Data Gathering & Automation (The Foundation)](./Vol1_Data_Gathering) Focuses on establishing a robust data infrastructure and an automated, self-healing ETL pipeline in Excel Power Query.
* 📂 **Step 1: Raw Data Ingestion** -> [Browse Raw Files](./Vol1_Data_Gathering/01_Raw_Files)
* 💻 **Step 2: Custom ETL Formula Script** -> [View Power Query M-Code](./Vol1_Data_Gathering/02_Power_Query_M_Code)
* 📊 **Step 3: Cleaned Unified Database** -> [Access Clean Data Model](./Vol1_Data_Gathering/03_Clean_Data_Model)
 
 ##  Vol 1 Resume: Ingestion & ETL Pipeline Detail
 ```text
Raw Daily Files (Data Lake) ├── sales_moderntrade_n1.xlsx
       ├── sales_moderntrade_n2.xlsx
          └── sales_moderntrade_n3.xlsx
               │ ▼ [Automated Power Query Ingestion Engine] Cleaned & Consolidated Table (Gold Standard).
````





# Vol 1: Data Gathering & Automation (The Data Engineering Backend)

This folder contains the core data engineering backend of our Modern Trade sales analytics platform. The primary objective of this phase is to establish a robust, automated, and self-healing ETL (Extract, Transform, Load) pipeline that ingests messy and inconsistent daily transactional logs directly from retail terminals and programmatically cleanses them into a "single source of truth."



---

## 📂 Inside This Folder

*   📁 **[01_Raw_Files](./01_Raw_Files)**: Represents our local data lake, holding the raw daily spreadsheets from Marjane, Carrefour, and LabelVie.
*   📁 **[02_Power_Query_M_Code](./02_Power_Query_M_Code)**: Holds the custom-built programmatic formulas and fallback parsing scripts.
*   📁 **[03_Clean_Data_Model](./03_Clean_Data_Model)**: Hosts the final standardized and consolidated database, ready for Business Intelligence applications.

---

## 🛠️ Step-by-Step ETL Execution Pipeline

### Step 1: Automated Ingestion & Direct Directory Monitoring
To eliminate repetitive manual work, we configured the Power Query Ingestion Engine to monitor our local folder, filter strictly for Excel formats, and dynamically merge all transactional tables:

* **Traceability:** This maintains full trace of which retail branch generated each row through the `Source.Name` column.

---

### Step 2: Casing Standardization & Space Sanitization

Field promoters often enter data with varying text capitalization and trailing whitespaces. We applied a sequence of string transformations to prevent split records:

* **Trim:** Removes redundant leading/trailing white spaces (e.g., `"OMO ACTIVE   "` becomes `"OMO ACTIVE"`).
* **Uppercase:** Normalizes all product nomenclature to guarantee exact groupings.

```powerquery
Trimmed_Product = Table.TransformColumns(Previous_Step, {{"Product", Text.Trim, type text}}),
Upper_Product = Table.TransformColumns(Trimmed_Product, {{"Product", Text.Upper, type text}})

```

---

### Step 3: Resolving Hybrid Date Formats (Custom M-Code Fallback Engine)

Because data originated from systems utilizing mixed French/Moroccan (`DD/MM/YYYY`) and US English (`Month DD, YYYY`) regional settings, standard date conversion failed on over 50% of the entries.

We bypassed UI limitations and wrote a custom fallback script that attempts local parsing first, and dynamically falls back to the US English locale on failure:

```powerquery
try 
    Date.FromText(Text.Trim([Date]), [Format = "d/M/yyyy", Culture = "fr-FR"]) 
otherwise 
    try 
        Date.FromText(Text.Trim([Date]), [Culture = "en-US"]) 
    otherwise 
        null

```

---

### Step 4: Logic Consistency Checks & Revenue Reconstruction

We detected a critical system conflict where daily branch transactions registered `0` in `Units_Sold`, but reflected positive or negative revenue values. Removing these rows would break our transaction audit trail.

We applied custom business logic to enforce structural data consistency:

1. If `Units_Sold` is 0, the revenue is strictly set to `0`.
2. If the revenue is negative while units are sold, it calculates positive revenue based on default product unit pricing.
3. Otherwise, it retains the verified raw revenue.

```powerquery
each if [Units_Sold] = 0 then 0 
else if [Revenue] < 0 then [Units_Sold] *30
else if [Revenue] < 0 and [Revenue] = 0 then 0
else [Revenue] 

```

---

## 🎯 Final Outcome

With this automated backend, we transformed a heavily corrupted data stream into a **standardized, audit-ready dataset** that updates dynamically whenever a new file is added. This forms the perfect foundation for our upcoming visual dashboard!
