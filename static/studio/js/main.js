// ----- Бургер -----
const burger = document.getElementById('burgerBtn');
const nav = document.getElementById('navMenu');

if (burger && nav) {
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav--open');
        burger.classList.toggle('burger--active');
    });
}

// ----- Плавний скрол для внутрішніх якорів -----
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href.length > 1) {
            e.preventDefault();
            const id = href.substring(1);
            const target = document.getElementById(id);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        }
    });
});

// ----- Перемикач теми (dark / light) -----
const themeToggle = document.getElementById('themeToggle');
const body = document.body;

function applyTheme(theme) {
    body.setAttribute('data-theme', theme);
    if (themeToggle) {
        themeToggle.textContent = theme === 'dark' ? '🌙' : '☀️';
    }
}

const savedTheme = localStorage.getItem('theme') || 'dark';
applyTheme(savedTheme);

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const newTheme = body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        applyTheme(newTheme);
        localStorage.setItem('theme', newTheme);
    });
}
