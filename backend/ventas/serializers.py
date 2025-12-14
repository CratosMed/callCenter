from rest_framework import serializers
from .models import Venta, Telefono

# Serializer para los Teléfonos
class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = ['id', 'numero', 'etiqueta']

# Serializer Principal para la Venta
class VentaSerializer(serializers.ModelSerializer):
    # Aquí incrustamos los teléfonos dentro de la venta
    telefonos = TelefonoSerializer(many=True, required=False) # many=True porque pueden ser varios

    class Meta:
        model = Venta
        fields = '__all__' # ¡Truco! Esto incluye TODOS los campos automáticamente

    # Esta función mágica permite guardar una venta Y sus teléfonos al mismo tiempo
    def create(self, validated_data):
        telefonos_data = validated_data.pop('telefonos', []) # Saca los teléfonos aparte
        venta = Venta.objects.create(**validated_data) # Crea la venta primero
        
        # Crea cada teléfono y lo asocia a la venta creada
        for telefono_data in telefonos_data:
            Telefono.objects.create(venta=venta, **telefono_data)
        return venta