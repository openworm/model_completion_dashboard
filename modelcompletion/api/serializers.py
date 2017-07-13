from rest_framework import serializers

class CellSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)

class NeuronSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()

class MuscleSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()

class ChannelSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()

class BodyMuscleSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()

class PharynxMuscleSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()
