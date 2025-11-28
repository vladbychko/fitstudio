// static/studio/js/main.js

document.addEventListener("DOMContentLoaded", () => {
    /* ===========================
       THEME TOGGLE
    ============================ */
    const body = document.body;
    const themeToggle = document.getElementById("themeToggle");

    // зчитуємо збережену тему (dark / light)
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "light" || savedTheme === "dark") {
        body.setAttribute("data-theme", savedTheme);
    }

    function updateThemeIcon() {
        if (!themeToggle) return;
        const current = body.getAttribute("data-theme") || "dark";
        themeToggle.textContent = current === "dark" ? "🌙" : "☀️";
    }

    updateThemeIcon();

    if (themeToggle) {
        themeToggle.addEventListener("click", () => {
            const current = body.getAttribute("data-theme") || "dark";
            const next = current === "dark" ? "light" : "dark";
            body.setAttribute("data-theme", next);
            localStorage.setItem("theme", next);
            updateThemeIcon();
        });
    }

    /* ===========================
       BURGER MENU
    ============================ */
    const burger = document.getElementById("burgerBtn");
    const navMenu = document.getElementById("navMenu");

    if (burger && navMenu) {
        burger.addEventListener("click", () => {
            burger.classList.toggle("burger--active");
            navMenu.classList.toggle("nav--open");
        });
    }

    /* ===========================
       SMOOTH SCROLL ДЛЯ ЯКОРІВ
    ============================ */
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener("click", (e) => {
            const href = link.getAttribute("href");
            if (!href || href.length < 2) return;
            const target = document.getElementById(href.substring(1));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });
});
