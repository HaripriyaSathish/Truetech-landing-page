// Scroll-reveal: adds `.active` to any `.reveal` element once it enters the
// viewport, which triggers the CSS transition defined in style.css.
// Extend this file with one small function per animated section as you
// convert each Figma screen — keep each animation isolated and named
// after the section it belongs to (e.g. animateHero, animateTestimonials).
document.addEventListener("DOMContentLoaded", () => {
  const revealEls = document.querySelectorAll(".reveal");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("active");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  revealEls.forEach((el) => observer.observe(el));
});
