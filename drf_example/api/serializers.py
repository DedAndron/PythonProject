from rest_framework import serializers
from .models import Product, Category


class ProductModelSerializer(serializers.ModelSerializer):
    """
    props
    """
    
    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializer(serializers.Serializer):
    productId = serializers.UUIDField(source='id',
                                      read_only=True,
                                      required=False)
    name = serializers.CharField(max_length=255, required=False)
    price = serializers.FloatField(required=False)
    description = serializers.CharField(required=False)
    
    price_usd = serializers.SerializerMethodField()
    full_info = serializers.SerializerMethodField()
    
    """
    def get_<method_field_name>(self, obj)
    """
    def get_full_info(self, instance:Product):
        return f"{instance.id}-{instance.name}-{instance.price}"
    
    def get_price_usd(self, instance:Product):
        rate = self.context.get("usd_rate", 41)
        return round(instance.price / rate, 2)
    
    # def validate_<field>
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price can't be lte 0")
        return value
    
    def create(self, validated_data):
        print("Validate data: ", validated_data)
        return Product.objects.create(**validated_data)
    
    def update(self, instance:Product, validated_data):
        instance.name = validated_data.get('name')
        instance.price = validated_data.get('price')
        instance.description = validated_data.get('description')
        instance.save()
        return instance
    
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    categoryId = serializers.UUIDField(source='id',
                                      read_only=True,
                                      required=False)
    name = serializers.CharField(max_length=255, required=False)

    full_info = serializers.SerializerMethodField()

    def get_full_info(self, instance: Category):
        return f"{instance.id}-{instance.name}"
    def create(self, validated_data):
        print("Validate data: ", validated_data)
        return Category.objects.create(**validated_data)
    def update(self, instance:Category, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance