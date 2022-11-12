from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute, BooleanAttribute,
    MapAttribute, ListAttribute, BinaryAttribute, JSONAttribute
)
from ..core.configs import settings as c


class CognitoModel(Model):
    class Meta:
        table_name = c.dynamodb_table_name
        region = c.aws_default_region

    pk = UnicodeAttribute(hash_key=True)  # email
    sk = UnicodeAttribute(range_key=True)  # role
    password = UnicodeAttribute()
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute(null=True)
    phone_number = UnicodeAttribute(null=True)
    created_at = UnicodeAttribute()
    user_id = UnicodeAttribute(null=True)
    user_confirmed = BooleanAttribute()
    company = UnicodeAttribute(null=True)
    agreement = BooleanAttribute(null=True)
