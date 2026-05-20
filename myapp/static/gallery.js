(() => {
    const modal = document.getElementById("galleryModal");
    if (!modal) return;

    const titleEl = document.getElementById("galleryTitle");
    const imgEl = document.getElementById("galleryImg");
    const countEl = document.getElementById("galleryCount");
    const closeBtn = document.getElementById("galleryClose");
    const prevBtn = document.getElementById("galleryPrev");
    const nextBtn = document.getElementById("galleryNext");

    let images = [];
    let index = 0;

    const setIndex = (newIndex) => {
        if (!images.length) return;
        index = (newIndex + images.length) % images.length;
        imgEl.src = images[index];
        countEl.textContent = `${index + 1} / ${images.length}`;
    };

    const open = (title, imageList) => {
        images = imageList.filter(Boolean);
        index = 0;
        titleEl.textContent = title || "";

        if (!images.length) return;

        modal.classList.add("open");
        modal.setAttribute("aria-hidden", "false");
        document.body.style.overflow = "hidden";

        setIndex(0);
    };

    const close = () => {
        modal.classList.remove("open");
        modal.setAttribute("aria-hidden", "true");
        document.body.style.overflow = "";
        imgEl.src = "";
        images = [];
        index = 0;
    };

    document.querySelectorAll(".gallery-open").forEach((el) => {
        el.addEventListener("click", (e) => {
            e.preventDefault();
            const title = el.getAttribute("data-title") || "";
            const raw = el.getAttribute("data-images") || "";
            const list = raw.split("|").map((s) => s.trim());
            open(title, list);
        });
    });

    closeBtn?.addEventListener("click", close);
    modal.addEventListener("click", (e) => {
        if (e.target === modal) close();
    });
    prevBtn?.addEventListener("click", () => setIndex(index - 1));
    nextBtn?.addEventListener("click", () => setIndex(index + 1));

    document.addEventListener("keydown", (e) => {
        if (!modal.classList.contains("open")) return;
        if (e.key === "Escape") close();
        if (e.key === "ArrowLeft") setIndex(index - 1);
        if (e.key === "ArrowRight") setIndex(index + 1);
    });
})();
