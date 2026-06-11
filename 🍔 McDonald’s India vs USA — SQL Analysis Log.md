🍔 McDonald’s India vs USA — SQL Analysis Log



This document contains the key SQL queries used to explore menu structure, nutrition patterns, and health indicators across McDonald’s India and USA datasets.



1\. Menu Structure Overview

📊 What categories exist and how big are they?

SELECT

&#x20;   menu,

&#x20;   COUNT(\*) AS item\_count

FROM mcd\_india

GROUP BY menu

ORDER BY item\_count DESC;



Purpose:

Understand how the Indian menu is distributed across categories like breakfast, regular, gourmet, etc.



2\. Calorie Extremes (India)

🔥 Which items are the highest in calories?

SELECT

&#x20;   item,

&#x20;   menu,

&#x20;   calories

FROM mcd\_india

ORDER BY calories DESC

LIMIT 10;



Purpose:

Identify extreme high-calorie items and potential nutritional outliers.



3\. Average Calories by Category

📦 Which menu groups are most calorie-heavy?

SELECT

&#x20;   menu,

&#x20;   ROUND(AVG(calories),2) AS avg\_calories

FROM mcd\_india

GROUP BY menu

ORDER BY avg\_calories DESC;



Purpose:

Compare energy density across menu categories.



4\. Sugar Hotspots (India)

🍭 Where is sugar concentrated?

SELECT

&#x20;   item,

&#x20;   menu,

&#x20;   sugar

FROM mcd\_india

ORDER BY sugar DESC

LIMIT 10;



Purpose:

Spot sugary items driving health risk (mostly beverages/desserts).



5\. Average Sugar by Category

SELECT

&#x20;   menu,

&#x20;   ROUND(AVG(sugar),2) AS avg\_sugar

FROM mcd\_india

GROUP BY menu

ORDER BY avg\_sugar DESC;



Purpose:

See which categories are consistently sugar-heavy.



6\. Sodium Extremes

🧂 Highest sodium items in the menu

SELECT

&#x20;   item,

&#x20;   menu,

&#x20;   sodium

FROM mcd\_india

ORDER BY sodium DESC

LIMIT 10;



Purpose:

Identify salt-heavy items contributing to cardiovascular risk.



7\. Protein Leaders

💪 Which items give the most protein?

SELECT

&#x20;   item,

&#x20;   menu,

&#x20;   protein

FROM mcd\_india

ORDER BY protein DESC

LIMIT 10;



Purpose:

Highlight high-protein menu options.



8\. Protein Efficiency

⚖️ Protein per calorie efficiency

SELECT

&#x20;   item,

&#x20;   menu,

&#x20;   ROUND(protein/calories \* 100,2) AS protein\_per\_100\_calories

FROM mcd\_india

WHERE calories > 0

ORDER BY protein\_per\_100\_calories DESC;



Purpose:

Find “lean protein” items that give more nutrition per calorie.



9\. Custom Health Score (India)

🧪 Composite nutritional risk metric

SELECT

&#x20;   item,

&#x20;   menu,

&#x20;   ROUND(

&#x20;       (protein \* 2)

&#x20;       - (sugar)

&#x20;       - (satfat \* 2),

&#x20;   2) AS health\_score

FROM mcd\_india

ORDER BY health\_score DESC;



Purpose:

Create a simple scoring model balancing protein vs sugar and saturated fat.



10\. Veg vs Non-Veg Split (India)

🌱🍗 Macro differences by food type

SELECT

&#x20;   CASE

&#x20;       WHEN item LIKE '%Chicken%' THEN 'Non-Veg'

&#x20;       WHEN item LIKE '%Fish%' THEN 'Non-Veg'

&#x20;       WHEN item LIKE '%Egg%' THEN 'Non-Veg'

&#x20;       WHEN item LIKE '%Sausage%' THEN 'Non-Veg'

&#x20;       WHEN item LIKE '%McNuggets%' THEN 'Non-Veg'

&#x20;       WHEN item LIKE '%Strips%' THEN 'Non-Veg'

&#x20;       ELSE 'Veg'

&#x20;   END AS food\_type,



&#x20;   ROUND(AVG(calories),2) AS avg\_calories

FROM mcd\_india

GROUP BY food\_type;



Purpose:

Compare nutritional profiles between veg and non-veg items.



11\. Veg vs Non-Veg Full Nutrition Profile

SELECT

&#x20;   CASE

&#x20;       WHEN item LIKE '%Chicken%' THEN 'Non-Veg'

&#x20;       WHEN item LIKE '%Fish%' THEN 'Non-Veg'

&#x20;       WHEN item LIKE '%Egg%' THEN 'Non-Veg'

&#x20;       WHEN item LIKE '%Sausage%' THEN 'Non-Veg'

&#x20;       WHEN item LIKE '%McNuggets%' THEN 'Non-Veg'

&#x20;       WHEN item LIKE '%Strips%' THEN 'Non-Veg'

&#x20;       ELSE 'Veg'

&#x20;   END AS food\_type,



&#x20;   COUNT(\*) AS items,

&#x20;   ROUND(AVG(calories),2) AS avg\_calories,

&#x20;   ROUND(AVG(protein),2) AS avg\_protein,

&#x20;   ROUND(AVG(sugar),2) AS avg\_sugar,

&#x20;   ROUND(AVG(sodium),2) AS avg\_sodium

FROM mcd\_india

GROUP BY food\_type;



Purpose:

Full macro comparison of veg vs non-veg categories.



12\. Veg Items Only (Calorie Extremes)

SELECT

&#x20;   item,

&#x20;   calories

FROM mcd\_india

WHERE item NOT LIKE '%Chicken%'

AND item NOT LIKE '%Fish%'

AND item NOT LIKE '%Egg%'

AND item NOT LIKE '%Sausage%'

AND item NOT LIKE '%McNuggets%'

AND item NOT LIKE '%Strips%'

ORDER BY calories DESC

LIMIT 10;



Purpose:

Check whether “veg” actually means lower calorie or not.



13\. Non-Veg Heavy Items

SELECT

&#x20;   item,

&#x20;   calories

FROM mcd\_india

WHERE

&#x20;   item LIKE '%Chicken%'

&#x20;   OR item LIKE '%Fish%'

&#x20;   OR item LIKE '%Egg%'

&#x20;   OR item LIKE '%Sausage%'

&#x20;   OR item LIKE '%McNuggets%'

&#x20;   OR item LIKE '%Strips%'

ORDER BY calories DESC

LIMIT 10;



Purpose:

Identify calorie-heavy protein-based items.



14\. USA Category Overview

SELECT

&#x20;   Category,

&#x20;   COUNT(\*) AS item\_count

FROM us\_menu

GROUP BY Category

ORDER BY item\_count DESC;



Purpose:

Understand structure of USA menu categories.



15\. USA Nutrition by Category

SELECT

&#x20;   Category,

&#x20;   ROUND(AVG(Calories),2) AS avg\_calories,

&#x20;   ROUND(AVG(Protein),2) AS avg\_protein,

&#x20;   ROUND(AVG(Sugars),2) AS avg\_sugar,

&#x20;   ROUND(AVG(Sodium),2) AS avg\_sodium

FROM us\_menu

GROUP BY Category

ORDER BY avg\_calories DESC;



Purpose:

Compare nutrition intensity across US categories.



16\. Sugar Extremes (USA)

SELECT

&#x20;   Item,

&#x20;   Category,

&#x20;   Sugars

FROM us\_menu

ORDER BY Sugars DESC

LIMIT 10;



Purpose:

Find highest sugar items (mostly drinks/desserts).



17\. Fries Analysis (Example Slice)

SELECT item, calories, sodium 

FROM us\_menu

WHERE item LIKE '%fries%';



Purpose:

Isolate fries for cross-country comparison.



18\. USA Health Score Model

SELECT

&#x20;   Item,

&#x20;   Category,

&#x20;   (

&#x20;       Protein\*2 

&#x20;       - Sugars 

&#x20;       - Sodium\*0.001 

&#x20;       - "Saturated Fat"\*2 

&#x20;       - "Trans Fat"\*5

&#x20;   ) AS health\_score

FROM us\_menu

ORDER BY health\_score ASC

LIMIT 10;



Purpose:

Rank worst nutritional items in US menu.



19\. Protein Efficiency (USA)

SELECT

&#x20;   Item,

&#x20;   Category,

&#x20;   Protein,

&#x20;   Calories,

&#x20;   (Protein \* 1.0 / Calories) AS protein\_efficiency

FROM us\_menu

ORDER BY protein\_efficiency DESC

LIMIT 10;



Purpose:

Find best protein-to-calorie items.

