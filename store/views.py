from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# GET all products
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# POST (add product manually via API)
@api_view(['POST'])
def add_product(request):
    many = isinstance(request.data, list)
    serializer = ProductSerializer(data=request.data, many=many)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_product(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return Response({"message": "Product deleted successfully"})
    except Product.DoesNotExist:
        return Response({"error": "Product not found"})