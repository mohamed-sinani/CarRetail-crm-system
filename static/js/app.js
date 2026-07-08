document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.querySelector("#crmSidebar");
    const backdrop = document.querySelector(".sidebar-backdrop");
    const toggle = document.querySelector("[data-sidebar-toggle]");

    if (toggle && sidebar && backdrop) {
        toggle.addEventListener("click", () => {
            sidebar.classList.add("open");
            backdrop.classList.add("show");
        });
        backdrop.addEventListener("click", () => {
            sidebar.classList.remove("open");
            backdrop.classList.remove("show");
        });
    }

    const salesCanvas = document.querySelector("#salesChart");
    const statusCanvas = document.querySelector("#statusChart");

    if (salesCanvas && window.Chart) {
        const labels = JSON.parse(document.querySelector("#sales-labels").textContent);
        const values = JSON.parse(document.querySelector("#sales-values").textContent);
        new Chart(salesCanvas, {
            type: "line",
            data: {
                labels,
                datasets: [{
                    label: "Revenue",
                    data: values,
                    borderColor: "#F59E0B",
                    backgroundColor: "rgba(245, 158, 11, .14)",
                    fill: true,
                    tension: .38,
                    pointRadius: 4,
                    pointBackgroundColor: "#111827"
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false } },
                scales: {
                    y: { beginAtZero: true, grid: { color: "#EEF2F7" } },
                    x: { grid: { display: false } }
                }
            }
        });
    }

    if (statusCanvas && window.Chart) {
        const values = JSON.parse(document.querySelector("#vehicle-status-values").textContent);
        new Chart(statusCanvas, {
            type: "doughnut",
            data: {
                labels: ["Available", "Reserved", "Sold"],
                datasets: [{
                    data: values,
                    backgroundColor: ["#10B981", "#F59E0B", "#EF4444"],
                    borderWidth: 0
                }]
            },
            options: {
                cutout: "68%",
                plugins: { legend: { position: "bottom", labels: { usePointStyle: true } } }
            }
        });
    }

    document.querySelectorAll("[data-copy-text]").forEach((button) => {
        button.addEventListener("click", async () => {
            const originalText = button.textContent;
            await navigator.clipboard.writeText(button.getAttribute("data-copy-text"));
            button.textContent = "Copied";
            window.setTimeout(() => {
                button.textContent = originalText;
            }, 1400);
        });
    });
});
