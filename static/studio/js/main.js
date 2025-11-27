document.addEventListener('DOMContentLoaded', () => {
    const nav = document.getElementById('nav');
    const burger = document.getElementById('burger');
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');

    // Бургер-меню
    if (burger && nav) {
        burger.addEventListener('click', () => {
            nav.classList.toggle('nav--open');
        });

        // Закривати меню при кліку на лінк
        nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                nav.classList.remove('nav--open');
            });
        });
    }

    // Плавний скрол до секцій
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const href = anchor.getAttribute('href');
            if (!href || href === '#') return;
            const target = document.querySelector(href);
            if (!target) return;

            e.preventDefault();
            window.scrollTo({
                top: target.offsetTop - 70,
                behavior: 'smooth'
            });
        });
    });

    // Імітація відправки форми (без бекенду)
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const name = contactForm.querySelector('#name').value.trim();
            const phone = contactForm.querySelector('#phone').value.trim();

            if (!name || !phone) {
                formMessage.textContent = 'Будь ласка, заповніть всі обов’язкові поля.';
                formMessage.style.color = '#ff6b6b';
                return;
            }

            formMessage.textContent = 'Дякуємо! Ми зв’яжемося з вами найближчим часом.';
            formMessage.style.color = '#4ff1c6';

            contactForm.reset();
        });
    }
});
