from django import template
from cryptography.fernet import Fernet
register = template.Library()

@register.filter
def get_attribute(obj, attr_name):
    return getattr(obj, attr_name)

@register.filter
def encode_id(id):
    key = Fernet(b'v06isf7eUcEMAhUnM6bZsMVO0puqpoxNvT90MSMhXSs=')
    encrypted_message = key.encrypt(str(id).encode())
    return encrypted_message.decode()