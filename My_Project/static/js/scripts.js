function displayProducts() {
    const productsContainer = document.getElementById('productsContainer');
    productsContainer.innerHTML = '';
    products.forEach(product => {
        const productCard = document.createElement('div');
        productCard.classList.add('product-card');
        productCard.innerHTML = `
            <h3>${product.name}</h3>
            <p>Price: $${product.price.toFixed(2)}</p>
            <button onclick="buyNow(${product.id})">Buy Now</button>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productsContainer.appendChild(productCard);
    });
}

// Function to add a product to the cart
function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        // Implement cart functionality as needed
        console.log(`Added ${product.name} to cart.`);
    }
}

// Function to handle buy now action
function buyNow(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        // Implement buy now functionality as needed
        console.log(`Buying ${product.name} now.`);
    }
}

// Display products when the page loads
displayProducts();