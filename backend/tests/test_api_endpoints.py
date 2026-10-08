def test_health_check(api_client):
    """Tests that the health check endpoint returns status 200 and HEALTHY status."""
    response = api_client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "HEALTHY"
    assert "version" in data