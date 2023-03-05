from fastapi import FastAPI
from fastapi import APIRouter
from google.oauth2 import id_token
from google.auth.transport import requests
from fastapi.exceptions import HTTPException


router = APIRouter(
    prefix="/auth",
    tags = ["authentication"],
)


@router.post('/verify-token')
def verify_token(token: str):
    CLIENT_ID = '548719013779-6ed69uc3bi9bnl2okehar88279vd8j61.apps.googleusercontent.com'

    try:
        # Verifica la validez del token.
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        # Verifica que el token sea emitido para el mismo proyecto y cliente que se espera.
        if idinfo['aud'] != CLIENT_ID:
            raise HTTPException(status_code=401, detail='Token de autenticación inválido.')
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise HTTPException(status_code=401, detail='Token de autenticación inválido.')

        # Si el token es válido, se devuelve un mensaje de éxito.
        return {'success': True, 'message': 'Token de autenticación válido.'}
    except ValueError as error:
        raise HTTPException(status_code=401, detail='Token de autenticación inválido: ' + str(error))