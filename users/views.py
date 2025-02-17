from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.template.loader import render_to_string

from .forms import UserRegistrationForm
from .forms import UserProfileForm
from .models import Cart, CartItem
from catalog.models import Product


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_url')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        # Если отправлена форма редактирования профиля
        if 'profile_submit' in request.POST:
            profile_form = UserProfileForm(request.POST, instance=user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Ваш профиль успешно обновлен.')
                return redirect('edit_profile')
            else:
                messages.error(request, 'Произошла ошибка при обновлении профиля. Проверьте введенные данные.')

        # Если отправлена форма изменения пароля
        elif 'password_submit' in request.POST:
            password_form = PasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Важно для сохранения сессии
                messages.success(request, 'Ваш пароль успешно изменен.')
                return redirect('edit_profile')
            else:
                messages.error(request, 'Произошла ошибка при изменении пароля. Проверьте введенные данные.')

    profile_form = UserProfileForm(instance=user)
    password_form = PasswordChangeForm(user)

    return render(request, 'edit_profile.html', {
        'profile_form': profile_form,
        'password_form': password_form,
    })


@login_required
def add_to_cart(request, product_id):

    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)

        cart, cart_created = Cart.objects.get_or_create(user=request.user)

        cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not cart_item_created:
            cart_item.quantity += 1
            cart_item.save()

        items = cart.items.all()
        total_count = items.count()

        # Рендерим обновлённый HTML корзины.
        cart_html = render_to_string('cart.html', {
            'cart_items': cart.items.all(),
            'cart_total_sum': cart.get_total_sum(),
        })

        return JsonResponse({
            'success': True,
            'total_count': total_count,
            'cart_html': cart_html,
        })

    return JsonResponse({'success': False, 'error': 'Only POST allowed'})

@login_required
def del_from_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item = cart.items.filter(product=product).first()
        if cart_item:
            cart_item.delete()

        items = cart.items.all()
        total_count = items.count()

        cart_html = render_to_string('cart.html', {
            'cart_items': cart.items.all(),
            'cart_total_sum': cart.get_total_sum(),
        })

        return JsonResponse({
            'success': True,
            'total_count': total_count,
            'cart_html': cart_html,
        })

    return JsonResponse({'success': False, 'error': 'Only POST allowed'})

# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#
#     cart, cart_created = Cart.objects.get_or_create(user=request.user)
#
#     cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)
#
#     if not cart_item_created:
#         cart_item.quantity += 1
#         cart_item.save()
#
#     # Получаем адрес, откуда пришёл пользователь
#     referer = request.META.get('HTTP_REFERER')
#     return redirect(referer)
#
#
# @login_required
# def del_from_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart, created = Cart.objects.get_or_create(user=request.user)
#
#     cart_item = cart.items.filter(product=product).first()
#     if cart_item:
#         cart_item.delete()
#
#     referer = request.META.get('HTTP_REFERER')
#     return redirect(referer)
