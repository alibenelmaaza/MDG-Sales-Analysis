
try 
    Date.FromText(Text.Trim([Date]), [Format = "d/M/yyyy", Culture = "fr-FR"]) 
otherwise 
    try 
        Date.FromText(Text.Trim([Date]), [Culture = "en-US"]) 
    otherwise 
        null
