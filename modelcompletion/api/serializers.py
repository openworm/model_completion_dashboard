from rest_framework import serializers

class StringListField(serializers.ListField):
    child = serializers.CharField()

class CellSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)

class NeuronSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()

class NeuronDetailSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()
    receptors = StringListField()
    type = StringListField()
    innexin= StringListField()
    neurotransmitter = StringListField()
    neuropeptide = StringListField()


class MuscleDetailSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=200)
    completeness=serializers.IntegerField()
    neurons= StringListField()
    receptors = StringListField()



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
