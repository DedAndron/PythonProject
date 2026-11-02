const cardContainer = document.getElementById("test-card");

if (cardContainer) {
    cardContainer.innerHTML = `
        <section class="card shadow-sm h-100" style="max-width: 320px">
            <img src="${cardContainer.dataset.imageUrl}" class="card-img-top" alt="Card image">
            <div class="card-body">
                <h4 class="card-title">Card title</h4>
                <p class="card-text">
                    Some quick example text to build on the card title and make up the bulk of the card’s content.
                </p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </section>
    `;
}