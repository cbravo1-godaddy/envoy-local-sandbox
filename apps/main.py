from typing import Optional
from fastapi import FastAPI, Request, Response
import argparse
import logging
import uvicorn


def get_app(app_value):
    # Fast API
    app = FastAPI()
    logger = logging.getLogger(__name__)

    @app.get("/v1/{sub_path:path}")
    def read_root_v1(
        request: Request,
        sub_path: str,
    ):
        x_dsa_host = request.headers.get("x-dsa-host")
        x_dsa_path = request.headers.get("x-dsa-path")
        x_dsa_originalip = request.headers.get("x-dsa-originalip")

        # Print the header value
        print(f"x-dsa-host: {x_dsa_host}")
        print(f"x-dsa-path: {x_dsa_path}")
        print(x_dsa_originalip)

        return {
            "Hello": f"World from app v1 - {app_value}, req-host: {x_dsa_host}, req-path: v1/{sub_path}, x-dsa-path: {x_dsa_path}"
        }

    @app.get("/v2/{sub_path:path}")
    def read_root_v2(request: Request, sub_path: str, contextState: Optional[str]):
        x_dsa_host = request.headers.get("x-dsa-host")
        x_dsa_path = request.headers.get("x-dsa-path")
        x_dsa_originalip = request.headers.get("x-dsa-originalip")

        # Print the header value
        params = request.query_params
        print(params["contextState"])
        print(contextState)
        print(f"x-dsa-host: {x_dsa_host}")
        print(f"x-dsa-path: {x_dsa_path}")
        print(x_dsa_originalip)

        return {
            "Hello": f"World from app v1 - {app_value}, req-host: {x_dsa_host}, req-path: v1/{sub_path}, x-dsa-path: {x_dsa_path}"
        }

    @app.get("/healthcheck.html")
    def read_root(request: Request):
        x_dsa_host = request.headers.get("x-dsa-host")
        x_dsa_path = request.headers.get("x-dsa-path")

        # Print the header value
        print("healthcheck: {x_dsa_path}")

        return {"Health": f"app is ok {app_value}, req-host: {x_dsa_path}"}

    @app.get("/swagger/{sub_path:path}")
    def swagger(request: Request, sub_path: str, response: Response):
        x_dsa_host = request.headers.get("x-dsa-host")
        x_dsa_path = request.headers.get("x-dsa-path")

        # Print the header value
        x_dsa_host = request.headers.get("x-dsa-host")
        x_dsa_path = request.headers.get("x-dsa-path")

        # Print the header value
        print(f"swagger x-dsa-host: {x_dsa_host}")
        print(f"swagger x-dsa-path: {x_dsa_path}")

        response.headers["X-Cat-Dog"] = "alone in the world"
        return {
            "Swagger": f"App {app_value}, req-host: {x_dsa_host}, req-path: swagger/{sub_path}, x-dsa-path: {x_dsa_path}"
        }

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

    @app.get("/")
    def read_root(request: Request):

        return {"Hello": f"World from app default path"}

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
