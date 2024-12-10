console.log('catalog.js загружен');

let cart = [];

// Получаем данные из JSON
const productsData = JSON.parse(document.getElementById('products-data').textContent);
const drinksData = JSON.parse(document.getElementById('drinks-data').textContent);

console.log('Products Data:', productsData);
console.log('Drinks Data:', drinksData);

function displayProducts(categoryId) {
    console.log('displayProducts called with category:', categoryId);
    const grid = document.getElementById('productsGrid');
    grid.innerHTML = '';

    let filteredProducts = productsData.filter(product => product.fields.category === categoryId);
    let filteredDrinks = drinksData.filter(drink => drink.fields.category === categoryId);

    console.log('Filtered Products:', filteredProducts);
    console.log('Filtered Drinks:', filteredDrinks);

    filteredProducts.forEach(product => {
        const card = document.createElement('div');
        card.className = 'product-card';

        card.innerHTML = `
        <div class="product-image" style="background-image: url('/media/${product.fields.image}');"></div>
        <h3 class="product-title">${product.fields.name}</h3>
        <p class="product-desc">${product.fields.description}</p>
        <p class="product-price">${product.fields.price} ₽</p>
        <button class="add-to-cart" onclick="addToCart(${product.pk}, 'product')">Добавить в корзину</button>
    `;
        grid.appendChild(card);
    });

    filteredDrinks.forEach(drink => {
        const card = document.createElement('div');
        card.className = 'product-card';

        card.innerHTML = `
        <div class="product-image" style="background-image: url('/media/${drink.fields.image}');"></div>
        <h3 class="product-title">${drink.fields.name}</h3>
        <p class="product-desc">${drink.fields.description}</p>
        <p class="product-price">${drink.fields.price} ₽</p>
        <button class="add-to-cart" onclick="addToCart(${drink.pk}, 'drink')">Добавить в корзину</button>
    `;
        grid.appendChild(card);
    });
}

function searchProducts(query) {
    console.log('searchProducts called with query:', query);
    const grid = document.getElementById('productsGrid');
    grid.innerHTML = '';

    const searchResults = [];

    // Search through all categories
    const allProducts = [...productsData, ...drinksData];
    const results = allProducts.filter(product =>
        product.fields.name.toLowerCase().includes(query.toLowerCase()) ||
        product.fields.description.toLowerCase().includes(query.toLowerCase())
    );
    searchResults.push(...results);

    if (searchResults.length === 0) {
        grid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 40px;">
            <h3>К сожалению, ничего не найдено 😿</h3>
            <p>Попробуйте изменить параметры поиска</p>
        </div>
    `;
        return;
    }

    // Display search results
    searchResults.forEach(product => {
        const card = document.createElement('div');
        card.className = 'product-card';

        card.innerHTML = `
        <div class="product-image" style="background-image: url('/media/${product.fields.image}');"></div>
        <h3 class="product-title">${product.fields.name}</h3>
        <p class="product-desc">${product.fields.description}</p>
        <p class="product-price">${product.fields.price} ₽</p>
        <button class="add-to-cart" onclick="addToCart(${product.pk}, '${product.fields.model}')">Добавить в корзину</button>
    `;
        grid.appendChild(card);
    });
}

function addToCart(productId, productType) {
    console.log('addToCart called with productId:', productId, 'and productType:', productType);
    let product;
    const allProducts = [...productsData, ...drinksData];
    product = allProducts.find(p => p.pk === productId && p.fields.model === productType);

    const existingItem = cart.find(item => item.pk === productId && item.model === productType);
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({ ...product.fields, quantity: 1, model: productType });
    }

    updateCart();
    openCart(); // Открываем корзину после добавления товара
    saveCartToSession(); // Сохраняем корзину в сессии
}

function updateCart() {
    const cartItems = document.querySelector('.cart-items');
    const totalElement = document.querySelector('.total-amount');

    if (cart.length === 0) {
        cartItems.innerHTML = `
        <div class="empty-cart">
            <p>Ваша корзина пуста</p>
            <button class="find-sweets-btn">Найти что-нибудь вкусненькое</button>
        </div>
    `;
        document.querySelector('.cart-total').style.display = 'none';
        return;
    }

    document.querySelector('.cart-total').style.display = 'block';
    cartItems.innerHTML = cart.map(item => `
    <div class="cart-item">
        <div class="product-image" style="background-image: url('/media/${item.image}');"></div>
        <div class="item-details">
            <h4>${item.name}</h4>
            <p>${item.price} ₽</p>
            <div class="quantity-controls">
                <button class="quantity-btn" onclick="updateQuantity(${item.pk}, '${item.model}', -1)">-</button>
                <span>${item.quantity}</span>
                <button class="quantity-btn" onclick="updateQuantity(${item.pk}, '${item.model}', 1)">+</button>
            </div>
        </div>
        <button class="close-cart" onclick="removeFromCart(${item.pk}, '${item.model}')">×</button>
    </div>
`).join('');

    const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
    totalElement.textContent = total;
}

function updateQuantity(productId, productType, change) {
    const itemIndex = cart.findIndex(item => item.pk === productId && item.model === productType);

    if (itemIndex !== -1) {
        cart[itemIndex].quantity += change;
        if (cart[itemIndex].quantity <= 0) {
            cart.splice(itemIndex, 1);
        }
        updateCart();
        saveCartToSession(); // Сохраняем корзину в сессии
    }
}

function removeFromCart(productId, productType) {
    cart = cart.filter(item => !(item.pk === productId && item.model === productType));
    updateCart();
    saveCartToSession(); // Сохраняем корзину в сессии
}

function openCart() {
    console.log('openCart called');
    document.querySelector('.cart').classList.add('open');
}

function closeCart() {
    console.log('closeCart called');
    document.querySelector('.cart').classList.remove('open');
}

function saveCartToSession() {
    fetch('/save_cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(cart)
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Cart saved to session');
            } else {
                console.error('Failed to save cart to session');
            }
        });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    displayProducts(1); // Предполагаем, что 'cakes' имеет id 1

    // Add these new event listeners for search
    const searchInput = document.querySelector('.search-input');
    const searchButton = document.querySelector('.search-button');

    function performSearch() {
        const query = searchInput.value.trim();
        if (query) {
            document.querySelectorAll('.category-btn').forEach(btn => btn.classList.remove('active'));
            searchProducts(query);
        } else {
            document.querySelector('.category-btn[data-category="1"]').click(); // Предполагаем, что 'cakes' имеет id 1
        }
    }

    searchButton.addEventListener('click', performSearch);

    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            performSearch();
        }
    });

    document.querySelectorAll('.category-btn').forEach(button => {
        button.addEventListener('click', (e) => {
            document.querySelectorAll('.category-btn').forEach(btn => btn.classList.remove('active'));
            e.target.classList.add('active');
            searchInput.value = ''; // Clear search input when switching categories
            displayProducts(parseInt(e.target.dataset.category, 10));
        });
    });

    document.querySelector('.close-cart').addEventListener('click', closeCart);

    document.querySelector('.cart').addEventListener('click', (e) => {
        if (e.target.classList.contains('find-sweets-btn')) {
            closeCart();
            document.querySelector('.category-btn[data-category="1"]').click(); // Предполагаем, что 'cakes' имеет id 1
        }
    });
});

document.querySelector('.checkout-btn').addEventListener('click', () => {
    if (cart.length === 0) {
        alert('Ваша корзина пуста. Добавьте товары перед оформлением заказа.');
        return;
    }

    fetch('/check_auth/')
        .then(response => response.json())
        .then(data => {
            if (data.is_authenticated) {
                const totalAmount = document.querySelector('.total-amount').textContent;
                window.location.href = `/checkout/?total=${totalAmount}`;
            } else {
                alert('Для оформления заказа необходимо авторизоваться. Пожалуйста, войдите в систему или зарегистрируйтесь.');
                window.location.href = '/login/';
            }
        });
});
