/*
===========================================
Portfolio v2 JavaScript
Debashish Talukder
===========================================
*/

document.addEventListener("DOMContentLoaded", () => {

    /* ======================================
       Navbar Shadow on Scroll
    ====================================== */

    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", () => {

        if (window.scrollY > 50) {

            navbar.style.background = "#0f172a";
            navbar.style.boxShadow = "0 8px 20px rgba(0,0,0,.15)";

        } else {

            navbar.style.background = "rgba(15,23,42,.95)";
            navbar.style.boxShadow = "none";

        }

    });

    /* ======================================
       Fade In Animation
    ====================================== */

    const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.classList.add("show");

            }

        });

    }, {
        threshold: 0.15
    });

    document.querySelectorAll(".stats-card,.skill-card,.project-card")
        .forEach(card => {

            card.classList.add("hidden");

            observer.observe(card);

        });

    /* ======================================
       Counter Animation
    ====================================== */

    const counters = document.querySelectorAll(".stats-card h2");

    counters.forEach(counter => {

        const text = counter.innerText;

        const number = parseInt(text);

        if (isNaN(number))
            return;

        let current = 0;

        const increment = Math.ceil(number / 40);

        const timer = setInterval(() => {

            current += increment;

            if (current >= number) {

                counter.innerText = text;

                clearInterval(timer);

            } else {

                if (text.includes("+")) {

                    counter.innerText = current + "+";

                } else {

                    counter.innerText = current;

                }

            }

        }, 40);

    });

    /* ======================================
       Active Navigation
    ====================================== */

    const links = document.querySelectorAll(".nav-link");

    links.forEach(link => {

        if (link.href === window.location.href) {

            link.classList.add("active");

        }

    });

    /* ======================================
       Smooth Hover Effect
    ====================================== */

    document.querySelectorAll(".project-card").forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-12px)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "";

        });

    });

});

/* ===================================
   Scroll Reveal Animation
=================================== */

.hidden{

    opacity:0;

    transform:translateY(40px);

    transition:all .8s ease;

}

.show{

    opacity:1;

    transform:translateY(0);

}

/* ===================================
   Active Navigation
=================================== */

.nav-link.active{

    color:#38bdf8 !important;

    font-weight:600;

}