# IPL Data Analysis Project

This project contains a set of SQL queries for analyzing the IPL (Indian Premier League) database. 

## Project Overview
The goal is to extract key performance metrics for players, including runs, centuries, and bowling figures using SQLite.

## Queries Included
* **Query 1: Player Match Data** - Overview of players in specific matches.
* **Query 2: Batsman vs Runs** - Total runs scored by each player.
* **Query 3: Fifties and Hundreds** - Count of career milestones (50s and 100s).
* **Query 4: Best Bowling Figures** - Top performance for each bowler in a single match.
* **Query 5: Comprehensive Career Metrics** - A combined view of all batting and bowling stats.

## Database Structure
The analysis is performed on a relational database with the following key tables:
* `Player`
* `Ball_by_Ball`
* `Batsman_Scored`
* `Wicket_Taken`

## How to Run
1. Open the `database.sqlite` file in **DB Browser for SQLite**.
2. Copy the queries from `solution.sql` into the **Execute SQL** tab.
3. Run the queries to see the results.