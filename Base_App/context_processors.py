from Base_App.models import Cart

from .utils import cms


def cart_item_count(request):
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()
    else:
        count = 0
    return {'cart_count': count}


def cms_processor(request):
    return {'cms': cms}