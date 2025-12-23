# Dinosaur Database Filtering Project

This project involves data manipulation and filtering of a dinosaur dataset using Google Sheets/Excel.

## Part 1: Cretaceous Dinosaurs Filtering
**Goal:** Identify specific dinosaurs based on multiple biological and chronological criteria.
* **Filter 1 (Period):** `Cretaceous`
* **Filter 2 (Diet):** `NOT Carnivore` (Excluded all meat-eaters)
* **Filter 3 (Height):** `< 2.0` meters
* **Filter 4 (Weight):** Between `10` and `100` kg
* **Result:** Successfully filtered down to **4 dinosaurs**.

## Part 2: Jurassic Beasts Analysis (Top 50% by Length)
**Goal:** Extract the longest 50% of dinosaurs from the Jurassic period.
* **Initial Filter:** `Period` = `Jurassic` (Resulted in 7 dinosaurs).
* **Statistical Calculation:** Used `=MEDIAN(Length_Range)` to determine the 50th percentile threshold.
* **Percentile Filter:** Applied a "Greater than or equal to" filter on the `Length` column using the calculated median value.
* **Result:** Successfully identified the **top 4 dinosaurs**.

## Part 3: Text Pattern Matching (Bird-hipped & Tooth)
**Goal:** Find specific anatomical classifications with text-based name meanings.
* **Filter 1 (Hip Type):** `bird-hipped`
* **Filter 2 (Meaning of Name):** Applied "Text contains" filter for the string `tooth`.
* **Result:** Successfully narrowed down the dataset to **2 dinosaurs**.

## Technical Details
* **Tools used:** MS Excel.
* **Data Format:** Calculations performed in `.xlsx` format.
* **Methodology:** Manual filtering via headers and statistical functions (MEDIAN) for percentile analysis.