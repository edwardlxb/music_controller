from rest_framework import serializers
from .models import Room

# Serializers allow complex data such as querysets and model instances to be converted
#   to native Python datatypes that can then be easily rendered into JSON,
#   XML or other content types. Serializers also provide deserialization,
#   allowing parsed data to be converted back into complex types,
#   after first validating the incoming data.


class RoomSerializer(serializers.ModelSerializer):
    # Serializer classes can also include reusable validators
    # that are applied to the complete set of field data.
    # These validators are included by declaring them on an
    # inner Meta class, like so:
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')

# make sure the data send using the post request is valid and
#      fits the fields we need


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')
