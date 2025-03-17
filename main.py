import tornado.ioloop
# import tornado.web
import tornado.websocket
import subprocess


def set_start_state(file_path):
    import json
    # 读取JSON文件
    with open(file_path, 'r') as file:
        data = json.load(file)
    # 修改数值
    data["tick_state"]["start"] = False
    # 保存回去
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    # set_start_state('/Users/wangkai/GitHub/AgentSims/snapshot/app.json')

    from app import App

    class WebSocketHandler(tornado.websocket.WebSocketHandler):
        app_cache = App()
        ping_interval = 0

        def check_origin(self,remote_address):
            # CORS
            return True

        def open(self):
            self.app_cache.register(self)

        def on_close(self):
            # print("connection closing")
            self.app_cache.logout(self)

        async def on_message(self, message):
            await self.app_cache.execute(self, message)


    class Application(tornado.web.Application):
        def __init__(self):
            handlers = [
                (r'/ws', WebSocketHandler),
            ]
            tornado.web.Application.__init__(self, handlers, websocket_ping_interval=0)
    print("----------Server Started----------")
    app = Application()
    app.listen(8000, address='0.0.0.0')
    # subprocess.call("python3 -u tick.py")
    # "tick_state":{"start_time":1730357154746,"tick_count":0,"start":true}
    tornado.ioloop.IOLoop.current().start()
    print("----------Server Stopped----------")
