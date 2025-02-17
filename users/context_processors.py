from .models import Cart


def cart_context(request):
    if not request.user.is_authenticated:
        return {
            'cart_items': [],
            'cart_total_sum': 0,
        }

    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()

    total_sum = cart.get_total_sum()

    return {
        'cart_items': items,
        'cart_total_sum': total_sum,
    }
