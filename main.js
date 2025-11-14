/* ======================================================
   AGRIFARMA PREMIUM UI INTERACTIONS
   File: main.js
====================================================== */

// Navbar color change on scroll
window.addEventListener("scroll", function() {
  const navbar = document.querySelector(".navbar");
  if (window.scrollY > 50) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function(e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth"
    });
  });
});

// Fade-in animations on scroll
const fadeEls = document.querySelectorAll('.fade-in');
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

fadeEls.forEach(el => observer.observe(el));

// Add class for visible fade-in
document.styleSheets[0].insertRule(`
  .fade-in.visible {
    opacity: 1 !important;
    transform: translateY(0) !important;
    transition: opacity 0.8s ease, transform 0.8s ease;
  }
`, document.styleSheets[0].cssRules.length);
