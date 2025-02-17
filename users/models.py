from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Создаёт отношение "один-к-одному" между моделью Cart и моделью User.
    # Это значит, что каждый пользователь (User) может иметь только одну корзину (Cart),
    # и каждая корзина принадлежит только одному пользователю.

    # Аргумент on_delete=models.CASCADE:
    # Когда пользователь (User) удаляется, связанная с ним корзина (Cart) будет также автоматически удалена.
    # Это помогает поддерживать целостность данных и избегать ситуаций, когда у нас остаются "сиротские"
    # записи в базе данных.

    def get_total_sum(self):
        return sum(item.quantity * item.product.price for item in self.items.all())

    def __str__(self):
        return f"Cart of {self.user.username}"

# CartItem связывает конкретный товар с количеством, которое пользователь выбрал,
# и привязывает это к корзине, которая принадлежит конкретному пользователю.
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    # создаёт отношение "многие-к-одному" с моделью Cart.
    # Это означает, что один объект Cart может быть связан с несколькими объектами CartItem,
    # но каждый объект CartItem может быть связан только с одним объектом Cart.

    # related_name='items' позволяет обращаться к связанным объектам CartItem из объекта Cart
    # через атрибут items. Например, если у нас есть объект cart,
    # то мы можем получить все связанные с ним CartItem с помощью cart.items.all().

    # on_delete=models.CASCADE указывает, что если связанный объект Cart будет удалён,
    # то все связанные с ним объекты CartItem также будут автоматически удалены.

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # один объект Product может быть связан с несколькими объектами CartItem,
    # но каждый объект CartItem может быть связан только с одним объектом Product.
    # Например, если у нас есть несколько корзин,
    # то один и тот же продукт может присутствовать в каждой из них как отдельный элемент корзины.

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

