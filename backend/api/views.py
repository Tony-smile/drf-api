import json
from django.http import JsonResponse
from products.models import Products

def api_home(request, *args, **kwargs):
    model_data = Products.objects.all.order_by("?").first()
    
    data = {}
    if model_data:
        data['product_id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price 

    return JsonResponse(data)
   # return JsonResponse({"Greetings": "Hello there, welce to my api"})