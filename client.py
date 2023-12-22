import asyncio
import websockets
import os
import time


async def hello():
    try:
        uri = "ws://localhost:8765"
        async with websockets.connect(uri=uri) as websocket:
            name = input("what is  your name?: ")
            await websocket.send(name)
            while True:
                try:
                    message = await websocket.recv()
                    if message:
                        print(message)
                    msg = input("> ")
                    if msg == "q".upper():
                        websocket.send(msg)
                        print("Quiting -----")
                        time.sleep(5)
                        os.system("cls")
                        break
                    await websocket.send(msg)
                except Exception as exc:
                    print("something went wrong")
                    break
    except Exception as ex:
        print("couldn't find the server")
        print("quiting -------")



if __name__ == "__main__":
    asyncio.run(hello())