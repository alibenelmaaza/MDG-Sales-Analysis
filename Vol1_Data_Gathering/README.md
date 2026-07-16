# MDG Modern Trade Sales Analytics Platform
> **Vol. 1: Data Gathering & Automation (The Data Engineering Backend)**

This repository contains the first volume of an end-to-end FMCG sales operations pipeline designed to simulate distribution analytics for major retail accounts in Morocco (3 Modern Trades). 

The primary objective of **Volume 1** is to establish a robust, automated, and self-healing ETL (Extract, Transform, Load) pipeline that ingests messy and inconsistent daily transaction logs from the field and programmatically cleanses them into a "single source of truth"—eliminating repetitive manual clean-up tasks.

---

## 📂 Volume 1 Architecture: Ingestion & ETL Pipeline

```text
Raw Daily Files (Data Lake) 
   ├── sales_moderntrade_n1.xlsx (Marjane California)
   ├── sales_moderntrade_n2.xlsx (Carrefour Tamaris)
   └── sales_moderntrade_n3.xlsx (LabelVie Anfa)
            │
            ▼ [Automated Power Query Ingestion Engine]
   Cleaned & Consolidated Consolidated Table (Gold Standard)
