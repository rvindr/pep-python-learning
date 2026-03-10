from rest_framework import serializers
from .models import User

# class UserSerialier(serializers.Serializer):

#     def start_s(value):
#         if value[0].lower()!='s':
#             raise serializers.ValidationError('Name must be start with s only')
#     id = serializers.CharField(required=False)
#     name = serializers.CharField(required=True,validators = [start_s])
#     phone_num = serializers.IntegerField(required=True)
#     city = serializers.CharField(required=True)


#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
    

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.phone_num = validated_data.get('phone_num',instance.phone_num)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance

#     # types of validation
#     # field level validation

#     def validate_phone_num(self, value):
#         if len(str(value)) != 10:
#             raise serializers.ValidationError("Phone number must 10 digits")

#     # object level validation
#     def validate(self, attrs):
#         nm = attrs.get('name')
#         c = attrs.get('city')
#         p = attrs.get('phone_num')

#         if nm.lower() == 'ravinder' and c.lower() != 'sirsa':
#             raise serializers.ValidationError('City must be sirsa')
#         return attrs
    

class UserSerialier(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['name', 'city', 'phone_num']
        # read_only_fields = ['name', ]


    # validation method will work in the same way as Serializer class