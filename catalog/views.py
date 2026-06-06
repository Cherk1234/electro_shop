import json
import random
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Order

def product_list(request):
    products = Product.objects.all()
    categories = set(p.category.name for p in products if p.category)
    return render(request, 'catalog/index.html', {
        'products': products,
        'categories': categories
    })

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        num = str(random.randint(100000, 999999))
        
        Order.objects.create(
            order_number=num,
            phone=data.get('phone'),
            details=data.get('details')
        )
        return JsonResponse({'status': 'success', 'order_number': num})
    return JsonResponse({'status': 'error'}, status=400)

def track_order(request):
    num = request.GET.get('num', '').strip()
    try:
        # ИСПРАВЛЕНО: добавлено .objects
        order = Order.objects.get(order_number=num)
        return JsonResponse({
            'found': True, 
            'number': order.order_number, 
            'date': order.created_at.strftime('%d.%m.%Y')
        })
    except Order.DoesNotExist:
        return JsonResponse({'found': False})
