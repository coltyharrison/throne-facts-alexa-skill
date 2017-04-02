from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute
)


class ThroneFacts(Model):
    class Meta:
        table_name = 'ThroneFacts'

    amazon_id = UnicodeAttribute(hash_key=True)
    house = UnicodeAttribute(default="None")
    num_correct = NumberAttribute(default=0)
    num_total = NumberAttribute(default=0)
    score = NumberAttribute(default=0)
