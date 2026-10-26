document.addEventListener("DOMContentLoaded", () => {


// =========================================
// 1. GET HTML ELEMENTS
// =========================================

const searchInput = document.getElementById("searchInput");
const discountFilter = document.getElementById("discountFilter");
const sortSelect = document.getElementById("sortSelect");
const refreshButton = document.getElementById("refreshButton");

const tableBody = document.getElementById("dealsTableBody");
const resultsCount = document.getElementById("resultsCount");
const noResults = document.getElementById("noResults");

const previousPageButton = document.getElementById("previousPage");
const nextPageButton = document.getElementById("nextPage");

const paginationInfo = document.getElementById("paginationInfo");
const pageNumber = document.getElementById("pageNumber");

const totalDealsElement = document.getElementById("totalDeals");
const averageDiscountElement = document.getElementById("averageDiscount");
const lowestPriceElement = document.getElementById("lowestPrice");
const potentialSavingsElement = document.getElementById("potentialSavings");

// Get all existing game rows from the HTML.
let rows = Array.from(
    document.querySelectorAll(".deal-row")
);

// Number of games displayed per page.
const pageSize = 10;

let currentPage = 1;
let filteredRows = [...rows];


// =========================================
// 2. SEARCH, FILTER AND SORT
// =========================================

function updateDashboard() {

    const searchTerm = searchInput.value.trim().toLowerCase();
    const minimumDiscount = Number(discountFilter.value);

    // Filter games by title and minimum discount.
    filteredRows = rows.filter(row => {

        const title = row.dataset.title || "";
        const discount = Number(row.dataset.discount);

        return title.includes(searchTerm)
            && discount >= minimumDiscount;
    });


    // Sort the filtered games.
    const sortValue = sortSelect.value;

    filteredRows.sort((a, b) => {

        if (sortValue === "price-asc") {
            return Number(a.dataset.price)
                - Number(b.dataset.price);
        }

        if (sortValue === "price-desc") {
            return Number(b.dataset.price)
                - Number(a.dataset.price);
        }

        if (sortValue === "title-asc") {
            return (a.dataset.title || "").localeCompare(
                b.dataset.title || ""
            );
        }

        if (sortValue === "title-desc") {
            return (b.dataset.title || "").localeCompare(
                a.dataset.title || ""
            );
        }

        // Default: highest discount first.
        return Number(b.dataset.discount)
            - Number(a.dataset.discount);
    });

    // Return to page one after changing filters.
    currentPage = 1;

    renderRows();
}


// =========================================
// 3. RENDER THE CURRENT PAGE
// =========================================

function renderRows() {

    // Hide every row before displaying the current page.
    rows.forEach(row => {
        row.hidden = true;
    });

    // Calculate the total number of pages.
    const totalPages = Math.max(
        1,
        Math.ceil(filteredRows.length / pageSize)
    );

    currentPage = Math.min(currentPage, totalPages);

    // Calculate which rows belong on this page.
    const startIndex = (currentPage - 1) * pageSize;
    const endIndex = startIndex + pageSize;

    const visibleRows = filteredRows.slice(
        startIndex,
        endIndex
    );

    // Display rows in the correct sorted order.
    visibleRows.forEach(row => {
        row.hidden = false;
        tableBody.appendChild(row);
    });

    // Show or hide the empty search result message.
    noResults.hidden = filteredRows.length !== 0;

    // Update the result count.
    resultsCount.textContent =
        `${filteredRows.length} deal${filteredRows.length === 1 ? "" : "s"}`;

    // Update pagination text.
    if (filteredRows.length === 0) {

        paginationInfo.textContent = "No deals to display";

    } else {

        paginationInfo.textContent =
            `Showing ${startIndex + 1}–${Math.min(endIndex, filteredRows.length)} of ${filteredRows.length} deals`;
    }

    pageNumber.textContent =
        `Page ${currentPage} of ${totalPages}`;

    // Enable or disable pagination buttons.
    previousPageButton.disabled = currentPage === 1;

    nextPageButton.disabled =
        currentPage === totalPages
        || filteredRows.length === 0;
}


// =========================================
// 4. SEARCH AND FILTER EVENT LISTENERS
// =========================================

searchInput.addEventListener("input", updateDashboard);

discountFilter.addEventListener("change", updateDashboard);

sortSelect.addEventListener("change", updateDashboard);


// =========================================
// 5. PREVIOUS PAGE
// =========================================

previousPageButton.addEventListener("click", () => {

    if (currentPage > 1) {

        currentPage--;

        renderRows();
    }
});


// =========================================
// 6. NEXT PAGE
// =========================================

nextPageButton.addEventListener("click", () => {

    const totalPages = Math.max(
        1,
        Math.ceil(filteredRows.length / pageSize)
    );

    if (currentPage < totalPages) {

        currentPage++;

        renderRows();
    }
});


// =========================================
// 7. KEYBOARD SHORTCUT
// =========================================

document.addEventListener("keydown", event => {

    const activeTag = document.activeElement.tagName;

    // Press "/" to focus the search box.
    if (
        event.key === "/"
        && !["INPUT", "TEXTAREA", "SELECT"].includes(activeTag)
    ) {

        event.preventDefault();

        searchInput.focus();
    }
});


// =========================================
// 8. UPDATE DASHBOARD STATISTICS
// =========================================

function updateStatistics(deals) {

    totalDealsElement.textContent = deals.length;

    const averageDiscount = deals.length
        ? deals.reduce(
            (total, deal) => total + Number(deal.savings || 0),
            0
        ) / deals.length
        : 0;

    averageDiscountElement.textContent =
        `${Math.round(averageDiscount)}%`;


    const lowestPrice = deals.length
        ? Math.min(
            ...deals.map(deal => Number(deal.sale_price))
        )
        : 0;

    lowestPriceElement.textContent =
        `$${lowestPrice.toFixed(2)}`;


    const potentialSavings = deals.reduce(
        (total, deal) => {

            const originalPrice = Number(deal.normal_price || 0);
            const salePrice = Number(deal.sale_price || 0);

            return total + originalPrice - salePrice;
        },
        0
    );

    potentialSavingsElement.textContent =
        `$${potentialSavings.toFixed(2)}`;
}


// =========================================
// 9. CREATE A GAME TABLE ROW
// =========================================

function createDealRow(deal) {

    const row = document.createElement("tr");

    row.className = "deal-row";

    const title = String(deal.title || "Unknown Game");
    const originalPrice = Number(deal.normal_price || 0);
    const salePrice = Number(deal.sale_price || 0);
    const discount = Number(deal.savings || 0);

    // Store searchable and sortable values on the row.
    row.dataset.title = title.toLowerCase();
    row.dataset.original = originalPrice;
    row.dataset.price = salePrice;
    row.dataset.discount = discount;

    row.innerHTML = `
        <td>
            <div class="game-info">
                <div class="game-icon">
                    <i class="fa-solid fa-gamepad"></i>
                </div>

                <div class="game-details">
                    <span class="game-title"></span>
                    <span class="game-subtitle">PC Game Deal</span>
                </div>
            </div>
        </td>

        <td>
            <span class="original-price"></span>
        </td>

        <td>
            <span class="sale-price"></span>
        </td>

        <td>
            <span class="discount-badge">
                <i class="fa-solid fa-arrow-down"></i>
                ${Math.round(discount)}%
            </span>
        </td>

        <td>
            <span class="saving-amount"></span>
        </td>
    `;

    // Insert the API-provided title as text, not HTML.
    row.querySelector(".game-title").textContent = title;

    row.querySelector(".original-price").textContent =
        `$${originalPrice.toFixed(2)}`;

    row.querySelector(".sale-price").textContent =
        `$${salePrice.toFixed(2)}`;

    row.querySelector(".saving-amount").textContent =
        `$${(originalPrice - salePrice).toFixed(2)}`;

    return row;
}


// =========================================
// 10. REFRESH DEALS FROM THE LIVE API
// =========================================

refreshButton.addEventListener("click", async () => {

    const originalButtonHTML = refreshButton.innerHTML;

    console.log("Refresh button clicked!");

    refreshButton.disabled = true;

    refreshButton.innerHTML = `
        <i class="fa-solid fa-spinner fa-spin"></i>
        <span>Refreshing...</span>
    `;

    try {

        // Send a POST request to Flask.
        const response = await fetch("/api/refresh", {
            method: "POST",
            headers: {
                "Accept": "application/json"
            }
        });

        // Read Flask's JSON response.
        const result = await response.json();

        // Handle unsuccessful responses.
        if (!response.ok || !result.success) {

            throw new Error(
                result.message || `Request failed: ${response.status}`
            );
        }

        if (!Array.isArray(result.deals)) {
            throw new Error("The server returned an invalid deals list.");
        }

        // Build the new rows.
        const newRows = result.deals.map(createDealRow);

        // Replace the existing table rows.
        tableBody.replaceChildren(...newRows);

        // Update our row collection.
        rows = newRows;

        // Update the dashboard statistics.
        updateStatistics(result.deals);

        // Reset and reapply search, filters and sorting.
        updateDashboard();

        console.log(
            "Deals refreshed successfully:",
            result.deals
        );

        alert(result.message || "Deals refreshed successfully!");

    } catch (error) {

        console.error("Failed to refresh deals:", error);

        alert(`Refresh failed: ${error.message}`);

    } finally {

        // Restore the button even if something fails.
        refreshButton.disabled = false;

        refreshButton.innerHTML = originalButtonHTML;
    }
});


// =========================================
// 11. INITIALIZE THE DASHBOARD
// =========================================

updateDashboard();


});
