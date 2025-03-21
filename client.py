import time
import json
import asyncio
import websockets

commands = {
    "command.auth.Register": {"nickname": str, "email": str, "cryptoPWD": str},
    "command.building.Create": {"building_type": int, "name": str, "x": int, "y": int, "rotation": int},
    "command.building.GetBuildingInfo": {"buildingID": int},
    "command.building.GetBuildings": {},
    "command.chat.ChatToNPC": {"NPCID": int, "content": str},
    "command.config.GetBuildingsConfig": {},
    "command.config.GetEquipmentsConfig": {},
    "command.config.GetNPCsConfig": {},
    "command.map.GetMapScene": {},
    "command.map.GetMapTown": {},
    "command.map.Navigate": {"x": int, "y": int},
    "command.npc.Create": {"asset": str, "model": str, "memorySystem": str, "planSystem": str, "nickname": str,
                           "bio": str, "goal": str, "cash": int},
    "command.npc.GetNPCInfo": {"NPCID": int},
    "command.npc.GetNPCs": {},
    "command.player.GetPlayerInfo": {},
    "command.timetick.Tick": {},
}


async def listen_server(websocket):
    while True:
        msg = await websocket.recv()
        print(f"Received: {msg}")


async def send_input(websocket):
    # info = json.dumps({"uri": "command.auth.Register", "method": "POST", "data": {"nickname": "fisher", "email": "abc@def.com", "cryptoPWD": "WWW"}}, ensure_ascii=False, separators=(",", ":"))
    # await websocket.send(info)
    uid = "Player-10001"
    while True:
        data = dict()
        command_list = ",".join([x for x in commands.keys()])
        command = input(f"Enter command to send from: {command_list}")
        if command not in commands:
            print("command not in commands list")
            continue
        for key, func in commands[command].items():
            param = func(input(f"Enter param {key}: "))
            data[key] = param
        request = json.dumps({"uid": uid, "uri": command, "data": data, "method": "POST"}, ensure_ascii=False,
                             separators=(",", ":"))
        print(f"Send: {request}")
        await websocket.send(request)


async def ping(websocket):
    # info = json.dumps({"uri": "command.auth.Register", "method": "POST", "data": {"nickname": "fisher", "email": "abc@def.com", "cryptoPWD": "WWW"}}, ensure_ascii=False, separators=(",", ":"))
    # await websocket.send(info)
    uid = "Player-10001"
    while True:
        info = json.dumps({"uid": uid, "uri": "ping", "method": "GET", "data": {}}, ensure_ascii=False,
                          separators=(",", ":"))
        print(f"Send: {info}")
        await websocket.send(info)
        await asyncio.sleep(10)


async def debug(websocket, send_to_unity=True):
    # 模拟unity前端
    # register
    if not send_to_unity:
        info = json.dumps({"uri": "command.auth.Register", "method": "POST",
                           "data": {"nickname": "Lixing", "email": "Lixing@163.com", "cryptoPWD": "123456"}},
                          ensure_ascii=False, separators=(",", ":"))
        print(f"Send: {info}")
        await websocket.send(info)
        msg = await websocket.recv()
        print(f"Received: {msg}")
    uid = "Player-10001"

    # GetPlayerInfo
    # time.sleep(3)
    # get_player_info = json.dumps({"uid": uid, "uri": "command.player.GetPlayerInfo", "method": "POST", "data": {}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {get_player_info}")
    # await websocket.send(get_player_info)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # # GetBuildings
    # # time.sleep(3)
    # get_buildings = json.dumps({"uid": uid, "uri": "command.building.GetBuildings", "method": "POST", "data": {}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {get_buildings}")
    # await websocket.send(get_buildings)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # # GetBuildingInfo
    # # time.sleep(3)
    # building_id = 1
    # get_building_info = json.dumps({"uid": uid, "uri": "command.building.GetBuildingInfo", "method": "POST", "data": {"buildingID": building_id}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {get_building_info}")
    # await websocket.send(get_building_info)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # # GetBuildingsConfig
    # # time.sleep(3)
    # get_buildings_config = json.dumps({"uid": uid, "uri": "command.config.GetBuildingsConfig", "method": "POST", "data": {}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {get_buildings_config}")
    # await websocket.send(get_buildings_config)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # # GetEquipmentsConfig
    # # time.sleep(3)
    # get_equipments_config = json.dumps({"uid": uid, "uri": "command.config.GetEquipmentsConfig", "method": "POST", "data": {}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {get_equipments_config}")
    # await websocket.send(get_equipments_config)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # # GetNPCsConfig
    # # time.sleep(3)
    # get_npcs_config = json.dumps({"uid": uid, "uri": "command.config.GetNPCsConfig", "method": "POST", "data": {}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {get_npcs_config}")
    # await websocket.send(get_npcs_config)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # # GetMapScene
    # # time.sleep(3)
    # # GetMapTown
    # # time.sleep(3)
    # get_map_town = json.dumps({"uid": uid, "uri": "command.map.GetMapTown", "method": "POST", "data": {}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {get_map_town}")
    # await websocket.send(get_map_town)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # GetNPCs
    # time.sleep(3)
    # get_npcs = json.dumps({"uid": uid, "uri": "command.npc.GetNPCs", "method": "POST", "data": {}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {get_npcs}")
    # await websocket.send(get_npcs)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # # GetNPCInfo
    # # time.sleep(3)
    # npc_id = 10001
    # get_npc_info = json.dumps({"uid": uid, "uri": "command.npc.GetNPCInfo", "method": "POST", "data": {"NPCID": npc_id}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {get_npc_info}")
    # await websocket.send(get_npc_info)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # testName = "changeCash"
    # fake_sendings = json.dumps({"uid": uid, "uri": "command.gm.FakeSendings", "method": "POST", "data": {"testName": testName}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {fake_sendings}")
    # await websocket.send(fake_sendings)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # start_mayor = json.dumps({"uid": uid, "uri": "command.starter.MayorStarter", "method": "POST", "data": {}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {start_mayor}")
    # await websocket.send(start_mayor)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # await asyncio.sleep(10)
    # start_ticks = json.dumps({"uid": uid, "uri": "command.starter.TickStarter", "method": "POST", "data": {}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {start_ticks}")
    # await websocket.send(start_ticks)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # building.Create
    # time.sleep(3)
    # building_type = 3
    # building_name = "dessert shop"
    # building_x = 3
    # building_y = 1
    # building_rotation = 0
    # create_building = json.dumps({"uid": uid, "uri": "command.building.Create", "method": "POST", "data": {"building_type": building_type, "name": building_name, "x": building_x, "y": building_y, "rotation": building_rotation}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {create_building}")
    # await websocket.send(create_building)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")
    # building_type = 4
    # building_name = "gym"
    # building_x = 3
    # building_y = 2
    # building_rotation = 0
    # create_building = json.dumps({"uid": uid, "uri": "command.building.Create", "method": "POST", "data": {"building_type": building_type, "name": building_name, "x": building_x, "y": building_y, "rotation": building_rotation}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {create_building}")
    # await websocket.send(create_building)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")
    # building_type = 5
    # building_name = "houseZ"
    # building_x = 3
    # building_y = 4
    # building_rotation = 0
    # create_building = json.dumps({"uid": uid, "uri": "command.building.Create", "method": "POST", "data": {"building_type": building_type, "name": building_name, "x": building_x, "y": building_y, "rotation": building_rotation}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {create_building}")
    # await websocket.send(create_building)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")
    # building_type = 6
    # building_name = "park"
    # building_x = 4
    # building_y = 2
    # building_rotation = 0
    # create_building = json.dumps({"uid": uid, "uri": "command.building.Create", "method": "POST", "data": {"building_type": building_type, "name": building_name, "x": building_x, "y": building_y, "rotation": building_rotation}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {create_building}")
    # await websocket.send(create_building)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")
    # building_type = 10
    # building_name = "houseA"
    # building_x = 2
    # building_y = 3
    # building_rotation = 0
    # create_building = json.dumps({"uid": uid, "uri": "command.building.Create", "method": "POST", "data": {"building_type": building_type, "name": building_name, "x": building_x, "y": building_y, "rotation": building_rotation}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {create_building}")
    # await websocket.send(create_building)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")
    # get_map_scene = json.dumps({"uid": uid, "uri": "command.map.GetMapScene", "method": "POST", "data": {}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {get_map_scene}")
    # await websocket.send(get_map_scene)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # npc.Create
    # time.sleep(3)
    # npc_asset = "premade_01"
    # npc_model = "gpt-3.5"
    # npc_memory = "LongShortTermMemories"
    # npc_plan = "QAFramework"
    # npc_home = 3
    # npc_work = 5
    # npc_nickname = "Alan"
    # npc_bio = "Alan is a genius with outstanding talents and the inventor of computers. Allen has an introverted personality and is only interested in the research he focuses on."
    # npc_goal = "Allen is committed to conducting more work and research."
    # npc_cash = 10000
    # create_npc = json.dumps({"uid": uid, "uri": "command.npc.Create", "method": "POST", "data": {"asset": npc_asset, "model": npc_model, "memorySystem": npc_memory, "planSystem": npc_plan, "homeBuilding": npc_home, "workBuilding": npc_work, "nickname": npc_nickname, "bio": npc_bio, "goal": npc_goal, "cash": npc_cash}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {create_npc}")
    # await websocket.send(create_npc)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")
    # npc_asset = "premade_04"
    # npc_model = "gpt-3.5"
    # npc_memory = "LongShortTermMemories"
    # npc_plan = "QAFramework"
    # npc_home = 3
    # npc_work = 5
    # npc_nickname = "Fei"
    # npc_bio = "Fei is a talented researcher with a research focus on artificial intelligence. As a university professor, she has a passion for open research in the field of artificial intelligence."
    # npc_goal = "Share with others the progress in the field of artificial intelligence, as well as helping others and answering their questions."
    # npc_cash = 10000
    # create_npc = json.dumps({"uid": uid, "uri": "command.npc.Create", "method": "POST", "data": {"asset": npc_asset, "model": npc_model, "memorySystem": npc_memory, "planSystem": npc_plan, "homeBuilding": npc_home, "workBuilding": npc_work, "nickname": npc_nickname, "bio": npc_bio, "goal": npc_goal, "cash": npc_cash}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {create_npc}")
    # await websocket.send(create_npc)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # Navigate
    # time.sleep(3)
    # content = "Hi, how do you feel about the town?"
    # target_x = 91
    # target_y = 70
    # navigate = json.dumps({"uid": uid, "uri": "command.map.Navigate", "method": "POST", "data": {"x": target_x, "y": target_y}}, ensure_ascii=False, separators=(",", ":"))
    # print(f"Send: {navigate}")
    # await websocket.send(navigate)
    # msg = await websocket.recv()
    # print(f"Received: {msg}")

    # # ChatToNPC
    time.sleep(3)
    npc_id = 10002
    content = "Hi, how do you feel about the town?"
    chat = json.dumps({"uid": uid, "uri": "command.chat.ChatWithNPC", "method": "POST",
                       "data": {"NPCID": f"NPC-{npc_id}", "content": content}}, ensure_ascii=False,
                      separators=(",", ":"))
    print(f"Send: {chat}")
    await websocket.send(chat)
    msg = await websocket.recv()
    print(f"Received: {msg}")
    server_task = asyncio.create_task(listen_server(websocket))
    await server_task

    # sending message to Player-10001: {"code":200,"uri":"chatWith","uid":"NPC-10002","data":{"sourceID":"NPC-10002","targetID":"Player-10001","content":"Hi Mayor! I love the town, especially the dessert shop. Have you tried their pastries? They're amazing!"}}

    # sending message to Player-10001: {"code":200,"uri":"movePath","uid":"NPC-10003","data":{"uid":"NPC-10003","path":[{"x":52,"y":72},{"x":52,"y":73},{"x":52,"y":74},{"x":52,"y":75},{"x":52,"y":76},{"x":52,"y":77},{"x":53,"y":77},{"x":54,"y":77},{"x":55,"y":77},{"x":56,"y":77},{"x":57,"y":77},{"x":58,"y":77},{"x":59,"y":77},{"x":60,"y":77},{"x":61,"y":77},{"x":62,"y":77},{"x":63,"y":77},{"x":64,"y":77},{"x":65,"y":77},{"x":66,"y":77},{"x":67,"y":77},{"x":68,"y":77},{"x":69,"y":77},{"x":70,"y":77},{"x":71,"y":77},{"x":72,"y":77},{"x":73,"y":77},{"x":74,"y":77},{"x":75,"y":77},{"x":76,"y":77},{"x":77,"y":77},{"x":78,"y":77},{"x":79,"y":77},{"x":79,"y":76},{"x":79,"y":75},{"x":79,"y":74},{"x":79,"y":73},{"x":79,"y":72},{"x":79,"y":71},{"x":79,"y":70},{"x":79,"y":69},{"x":79,"y":68},{"x":79,"y":67},{"x":79,"y":66},{"x":79,"y":65},{"x":79,"y":64},{"x":79,"y":63},{"x":79,"y":62},{"x":79,"y":61},{"x":79,"y":60},{"x":79,"y":59},{"x":79,"y":58},{"x":79,"y":57},{"x":79,"y":56},{"x":79,"y":55},{"x":79,"y":54},{"x":79,"y":53},{"x":79,"y":52},{"x":79,"y":51},{"x":79,"y":50},{"x":79,"y":49},{"x":79,"y":48},{"x":79,"y":47},{"x":79,"y":46},{"x":79,"y":45},{"x":79,"y":44},{"x":79,"y":43},{"x":79,"y":42},{"x":79,"y":41},{"x":79,"y":40},{"x":79,"y":39},{"x":79,"y":38},{"x":79,"y":37},{"x":79,"y":36},{"x":79,"y":35},{"x":79,"y":34},{"x":79,"y":33},{"x":79,"y":32},{"x":79,"y":31},{"x":79,"y":30},{"x":79,"y":29},{"x":79,"y":28},{"x":79,"y":27},{"x":79,"y":26},{"x":79,"y":25},{"x":79,"y":24},{"x":79,"y":23},{"x":79,"y":22},{"x":80,"y":22},{"x":81,"y":22},{"x":82,"y":22},{"x":83,"y":22},{"x":84,"y":22},{"x":85,"y":22},{"x":85,"y":21},{"x":85,"y":20},{"x":85,"y":19},{"x":85,"y":18},{"x":85,"y":17},{"x":85,"y":16},{"x":85,"y":15},{"x":86,"y":15},{"x":86,"y":14},{"x":86,"y":13},{"x":86,"y":12},{"x":87,"y":12},{"x":88,"y":12},{"x":89,"y":12}]}}



async def main():
    async with websockets.connect("ws://localhost:8000/ws", ping_interval=None) as websocket:
        msg = await websocket.recv()
        print(f"Received: {msg}")
        # server_task = asyncio.create_task(listen_server(websocket))
        debug_task = asyncio.create_task(debug(websocket, send_to_unity=True))
        # input_task = asyncio.create_task(send_input(websocket))
        ping_task = asyncio.create_task(ping(websocket))

        # await server_task
        await debug_task
        # await input_task
        await ping_task


asyncio.run(main())