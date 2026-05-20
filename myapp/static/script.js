const bm = document.querySelector(".bm");
const nav = document.querySelector(".l");
const cl = document.querySelector(".close");

// Scroll - navbar shadow
const navcon = document.querySelector(".navcon");
window.addEventListener("scroll", () => {
  //remove nav
  if (window.scrollY == 0) {
    navcon.classList.remove("shadow");
  } else {
    navcon.classList.add("shadow");
  }
});

// navbar animations

function opennav() {
  nav.classList.add("open");
  cl.style.display = "flex";
}

function closenav() {
  nav.classList.remove("open");
  cl.style.display = "none";
}

function togglelist(element, cls) {
  if (!element.classList.contains(cls)) element.style.display = "flex";
  setTimeout(() => {
    element.classList.toggle(cls);
  }, 10);
  setTimeout(() => {
    if (!element.classList.contains(cls)) element.style.display = "none";
  }, 210);
}

// Add-on Courses: Read more / Read less
document.addEventListener("DOMContentLoaded", () => {
  const toggleButtons = document.querySelectorAll(".js-addon-toggle");
  if (!toggleButtons.length) return;

  toggleButtons.forEach((btn) => {
    const targetId = btn.getAttribute("data-target");
    if (!targetId) return;
    const target = document.getElementById(targetId);
    if (!target) return;

    // Default collapsed (JS-enabled only)
    target.classList.add("is-collapsed");
    btn.style.display = "inline-flex";

    btn.addEventListener("click", () => {
      const isCollapsed = target.classList.toggle("is-collapsed");
      const moreText = btn.getAttribute("data-more") || "Show more";
      const lessText = btn.getAttribute("data-less") || "Show less";
      btn.textContent = isCollapsed ? moreText : lessText;
    });
  });
});
