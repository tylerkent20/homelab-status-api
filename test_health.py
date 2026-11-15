from app import app


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "healthy"
    

def test_version_endpoint():
    client = app.test_client()

    response = client.get("/api/version")
    data = response.get_json()

    assert response.status_code == 200
    assert data["application"] == "homelab-status-api"
    assert data["version"] == "1.1.0"