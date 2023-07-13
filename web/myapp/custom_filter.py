from django import template
import base64

register = template.Library()

@register.filter
def get_attribute(obj, attr_name):
    return getattr(obj, attr_name)

@register.filter
def encode_id(id):
    salt = "dict"
    encoded_string = base64.b64encode(f"{salt}{id}".encode('utf-8')).decode('utf-8')[:10]
    return encoded_string