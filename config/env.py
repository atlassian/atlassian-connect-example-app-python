from flask_ngrok2 import run_with_ngrok
from dotenv import load_dotenv
import os

load_dotenv(".env")

def env_check(*required_env_vars):
    compare_env_vars = set(required_env_vars).difference(os.environ)

    if (len(compare_env_vars)):
        missing_env_vars = ', '.join(map(str, compare_env_vars))
        raise Exception('Missing required Environment Variables: ', missing_env_vars)

env_check('APP_URL', 'NGROK_AUTHTOKEN')

def run_with_env(app):
    run_with_ngrok(app, os.environ)
