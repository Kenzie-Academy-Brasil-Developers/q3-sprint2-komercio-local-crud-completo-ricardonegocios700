from flask.testing import FlaskClient


def test_route_list_all_status(client: FlaskClient):
    response = client.get("/products")
    assert response.status_code == 200


def test_route_create_status(client: FlaskClient):
    response = client.post(
        "/products", json={"name": "Esponja do Bob Esponja", "price": 5.5}
    )
    assert response.status_code == 201


def test_route_get_status(client: FlaskClient):
    response = client.get("/products/1")
    assert response.status_code == 200


def test_route_update_status(client: FlaskClient):
    response = client.patch("/products/1", json={"name": "Batman"})
    assert response.status_code == 204


def test_route_delete_status(client: FlaskClient):
    response = client.delete("/products/1")
    assert response.status_code == 204
