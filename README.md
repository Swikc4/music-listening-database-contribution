<a id="readme-top"></a>

<br />
<div align="center">
  <h3 align="center">Music Listening Database Application Contribution</h3>
  <p align="center">
    The SQL query module I contributed to a team-built Python and SQLite music database, a CIS 3120 team assignment at Baruch College
    <br />
    <a href="https://github.com/Swikc4/music-listening-database-contribution"><strong>Explore the repo »</strong></a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
      <ul><li><a href="#built-with">Built With</a></li></ul>
    </li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#original-contribution">Original Contribution</a></li>
    <li><a href="#team-context">Team Context</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

Academic team assignment completed for CIS 3120 Programming for Analytics at Baruch College in Spring 2026.

This repository contains the SQL query module I contributed to a three person Python and SQLite database application for artists, tracks, playlists, and playlist track relationships. My assigned work focused on the query module rather than the entire application.

[`queries.py`](queries.py) contains the four SQL query functions from my contribution plus the standalone SQLite smoke test I used to verify them. The functions handle:

* Tracks in a playlist in the correct order
* Tracks that are not included in any playlist
* The most frequently added track across playlists
* Total duration for each playlist

The queries use JOIN, LEFT JOIN, GROUP BY, COUNT, aggregate functions, ordering, and parameterized SQL.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
* ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
* ![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

* Python 3 (standard library only, no packages to install)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Swikc4/music-listening-database-contribution.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

Run the standalone smoke test, which builds a sample in-memory SQLite database and prints the output of each query function:

```sh
python queries.py
```

Expected output:

```text
[('Track One', 'Sample Artist A', 210, 1), ('Track Two', 'Sample Artist A', 185, 2), ('Track Three', 'Sample Artist B', 240, 3)]
[(5, 'Orphan Track', 'Sample Artist A')]
('Track One', 'Sample Artist A', 2)
[('Morning Commute', 10.583333333333334), ('Study Session', 6.75)]
```

The four blocks are: tracks in a playlist in order, tracks not in any playlist, the most frequently added track, and total duration per playlist in minutes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Original Contribution

My original pull request to the course repository is available here:

https://github.com/ProfessorPatrickSlatraigh/mp02-music-starter/pull/29

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Team Context

This was completed by a three person team. This repository contains the portion I personally contributed and does not present the complete team application as my individual work.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

* CIS 3120 Programming for Analytics, Baruch College (Zicklin School of Business)
