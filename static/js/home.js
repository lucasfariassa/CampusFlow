document.addEventListener("DOMContentLoaded", function() {
    const carousel = document.getElementById("image-carousel");
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");

    prevButton.addEventListener("click", function() {
        carousel.scrollBy(-248, 0);
    });

    nextButton.addEventListener("click", function() {
        carousel.scrollBy(248, 0);
    });
});
