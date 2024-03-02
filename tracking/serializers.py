from rest_framework import serializers

from tracking.models import Post


class DynamicFieldsModelSerializerMixin(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)
        list_fields = fields.split(",")
        super(DynamicFieldsModelSerializerMixin, self).__init__(
            *args, **kwargs
        )
        if fields is not None:
            allowed = set(list_fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class PostSerializer(
    DynamicFieldsModelSerializerMixin, serializers.ModelSerializer
):
    class Meta:
        model = Post
        fields = "__all__"
