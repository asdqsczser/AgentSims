import json
import time
import sys
import asyncio
import websockets

count_limit = 1
args = sys.argv
print(args)
if len(args) > 1:
    count_limit = int(args[1])

async def listen_server(websocket):
    while True:
        msg = await websocket.recv()
        print(f"listen_server Received: {msg}")

async def ping(websocket):
    # info = json.dumps({"uri": "command.auth.Register", "method": "POST", "data": {"nickname": "fisher", "email": "abc@def.com", "cryptoPWD": "WWW"}}, ensure_ascii=False, separators=(",", ":"))
    # await websocket.send(info)
    uid = "tick-10001"
    while True:
        info = json.dumps({"uid": uid, "uri": "ping", "method": "GET", "data": {}}, ensure_ascii=False, separators=(",", ":"))
        result = await websocket.send(info)
        print(f"Send ping: {info} {result}")
        await asyncio.sleep(10)


async def call_timetick_move(websocket):
    uid = "tick-10001"
    call = json.dumps({"uid": uid, "uri": "command.timetick.TickMove", "method": "POST"}, ensure_ascii=False, separators=(",", ":"))
    # sendings = list()
    counter = 0
    while True:
        sending = asyncio.create_task(websocket.send(call))
        # receive = await websocket.recv()
        await asyncio.sleep(1)
        await sending
        print(f"Sending: {call} count_limit:{count_limit} counter:{counter}")
        counter += 1
        if count_limit and count_limit <= counter:
            raise ValueError("Stop tick")


async def call_timetick(websocket):
    uid = "tick-10001"
    call = json.dumps({"uid": uid, "uri": "command.timetick.Tick", "method": "POST"}, ensure_ascii=False, separators=(",", ":"))
    # sendings = list()
    counter = 0
    while True:
        sending = asyncio.create_task(websocket.send(call))
        # receive = await websocket.recv()
        await asyncio.sleep(5)
        await sending
        print(f"Sending: {call} count_limit:{count_limit} counter:{counter}")
        counter += 1
        if count_limit and count_limit <= counter:
            raise ValueError("Stop tick")
    # for sending in sendings:
    #     await sending

async def main():
    async with websockets.connect("ws://localhost:8000/ws", ping_interval=None) as websocket:
        timer_task = asyncio.create_task(call_timetick(websocket))
        # timer_move_task = asyncio.create_task(call_timetick_move(websocket))
        ping_task = asyncio.create_task(ping(websocket))
        server_task = asyncio.create_task(listen_server(websocket))

        # from app import App
        # from command.timetick.Tick import Tick
        # app_cache = App()
        # tick_cls = Tick(app_cache)
        # movings = tick_cls.app.movings
        # moves = list()
        # print("before solving movings:", movings)
        # for moving in movings:
        #     move_task = asyncio.create_task(tick_cls.solve_moving(moving))
        #     moves.append(move_task)

        await server_task
        await timer_task
        # await timer_move_task
        await ping_task

        # try:
        #     await timer_task
        # except Exception as e:
        #     print(f"An exception occurred: {e}")
        # finally:
        #     for task in [ping_task, server_task]:
        #         if not task.done():
        #             task.cancel()
        #     await asyncio.gather(*[timer_task, ping_task, server_task], return_exceptions=True)
        #     print("All tasks done")

asyncio.run(main())