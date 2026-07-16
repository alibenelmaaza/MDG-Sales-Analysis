## Vol 1 - Extension: Actionable Sales Dashboard Architecture

This folder documents the modular architecture and visual intelligence layer of our Modern Trade sales analytics platform. To maintain a professional, enterprise-grade standard, we structured this phase into separate logical layers, separating our raw clean database from the analytical engine and the final reporting interface.

---

## 📂 Repository Directory Structure

*   📁 **[01_Main_Data_Table](./01_Main_Data_Table)**: Houses the documentation and configuration for our structured, clean source database (`CleanSalesData`) featuring our custom KPI columns.
*   📁 **[02_Pivot_Tables](./02_Pivot_Tables)**: Contains the backend analytical engine (`Dashboard_Backend`) where data is summarized by product lines and retail accounts.
*   📁 **[03_Dashboard_Charts](./03_Dashboard_Charts)**: Represents the high-fidelity presentation layer (`Dashboard`) containing the interactive UI.
*   📁 **[04_Complete_Workbook](.MDG_Sales_Analytics_Dashboard(versionVolume1-Extension))**: Hosts the final completed, interactive `.xlsx` workbook featuring all the layers integrated.

---

## 🛠️ Step-by-Step Architectural Implementation

### Layer 1: The Main Data Table (`CleanSalesData`)
We enhanced our programmatic ETL output by inserting two critical commercial metrics directly into the database:
1.  **Achievement Rate %:** Measures target compliance:
    `=[@[Corrected Revenue]]/[@Target]`
2.  **Average Selling Price (ASP):** Prevents division-by-zero errors when units sold are null:
    `=IF([@[Units_Sold]]=0, 0, [@[Corrected Revenue]]/[@[Units_Sold]])`

### Layer 2: The Pivot Tables Backend
To feed our visual charts without cluttering the user interface, we isolated two primary Pivot Tables inside `Dashboard_Backend`:
*   **Product Performance Pivot:** Summarizes targets, corrected revenues, and average achievement rates per product.
*   **Account Contribution Pivot:** Tracks total revenue distribution and volume velocity across Morocco's key retail chains (Modern Trade n1, Modern Trade n2, Modern Trade n3).

### Layer 3: The Dashboard Charts (The Visual UI)
We converted the backend pivot tables into an executive-ready visual experience:
1.  **Clustered Column-Line Combo Chart:** Plots total revenue against target on the primary axis, with the `Average Achievement Rate` mapped beautifully across a **Secondary Axis** line to prevent scale flattening.
2.  **Account Contribution Donut Chart:** A clean, modern visual demonstrating that **Modern Trade n3** dominates sales with **42%** contribution, followed by **Modern Trade n2** at **31%**, and **Modern Trade n1** at **27%**.

---

## 🎛️ Interactive Cross-Filtering (Slicers)

To deliver a native app-like experience, we integrated two advanced **Slicers**:
*   **Product Slicer:** Instantly drills down to isolate performance for `OMO ACTIVE`, `DOMESTOS ULTRA`, `DOVE NUTRITIVE`, or `SUNSILK EXPERT`.
*   **Revenue Bilan Slicer:** Dynamically splits data based on daily target compliance (`Good Profit` vs `Low Profit`).

### 🔗 Slicer Synchronization (Report Connections)
By creating both pivot tables from the exact same data source (`CleanSalesData`), we unlocked the ability to link them. We configured **Report Connections** so that clicking any button instantly triggers a synchronous update across the column heights, the secondary line, and the donut percentages simultaneously.
