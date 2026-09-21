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

  initServiceLines();
  initOfficesToggle();
  initFaqAccordion();
});

// "Eight service lines" tabbed panel: click a sidebar row to swap the detail panel.
function initServiceLines() {
  const sidebarItems = document.querySelectorAll(".sidebar-item");
  if (!sidebarItems.length) return;

  sidebarItems.forEach((item) => {
    item.addEventListener("click", () => {
      const index = item.dataset.line;

      document.querySelectorAll(".sidebar-item").forEach((el) => el.classList.remove("active"));
      item.classList.add("active");

      document.querySelectorAll(".service-lines-detail").forEach((panel) => {
        panel.classList.toggle("active", panel.dataset.linePanel === index);
      });
    });
  });
}

// Offices toggle pills: click DUBAI/CHENNAI to highlight the matching office card and pill.
function initOfficesToggle() {
  const toggles = document.querySelectorAll(".toggle-pill");
  if (!toggles.length) return;

  const cards = document.querySelectorAll(".office-card");

  toggles.forEach((toggle) => {
    toggle.addEventListener("click", () => {
      const index = Number(toggle.dataset.office);

      toggles.forEach((el) => el.classList.remove("active"));
      toggle.classList.add("active");

      if (cards[index]) {
        cards[index].scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
      }
    });
  });
}

// FAQ accordion: click a question to expand it, collapsing any other open one.
function initFaqAccordion() {
  const questions = document.querySelectorAll(".faq-question");
  if (!questions.length) return;

  questions.forEach((question) => {
    question.addEventListener("click", () => {
      const item = question.closest(".faq-item");
      const wasActive = item.classList.contains("active");

      document.querySelectorAll(".faq-item").forEach((el) => el.classList.remove("active"));
      if (!wasActive) item.classList.add("active");
    });
  });
}
