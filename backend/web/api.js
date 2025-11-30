const BASE_URL = 'https://your-render-app.onrender.com';

export async function getMenu() {
    try {
        const response = await fetch(`${BASE_URL}/menu`);
        if (!response.ok) {
            throw new Error('Ошибка при получении меню');
        }
        const data = await response.json();
        return data;
    } catch (err) {
        console.error(err);
        return [];
    }
}

export async function placeOrder(order) {
    try {
        const response = await fetch(`${BASE_URL}/order`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(order)
        });
        if (!response.ok) {
            throw new Error('Ошибка при отправке заказа');
        }
        const data = await response.json();
        return data;
    } catch (err) {
        console.error(err);
        return null;
    }
}

export async function renderMenu() {
    const menuContainer = document.getElementById('menu');
    if (!menuContainer) return;

    const menu = await getMenu();
    menuContainer.innerHTML = '';

    menu.forEach(item => {
        const div = document.createElement('div');
        div.className = 'menu-item';
        div.innerHTML = `
            <h3>${item.name}</h3>
            <p>${item.description}</p>
            <strong>${item.price} ₽</strong>
            <button onclick="addToCart(${item.id})">Добавить в заказ</button>
        `;
        menuContainer.appendChild(div);
    });
}

export function addToCart(itemId) {
    console.log('Добавлено в корзину: ', itemId);
}
