from django.core.serializers.json import DjangoJSONEncoder
from dbModel.models import picModel

class picModelEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, picModel):
            return "ahahahahah"
        return super().default(obj)