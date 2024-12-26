KEYCLOAK_URL = "http://localhost:8081/realms/learner/protocol/openid-connect/token"
KEYCLOAK_CLIENT_ID = "learn"
KEYCLOAK_CLIENT_SECRET = "flmelfd.fdfdfde"
KEYCLOAK_USERNAME = "johndoe@gmail.com"
KEYCLOAK_PASSWORD = "abcd1234"
KEYCLOAK_GRANT_TYPE = "password"

# Common or critical endpoints
CRITICAL_ENDPOINT = "/api/v1/question"

# List of all other endpoints
API_ENDPOINTS = [
    "/api/v1/user",
    # ... add all other endpoints ...
]
