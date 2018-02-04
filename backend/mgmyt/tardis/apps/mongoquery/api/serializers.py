from rest_framework.serializers import ModelSerializer, SerializerMethodField
from tardis.apps.mongoquery.models import Collection, UserCollection, Job

class DynamicFieldsModelSerializer(ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class CollectionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Collection
        fields = ('collection_name','collection_description','collection_rowcount','collection_querylink')

class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ('query_text')
