import asyncio
import websockets
import os


async def hello(websocket):
    name = await websocket.recv()
    print(f"{name} joined the chat")
    greeting = f"hello {name}"

    await websocket.send(greeting)
    while True:
        try:
            msg = await websocket.recv()
            if msg == "q".upper():
                print(f"{name} left the chat!")
                os.system("cls")
                break
            print(msg)
            messge = input("> ")
            await websocket.send(messge)
        except Exception as ex:
            print("something went wrong")
            break


async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())