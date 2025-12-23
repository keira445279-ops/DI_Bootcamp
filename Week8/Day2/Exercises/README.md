# Data Analytics Bootcamp: Excel & Pivot Tables Solutions

This repository contains completed exercises focusing on logical functions, data analysis with Pivot Tables, and interactive visualization using Slicers.

## Exercise 1: Beetle Length Analysis (SingleIFBeetleLength.xlsx)
* **Column C (Length Status):** Implemented `=IF(B4 > $B$21; "LONG"; "SHORT")` to categorize beetles based on the average length in B21.
* **Column D (Extra Comment):** Created a nested logic with rounding: `=IF(B4 > $B$21; "This sample is " & ROUND(B4 - $B$21; 2) & " longer than average"; "")`.
* **Testing:** Verified that changing B4 to `50.2` updates the average and all dependent categories correctly, and confirmed functionality with B4 at `20.7`.

## Exercise 2: Holiday Statistics (ListOfHolidays.xlsx)
* **Pivot Table Setup:** Analyzed holiday data to find price trends.
* **Filters Applied:**
    * `Travel Method` filtered for **Plane**.
    * `Resort Name` filtered using Label Filters for names **Beginning with 'S'**.
* **Aggregation:** Values set to `Average of Price`.
* **Drill-down Verification:** Double-clicked the Grand Total to generate a detail sheet, confirming exactly **3 holidays** meet the criteria.

## Exercise 3: Oscar Nominations Chart (Movies.xlsx)
* **Pivot Chart:** Generated a chart showing the relationship between film certificates and Oscar success.
* **Metric:** Calculated the `Average of Oscar Nominations`.
* **Interactivity:** Integrated a **Slicer** for `Genre` to allow dynamic filtering of the average nominations by certificate for any specific genre selected.

## Exercise 4: House Search Analysis (FilmingOver.xlsx)
* **Calculated Field:** Added `Total Rooms` using the formula: `='Bedrooms' + 'Bathrooms' + 'Reception Rooms'`.
* **Data Grouping:**
    * **Urban Group:** Combined "Town" and "Village".
    * **Non-Urban Group:** Combined "Countryside" and "Remote".
* **Advanced Analysis:** Configured `Garden Size` in columns and set values to display as **% of Row Total** to analyze property distribution by location type.

## Exercise 5: Advanced Slicers (FilmingOver.xlsx)
* **Slicer Implementation:** Replaced standard country filters with a dynamic **Slicer**.
* **Multi-Table Connection:** * Created a second Pivot Table for `Average Oscar Wins` by `Certificate`.
    * Used **Report Connections** to link the original Country Slicer to both Pivot Tables.
* **Data View:** Filtered for **Australasian films** (Australia and New Zealand) to show synchronized statistics across both analysis sheets.

## Technical Skills Demonstrated
* **Logic:** Logical tests (IF), Absolute references ($), String concatenation (&).
* **Pivot Tables:** Aggregations (Average/Sum), Grouping, Calculated Fields.
* **Visualization:** Pivot Charts, Slicers, Report Connections.
* **Data Integrity:** Statistical verification via Drill-down.