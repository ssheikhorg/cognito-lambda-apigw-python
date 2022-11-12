from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute, BooleanAttribute,
    MapAttribute, ListAttribute, BinaryAttribute, JSONAttribute
)
from ..core.configs import settings as c


class ResellerModel(Model):
    class Meta:
        table_name = c.dynamodb_table_name
        region = c.aws_default_region
        aws_access_key_id = c.aws_access_key
        aws_secret_access_key = c.aws_secret_key

    pk = UnicodeAttribute(hash_key=True)  # email
    sk = NumberAttribute(range_key=True)  # quota
    password = UnicodeAttribute()
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute()
    user_enabled = BooleanAttribute()
