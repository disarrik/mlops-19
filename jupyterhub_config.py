from os import environ

c.JupyterHub.proxy_auth_token = environ.get("CONFIGPROXY_AUTH_TOKEN", "secret-token-change-me")

c.JupyterHub.cookie_secret = environ.get(
    "JUPYTERHUB_COOKIE_SECRET",
    "0000000000000000000000000000000000000000000000000000000000000000",
).encode()

c.JupyterHub.authenticator_class = "jupyterhub.auth.DummyAuthenticator"

c.Authenticator.admin_users = {"admin"}

c.JupyterHub.spawner_class = "jupyterhub.spawner.SimpleLocalProcessSpawner"

c.JupyterHub.hub_bind_url = "http://0.0.0.0:8081"
c.JupyterHub.hub_connect_url = "http://127.0.0.1:8081"
