#  DealQuest — Game Deals Scraper

**Discover game deals. Compare prices. Find your next favorite game.**

DealQuest is a web-based game deals dashboard built with Python, Flask, SQLite, HTML, CSS, and JavaScript. It fetches game deal information from the CheapShark API and presents it through an interactive, responsive dashboard.

The project combines web scraping-style data retrieval, REST API integration, database management, and frontend development in one application.

##  Features

* **Live Deal Fetching:** Retrieve game deals from the CheapShark API.
* **SQLite Database:** Store game deals locally and update existing records.
* **Interactive Dashboard:** View game prices and discounts in a clean interface.
* **Search:** Find games by title.
* **Discount Filtering:** Filter deals according to their discount.
* **Sorting:** Sort games by discount, sale price, or title.
* **Dashboard Statistics:** View deal counts, average discounts, lowest sale prices, and potential savings.
* **Refresh Functionality:** Request updated deal information without manually reloading the page.
* **Responsive Design:** Use the dashboard on desktop and smaller screens.
* **Error Handling:** Handle API request failures and unsuccessful database operations.

##  Tech Stack

| Technology       | Purpose                                                        |
| ---------------- | -------------------------------------------------------------- |
| Python           | Application logic and data processing                          |
| Flask            | Web server and backend routes                                  |
| Requests         | HTTP requests to the CheapShark API                            |
| Beautiful Soup 4 | HTML parsing practice and web data extraction                  |
| SQLite           | Local database storage                                         |
| HTML5            | Dashboard structure                                            |
| CSS3             | Styling and responsive layout                                  |
| JavaScript       | Search, filters, sorting, pagination, and refresh interactions |
| Git & GitHub     | Version control and project hosting                            |

##  How It Works

1. The Python scraper sends a request to the CheapShark API.
2. The API returns game deal information in JSON format.
3. The application stores and updates deal records in SQLite.
4. Flask serves the dashboard and exposes an endpoint for refreshing deals.
5. JavaScript communicates with the backend and updates the dashboard.
6. Users can search, filter, sort, and explore the displayed deals.

## Project Structure

text
game-deals-scraper/
│
├── app.py                  # Flask application and routes
├── scraper.py              # Fetch game deals from the API
├── database.py             # SQLite database operations
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Files excluded from Git
│
├── templates/
│   └── index.html          # Dashboard HTML template
│
├── static/
│   ├── css/
│   │   └── style.css       # Dashboard styling
│   │
│   └── js/
│       └── script.js       # Interactive dashboard logic
│
├── tests/                  # Test files
└── data/                   # Project data, if required
```

*The structure above describes the main application files. Additional helper scripts may also exist in the repository.*

##  Installation and Setup

### Prerequisites

Install the following before starting:

* Python 3.10 or newer
* Git
* Visual Studio Code (recommended)

### 1. Clone the repository

```bash
git clone https://github.com/Tanmaykamble2416/game-deals-scraper.git
```



### 2. Navigate to the project directory

```bash
cd game-deals-scraper
```

### 3. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

bash
python app.py


Open the local address displayed in the terminal, usually:

text
http://127.0.0.1:5000


The application creates its SQLite database when its database initialization function runs. Deal information can then be fetched and saved through the application.

##  Screenshots

Add screenshots of the working application here.

### Dashboard

<!-- Save a screenshot in screenshots/dashboard.png and uncomment the next line. -->

<!-- ![DealQuest Dashboard](screenshots/dashboard.png) -->

### Search, Filters, and Sorting

<!-- Save another screenshot in screenshots/filters.png and uncomment the next line. -->

<!-- ![DealQuest Search and Filters](screenshots/filters.png) -->

##  What I Learned

Building DealQuest provided practical experience with:

* Making HTTP requests and consuming a public REST API.
* Working with JSON responses.
* Building a backend application using Flask.
* Designing database tables and implementing SQLite CRUD operations.
* Connecting frontend interactions to backend endpoints.
* Using JavaScript to update page content dynamically.
* Handling request failures and database errors.
* Organizing a Python web application into separate modules.
* Managing project versions with Git and GitHub.

##  Future Improvements

Potential improvements include:

* Pagination through additional API results.
* Price history and deal tracking.
* Filters by game store and discount percentage.
* Price-drop notifications.
* Automated tests for database operations and API handling.
* Deployment so users can access the dashboard online.

##  Data Source

Game deal information is retrieved from the [CheapShark API](https://www.cheapshark.com/).

DealQuest is an independent learning project and is not affiliated with CheapShark.

##  Author

**YOUR NAME**

* GitHub: [@tanmaykamble2416](https://github.com/YOUR_USERNAME)

##  License

This project is available under the MIT License if a corresponding `LICENSE` file is added to the repository.
