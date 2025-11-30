const tg = window.Telegram.WebApp;
tg.expand();

const lang = tg.initDataUnsafe?.user?.language_code || "en";

const menuContainer = document.getElementById("menu-container");
const selected = [];

const BASE_URL = window.location.origin;

fetch(`${BASE_URL}/menu`)
    .then(res => res.json())
    .then(menu => {
        menuContainer.innerHTML = "";
        menu.forEach(item => {
            const card = document.createElement("div");
            card.classList.add("item");
            
            const name = item.name[lang] || item.name["en"];
            const description = item.description[lang] || item.description["en"];
            
            const weightOptions = item.weight?.map(w => `<option value="${w.value}">${w.value} ${w.unit}</option>`).join("") || "";
            
            card.innerHTML = `
                <img src="${item.image}" alt="${name}">
                <div class="item-title">${name}</div>
                <div class="item-description">${description}</div>
                <div class="item-weight">
                    <label>Вес:</label>
                    <select class="weight-selector">${weightOptions}</select>
                </div>
                <div class="item-price">${item.price} ₽</div>
                <button class="btn add" data-name="${name}" data-price="${item.price}">Добавить</button>
            `;
            menuContainer.appendChild(card);
        });
        
        document.querySelectorAll(".btn.add").forEach(btn => {
            btn.addEventListener("click", () => {
                const card = btn.closest(".item");
                const selectedWeight = card.querySelector(".weight-selector")?.value || "";
                
                const item = {
                    name: btn.dataset.name,
                    price: Number(btn.dataset.price),
                    weight: selectedWeight
                };
                
                selected.push(item);
                
                tg.MainButton.setText(`Оформить заказ (${selected.length})`);
                tg.MainButton.show();
                
                console.log("Добавлено в заказ:", item);
            });
        });
    })
    .catch(err => console.error("Ошибка загрузки меню:", err));

tg.MainButton.onClick(() => {
    tg.sendData(JSON.stringify(selected));
});
