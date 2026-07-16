# Advanced Power Query M-Code Scripts

This folder documents the custom programmatic M-code scripts used to bypass standard UI limitations and handle complex data preparation logic in our ETL pipeline.

---

## 📅 1. Hybrid Date Formatting Fallback Script

Because raw sales files were generated across different branch terminals with varying OS regional settings, the date column contained a hybrid mix of French/Moroccan format (`DD/MM/YYYY`) and US Text format (`Month DD, YYYY`)  Standard parsing failed and returned errors

We resolved this with a custom fallback script that tries parsing the local French/Moroccan format first, and gracefully falls back to the US English locale on failure:

```powerquery
try 
    Date.FromText(Text.Trim([Date]), [Format = "d/M/yyyy", Culture = "fr-FR"]) 
otherwise 
    try 
        Date.FromText(Text.Trim([Date]), [Culture = "en-US"]) 
    otherwise 
        null
````

---

## 💰 2. Logical Consistency Engine (Corrected Revenue) :
To prevent data corruption and preserve our total unit counts without omitting rows, we built a custom logical check. This formula evaluates the relationship between units sold and revenue, correcting system export errors where zero units were mapped to non-zero values:

```powerquery

each if [Units_Sold] = 0 then 0 
  else if [Revenue] < 0 then [Units_Sold] *30 
    else if [Revenue] < 0 and [Revenue] = 0 then 0
      else [Revenue]
````
