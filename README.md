# Music Listening Database Application Contribution

Academic team assignment completed for CIS 3120 Programming for Analytics at Baruch College in Spring 2026.

## Overview

This repository contains the SQL query module I contributed to a three person Python and SQLite database application for artists, tracks, playlists, and playlist track relationships.

My assigned work focused on the query module rather than the entire application.

## Code

[`queries.py`](queries.py) contains the four SQL query functions from my contribution plus the standalone SQLite smoke test I used to verify them.

The functions handle:

* Tracks in a playlist in the correct order
* Tracks that are not included in any playlist
* The most frequently added track across playlists
* Total duration for each playlist

The queries use JOIN, LEFT JOIN, GROUP BY, COUNT, aggregate functions, ordering, and parameterized SQL.

## Original Contribution

My original pull request to the course repository is available here:

https://github.com/ProfessorPatrickSlatraigh/mp02-music-starter/pull/29

## Tools and Skills

Python, SQL, SQLite, relational databases, Git and GitHub

## Team Context

This was completed by a three person team. This repository contains the portion I personally contributed and does not present the complete team application as my individual work.

## How to Run

Requires Python 3 (standard library only, no packages to install). Run the standalone smoke test, which builds a sample in-memory SQLite database and prints the output of each query function:

```
python queries.py
```
