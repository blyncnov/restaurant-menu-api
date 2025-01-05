from rest_framework.decorators import api_view
from rest_framework.response import Response

from restaurant.models import Restaurant
from restaurant.serializer import RestaurantSerializer

# Create your views here.

@api_view(['GET'])
def get_restaurants(request):
    all_restaurants = Restaurant.objects.all()
    serialized_restaurants = RestaurantSerializer(all_restaurants, many=True)
    return Response(serialized_restaurants.data)


@api_view(['GET'])
def get_restaurant(request, restaurant_id):
    print(restaurant_id)
    restaurant = Restaurant.objects.get(id=restaurant_id)
    serialized_restaurant = RestaurantSerializer(restaurant, many=False)
    return Response(serialized_restaurant.data)
