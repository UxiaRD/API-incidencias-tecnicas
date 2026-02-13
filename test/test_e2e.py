from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_fetch_urgent_incidencia():
    # 1. Test POST: Crear una incidencia alta y abierta
    nueva_incidencia = {
        "descripcion": "Fallo crítico en servidor",
        "prioridad": "alta",
        "estado": "abierta"
    }
    response_post = client.post("/incidencias", json=nueva_incidencia)
    
    assert response_post.status_code == 201
    data = response_post.json()
    assert data["descripcion"] == "Fallo crítico en servidor"
    assert "id" in data

    # 2. Test GET especial: Recuperar incidencias urgentes
    response_get = client.get("/incidencias/urgentes")
    
    assert response_get.status_code == 200
    urgentes = response_get.json()
    assert len(urgentes) >= 1
    assert urgentes[-1]["prioridad"] == "alta"
    assert urgentes[-1]["estado"] == "abierta"

def test_get_all_incidencias():
    response = client.get("/incidencias")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_cerrar_incidencia():
    # Usamos la ID 1 que creamos en los datos de prueba del main
    response = client.patch("/incidencias/1/cerrar")
    assert response.status_code == 200
    assert response.json()["estado"] == "cerrada"

def test_obtener_incidencia_no_existente():
    response = client.get("/incidencias/999")
    assert response.status_code == 404