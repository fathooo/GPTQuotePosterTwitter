from dotenv import load_dotenv
import os

load_dotenv()

env_variables = [
    "twitter_api_key",
    "twitter_api_secret",
    "twitter_bearer_token",
    "twitter_access_token",
    "twitter_access_token_secret",
    "openai_token",
    "save_on_db",
    "db_username",
    "db_password",
    "db_databa_name",
    "db_host",
    "db_port",
    "db_engine"
]

ENVIRONMENTS = {}
for var_name in env_variables:
    env_value = os.getenv(var_name)
    if env_value is None:
        raise ValueError(f"La variable de entorno {var_name} no está definida.")
    elif env_value == "":
        raise ValueError(f"La variable de entorno {var_name} está definida pero no tiene ningún valor asignado.")
    else:
        ENVIRONMENTS[var_name] = env_value
        if env_value.lower() == "true":
            ENVIRONMENTS[var_name] = True
        elif env_value.lower() == "false":
            ENVIRONMENTS[var_name] = False