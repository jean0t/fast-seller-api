from fastapi import FastAPI
from routers import clients, products, auth, orders


class App:
    """
    Class responsible to hold the highest abstraction of the API
    the app and routes are contained here.
    """

    def __init__(self):
        self.app = FastAPI()
        self.register_routes()

    def clients_routes(self):
        self.app.include_router(clients.router)

    def products_routes(self):
        self.app.include_router(products.router)

    def orders_routes(self):
        self.app.include_router(orders.router)

    def auth_routes(self):
        self.app.include_router(auth.router)

    def register_routes(self):
        self.clients_routes()
        self.products_routes()
        self.orders_routes()
        self.auth_routes()
