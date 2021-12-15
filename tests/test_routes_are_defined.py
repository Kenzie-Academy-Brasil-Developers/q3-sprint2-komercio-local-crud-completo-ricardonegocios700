def test_route_products_exists(app_routes):
    assert app_routes.match("/products"), 'Verifique se existe uma rota "/products"'


def test_route_products_unique_exists(app_routes):
    assert app_routes.match(
        "/products/4"
    ), 'Verifique se existe uma rota "/products/<id>"'
