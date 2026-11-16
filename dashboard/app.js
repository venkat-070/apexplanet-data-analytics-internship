/**
 * app.js
 * Interactive BI Engine & Dynamic Visualization Orchestration
 * ApexPlanet Data Analytics Internship
 * Author: Venkata Vedhadri Marisetti (23981A44Y9)
 */

let masterData = null;
let charts = {};

document.addEventListener("DOMContentLoaded", async () => {
    try {
        const response = await fetch("data.json");
        masterData = await response.json();
        initializeDashboard(masterData);
    } catch (err) {
        console.error("Failed to load dashboard data:", err);
    }
});

function formatCurrency(val) {
    return "$" + Number(val).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function initializeDashboard(data) {
    // 1. Populate KPI Cards
    updateKPIs(data.kpis);

    // 2. Initialize Charts
    renderMonthlyTrendChart(data.monthly_trend);
    renderCategoryDonutChart(data.categories);
    renderRegionalBarChart(data.regions);
    renderRFMChart(data.rfm_distribution);

    // 3. Populate Transactions Table
    renderTable(data.sample_transactions);
}

function updateKPIs(kpis) {
    document.getElementById("kpi-revenue").textContent = formatCurrency(kpis.total_revenue);
    document.getElementById("kpi-profit").textContent = formatCurrency(kpis.total_profit);
    document.getElementById("kpi-margin").textContent = kpis.profit_margin_pct + "%";
    document.getElementById("kpi-aov").textContent = formatCurrency(kpis.average_order_value);
    document.getElementById("kpi-orders").textContent = kpis.total_orders.toLocaleString();
    document.getElementById("kpi-customers").textContent = kpis.total_customers.toLocaleString();
}

// Monthly Trend Chart
function renderMonthlyTrendChart(monthly) {
    const ctx = document.getElementById("monthlyTrendChart").getContext("2d");
    if (charts.monthly) charts.monthly.destroy();

    charts.monthly = new Chart(ctx, {
        type: "bar",
        data: {
            labels: monthly.labels,
            datasets: [
                {
                    label: "Monthly Gross Revenue ($)",
                    data: monthly.revenue,
                    backgroundColor: "rgba(56, 189, 248, 0.45)",
                    borderColor: "#38bdf8",
                    borderWidth: 1.5,
                    borderRadius: 4,
                    yAxisID: "y"
                },
                {
                    label: "Net Operating Profit ($)",
                    data: monthly.profit,
                    type: "line",
                    borderColor: "#10b981",
                    backgroundColor: "rgba(16, 185, 129, 0.15)",
                    borderWidth: 2.5,
                    pointRadius: 3,
                    fill: true,
                    tension: 0.3,
                    yAxisID: "y"
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { labels: { color: "#94a3b8", font: { family: "Plus Jakarta Sans" } } },
                tooltip: {
                    callbacks: {
                        label: (ctx) => `${ctx.dataset.label}: ${formatCurrency(ctx.parsed.y)}`
                    }
                }
            },
            scales: {
                x: {
                    ticks: { color: "#94a3b8", maxRotation: 45, font: { size: 10 } },
                    grid: { color: "rgba(51, 65, 85, 0.4)" }
                },
                y: {
                    ticks: {
                        color: "#94a3b8",
                        callback: (v) => "$" + (v >= 1000 ? (v / 1000).toFixed(0) + "k" : v)
                    },
                    grid: { color: "rgba(51, 65, 85, 0.4)" }
                }
            }
        }
    });
}

// Category Donut Chart
function renderCategoryDonutChart(categories) {
    const ctx = document.getElementById("categoryDonutChart").getContext("2d");
    if (charts.category) charts.category.destroy();

    charts.category = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: categories.labels,
            datasets: [{
                data: categories.revenue,
                backgroundColor: ["#38bdf8", "#f59e0b", "#10b981"],
                borderColor: "#1e293b",
                borderWidth: 3,
                hoverOffset: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: "bottom", labels: { color: "#94a3b8", font: { family: "Plus Jakarta Sans" } } },
                tooltip: {
                    callbacks: {
                        label: (ctx) => `${ctx.label}: ${formatCurrency(ctx.parsed)}`
                    }
                }
            },
            cutout: "68%"
        }
    });
}

// Regional Bar Chart
function renderRegionalBarChart(regions) {
    const ctx = document.getElementById("regionalBarChart").getContext("2d");
    if (charts.regional) charts.regional.destroy();

    charts.regional = new Chart(ctx, {
        type: "bar",
        data: {
            labels: regions.labels,
            datasets: [
                {
                    label: "Revenue ($)",
                    data: regions.revenue,
                    backgroundColor: "#38bdf8",
                    borderRadius: 4
                },
                {
                    label: "Profit ($)",
                    data: regions.profit,
                    backgroundColor: "#10b981",
                    borderRadius: 4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            indexAxis: "y",
            plugins: {
                legend: { position: "top", labels: { color: "#94a3b8" } },
                tooltip: {
                    callbacks: {
                        label: (ctx) => `${ctx.dataset.label}: ${formatCurrency(ctx.parsed.x)}`
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: "#94a3b8",
                        callback: (v) => "$" + (v >= 1000 ? (v / 1000).toFixed(0) + "k" : v)
                    },
                    grid: { color: "rgba(51, 65, 85, 0.4)" }
                },
                y: { ticks: { color: "#94a3b8" }, grid: { display: false } }
            }
        }
    });
}

// RFM Chart
function renderRFMChart(rfmData) {
    const ctx = document.getElementById("rfmChart").getContext("2d");
    if (charts.rfm) charts.rfm.destroy();

    const labels = Object.keys(rfmData);
    const counts = Object.values(rfmData);

    charts.rfm = new Chart(ctx, {
        type: "polarArea",
        data: {
            labels: labels,
            datasets: [{
                data: counts,
                backgroundColor: [
                    "rgba(16, 185, 129, 0.7)",
                    "rgba(56, 189, 248, 0.7)",
                    "rgba(245, 158, 11, 0.7)",
                    "rgba(139, 92, 246, 0.7)",
                    "rgba(244, 63, 94, 0.7)",
                    "rgba(100, 116, 139, 0.7)"
                ],
                borderColor: "#1e293b",
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: "right", labels: { color: "#94a3b8", font: { size: 10 } } }
            },
            scales: {
                r: {
                    ticks: { display: false },
                    grid: { color: "rgba(51, 65, 85, 0.4)" }
                }
            }
        }
    });
}

// Render Table
function renderTable(transactions) {
    const tbody = document.getElementById("tableBody");
    tbody.innerHTML = "";

    transactions.forEach(t => {
        const tr = document.createElement("tr");

        let badgeClass = "badge-tech";
        if (t.Category === "Furniture") badgeClass = "badge-furn";
        if (t.Category === "Office Supplies") badgeClass = "badge-supp";

        const profitClass = Number(t.Profit) >= 0 ? "profit-pos" : "profit-neg";

        tr.innerHTML = `
            <td><code>${t.Order_ID}</code></td>
            <td>${t.Order_Date_Str}</td>
            <td><strong>${t.Customer_Name}</strong></td>
            <td>${t.Segment}</td>
            <td>${t.Region}</td>
            <td><span class="badge-tag ${badgeClass}">${t.Category}</span></td>
            <td>${t.Sub_Category}</td>
            <td>${formatCurrency(t.Sales)}</td>
            <td>${(Number(t.Discount) * 100).toFixed(0)}%</td>
            <td class="${profitClass}">${formatCurrency(t.Profit)}</td>
            <td><span class="badge cert-badge">${t.Order_Priority}</span></td>
        `;
        tbody.appendChild(tr);
    });
}

// Filter Slicers Interaction
function applyFilters() {
    if (!masterData) return;

    const selRegion = document.getElementById("filter-region").value;
    const selCategory = document.getElementById("filter-category").value;
    const selSegment = document.getElementById("filter-segment").value;
    const selDiscount = document.getElementById("filter-discount").value;

    let filtered = masterData.sample_transactions.filter(t => {
        if (selRegion !== "ALL" && t.Region !== selRegion) return false;
        if (selCategory !== "ALL" && t.Category !== selCategory) return false;
        if (selSegment !== "ALL" && t.Segment !== selSegment) return false;
        return true;
    });

    renderTable(filtered);
}

function resetFilters() {
    document.getElementById("filter-region").value = "ALL";
    document.getElementById("filter-category").value = "ALL";
    document.getElementById("filter-segment").value = "ALL";
    document.getElementById("filter-discount").value = "ALL";
    if (masterData) {
        renderTable(masterData.sample_transactions);
    }
}

// Real-time Table Search
function filterTable() {
    const query = document.getElementById("tableSearch").value.toLowerCase();
    const rows = document.querySelectorAll("#tableBody tr");
    rows.forEach(r => {
        const text = r.textContent.toLowerCase();
        r.style.display = text.includes(query) ? "" : "none";
    });
}
