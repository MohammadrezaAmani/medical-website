from rest_framework_jwt.utils import jwt_get_username_from_payload_handler


def jwt_get_username_from_payload_handler(payload):
    # Add your custom logic to get the username from the payload
    return payload.get("username")
