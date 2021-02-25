from rest_framework import serializers

class UserSerializar(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombres = serializers.CharField(max_length=200, required=True, allow_blank=False)
    apellidos = serializers.CharField(max_length=200, required=False, allow_blank=True)
    edad = serializers.IntegerField(required=False)
    email = serializers.CharField(max_length=300, required=True)
    clave = serializers.CharField(max_length=30, required=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)