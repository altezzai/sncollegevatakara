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
