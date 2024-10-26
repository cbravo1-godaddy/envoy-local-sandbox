from fastapi import FastAPI, Request
import argparse
import logging
import uvicorn


def get_app(app_value):
    # Fast API
    app = FastAPI()
    logger = logging.getLogger(__name__)

    @app.get("/")
    def read_root(request: Request):
        x_dsa_host = request.headers.get("x-dsa-host")

        # Print the header value
        print(f"x-dsa-host: {x_dsa_host}")

        return {"Hello": f"World from app {app_value}, x-dsa-host: {x_dsa_host}"}

    @app.get("/static/homepage")
    def get_static_homepage():
        logger.info(f"request / endpoint!")
        return {"Homepage": f"Getting homepage from app {app_value}"}

    @app.get("/static/{static_path_asset}")
    def get_static_asset(static_path_asset):
        return {"static asset": static_path_asset}

    @app.get("/admin")
    def get_admin():
        return {"adminState": True}

    return app


def start_server(app_value, app_port):
    app = get_app(app_value)
    config = uvicorn.Config(app, port=app_port, reload=True)
    server = uvicorn.Server(config)
    server.run()


# Running programmatically - https://www.uvicorn.org/#running-programmatically
if __name__ == "__main__":
    # CLI arg parser
    parser = argparse.ArgumentParser(description="Init a single app")
    parser.add_argument("--appNumber", type=int, help="App number")
    parser.add_argument("--port", type=int, help="Server app port")
    args = parser.parse_args()
    app_value = args.appNumber
    app_port = args.port
    start_server(app_value, app_port)
