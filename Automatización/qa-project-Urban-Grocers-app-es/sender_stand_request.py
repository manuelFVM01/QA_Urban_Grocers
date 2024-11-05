#importamos
import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_USER_PATH,
                         json=body, #cuerpo de la solicitud
                         headers=data.headers #encabezado de la solicitud
                         )


def post_new_token():
    response=post_new_user(data.user_body)
    auth_token=response.json()
    return auth_token['authToken']


def post_personal_kit(kit_body):
    auth_token= post_new_token()
    headers2 = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {auth_token}'
    }
    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers2
                         )