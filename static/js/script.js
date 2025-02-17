document.addEventListener('DOMContentLoaded', function () {
    const addToCartLinks = document.querySelectorAll('.add-to-cart');
    const cartButton = document.querySelector('.cart-button');
    const cartContainer = document.querySelector('.cart-container');

    if (addToCartLinks) {
        addToCartLinks.forEach(link => {
            link.addEventListener('click', function (event) {
                event.preventDefault(); // Останавливаем переход по ссылке

                const url = link.getAttribute('href'); // Получаем URL из ссылки.

                // Отправляем AJAX-запрос
                fetch(url, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'), // Передаём CSRF-токен
                        'Content-Type': 'application/json',
                    },
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            // Успешное добавление: обновляем интерфейс
                            updateCartButton(data.total_count); // Обновляем кнопку корзины.
                            updateCartHTML(data.cart_html);    // Обновляем содержимое корзины.
                        } else {
                            // Ошибка
                            console.error(data.error);
                        }
                    })
                    .catch(error => {
                        console.error('Ошибка при запросе:', error);
                        alert('Произошла ошибка при добавлении товара в корзину.');
                    });
            });
        });
    }

    if (cartContainer) {
        // Обработка кликов на элементы внутри корзины.
        cartContainer.addEventListener('click', (event) => {

            event.preventDefault(); // Останавливаем переход по ссылке.

            const target = event.target;

            // Проверяем, что кликнули по ссылке с классом "del-from-cart".
            if (target.tagName === 'A' && target.classList.contains('del-from-cart')) {
                event.preventDefault(); // Останавливаем переход по ссылке.

                const url = target.getAttribute('href'); // Получаем URL из ссылки.

                // Отправляем AJAX-запрос.
                fetch(url, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),
                        'Content-Type': 'application/json',
                    },
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            // Успешное удаление: обновляем интерфейс.
                            updateCartButton(data.total_count); // Обновляем кнопку корзины.
                            updateCartHTML(data.cart_html); // Обновляем содержимое корзины.
                        } else {
                            // Ошибка удаления.
                            console.error(data.error);
                        }
                    })
                    .catch(error => {
                        console.error('Ошибка при запросе:', error);
                        alert('Произошла ошибка при удалении товара из корзины.');
                    });
            }
        });
    }

    // Функция для обновления кнопки корзины.
    function updateCartButton(totalCount) {
        if (cartButton) {
            if (totalCount > 0) {
                cartButton.classList.remove('btn-empty');
                cartButton.classList.add('btn-nonempty');
                cartButton.textContent = `${totalCount} товаров`;
            } else {
                cartButton.classList.remove('btn-nonempty');
                cartButton.classList.add('btn-empty');
                cartButton.textContent = 'Пусто';
            }
        }
    }

    // Функция для обновления HTML корзины.
    function updateCartHTML(html) {
        if (cartContainer) {
            cartContainer.innerHTML = html; // Заменяем содержимое корзины.
        }
    }

    // Вспомогательная функция для получения CSRF-токена из cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    sorting = document.getElementById('sorting');

    if (sorting) {
        sorting.addEventListener('change', function (evt) {
            const selectedValue = evt.target.value;
            const container = document.querySelector('.products-container');
            const products = Array.from(container.querySelectorAll('.product'));

            // Сортировка элементов
            products.sort((a, b) => {
                // Для популярности (булево значение)
                if (selectedValue === 'popularity') {
                    // Сортируем true -> false
                    if (a.dataset.popularity === 'true') {
                        return -1;
                    } else {
                        return 1;
                    }
                }

                // Для цены
                else if (selectedValue === 'price_asc' || selectedValue === 'price_desc') {
                    const aPrice = parseFloat(a.dataset.price);
                    const bPrice = parseFloat(b.dataset.price);

                    if (selectedValue === 'price_asc') {
                        return aPrice - bPrice;
                    } else {
                        return bPrice - aPrice;
                    }
                }

                // Для жирности
                else if (selectedValue === 'fat') {
                    const aFat = parseFloat(a.dataset.fat);
                    const bFat = parseFloat(b.dataset.fat);

                    return aFat - bFat;
                }
            });

            // Перезапись элементов в контейнере
            container.innerHTML = '';
            products.forEach(product => container.appendChild(product));
        });
    }

});