from rest_framework import serializers

from tracking.models import Post


# class DynamicFieldsModelSerializerMixin(serializers.ModelSerializer):
#     def __init__(self, *args: tuple, **kwargs: dict) -> None:
#         fields = kwargs.pop("fields", None)
#         if fields is not None:
#             list_fields = fields.split(",")
#         super(DynamicFieldsModelSerializerMixin, self).__init__(
#             *args, **kwargs
#         )
#         if fields is not None:
#             allowed = set(list_fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)


class DynamicFieldsModelSerializerMixin(serializers.ModelSerializer):
    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        fields = kwargs.pop("fields", None)
        if fields is not None:
            list_fields = set(fields.split(","))
            existing_fields = set(self.fields)
            for field_name in existing_fields - list_fields:
                self.fields.pop(field_name)
        super(DynamicFieldsModelSerializerMixin, self).__init__(
            *args, **kwargs
        )


class PostSerializer(
    DynamicFieldsModelSerializerMixin, serializers.ModelSerializer
):
    class Meta:
        model = Post
        fields = "__all__"


# pass fields in serializers without query params
# class DynamicFieldsModelSerializerMixin(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         fields = kwargs.pop('fields', None)
#         super(DynamicFieldsModelSerializerMixin, self).__init__(*args, **kwargs)
#         if fields is not None:
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)
