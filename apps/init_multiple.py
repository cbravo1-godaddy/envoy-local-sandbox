##
## How to run multiple uvicorn server apps in the same process
## asyncio:
## https://github.com/encode/uvicorn/issues/541
## https://stackoverflow.com/questions/76142431/how-to-run-another-application-within-the-same-running-event-loop
## multiprocess: https://blog.stackademic.com/advanced-guide-to-asyncio-threading-and-multiprocessing-in-python-c4dc50971d24
##
import multiprocessing
from main import start_server


# Run the other script
configList = [
    {"value": 1, "port": 1111}, 
    {"value": 2, "port": 2222},
    {"value": 3, "port": 3333},
    {"value": 4, "port": 4444}
]

if __name__ == '__main__':
    processes = []
    try:
        for cfg in configList:
            app_value = cfg["value"]
            app_port= cfg["port"]
            process = multiprocessing.Process(target=start_server, args=(app_value, app_port))
            processes.append(process)
            process.start()
    except KeyboardInterrupt as k:
        print(f"KKeyboard interrumpt received | Stopping FastAPI application: {k}")

