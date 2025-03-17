# AgentSims: An Open-Source Sandbox for Large Language Model Evaluation
## Setup Instructions
```
1. git clone; Check config/app.json and config/api_key.json
2. Run preprocess_before_start.py
3. Start the backend server with ./restart.sh
4. Open the browser to http://xxxx:xxxx/client/index.html
5. Logs are stored in nohup.log
```

## Code Framework Overview
```
1. ./restart.sh starts main.py
2. The browser loads index.html, which is the Unity frontend, and sends {"uri":"command.auth.Register","method":"POST","data":{"nickname":"Mayor","email":"Lixing@163.com","cryptoPWD":"123456"}} to the backend
3. The on_message function in main.py receives the message and calls the execute method of the Register Class in the command.auth.Register folder
4. command.auth.login_base initializes NPCs and the map
5. When the tick button is clicked on the web frontend, {"uri":"command.tick.Tick","method":"POST","data":{}} is sent to the backend. Similarly, the backend calls the execute method of the TickStarter Class in the command.starter.TickStarter folder
6. TickStarter actually invokes tick.py in the project directory. The asyncio.create_task(call_timetick(websocket)) sends a message to the backend to start command/timetick/Tick.py
7. Tick-related configurations are detailed in config/app.json. For example, setting tick_count_limit=1 and manually running tick.py allows for step-by-step debugging
8. command/timetick/Tick.py contains the main logic for the agent. It is somewhat complex and can be refactored in the future to add custom logic such as TickChat, TickMove, etc.
9. The tick program and backend, as well as the frontend and backend, communicate through port 8000 (fixed). We mainly focus on frontend-backend communication. For example, websocket.send() at line 42 in command/timetick/Tick.py sends a message to the frontend to trigger character movement.
10. Backend data is persisted in both snapshot/app.json and a MySQL database.
11. Note that NPCs have states. Initially, they are in the "inited" state, and after the first tick, they transition to the "movings" state. Sometimes, if an NPC is not in the "movings" state, it won't execute the "movings" logic.
"inited":[],"movings":["NPC-10002"],"chatted":[],"using":["NPC-10001","NPC-10002"],"cache":[]
```


## 开启方法

```
1.git clone; 检查config/app.json和config/api_key.json
2.运行preprocess_before_start.py
3. 运行后端服务器 ./restart.sh
4.浏览器打开 http://xxxx:xxxx/client/index.html
5.日志文件在 nohup.log
``` 

## 代码框架学习
```
1. ./restart.sh启动了main.py
2. 浏览器index.html，即unity前端，发送 {"uri":"command.auth.Register","method":"POST","data":{"nickname":"Mayor","email":"Lixing@163.com","cryptoPWD":"123456"}} 到后端
3. main.py中的on_message函数接收到消息后，调用command.auth.Register文件夹下的Register Class的execute方法
4. command.auth.login_base对NPC和地图进行了初始化
5. 我们在网页前端中点击了tick按钮，发送了{"uri":"command.tick.Tick","method":"POST","data":{}}到后端，类似的, 后端开始调用command.starter.TickStarter文件夹下的TickStarter Class的execute方法
6. TickStarter实际上是调用了项目路径下的tick.py，其中asyncio.create_task(call_timetick(websocket))会发消息给后端来启动command/timetick/Tick.py
7. tick相关配置详见config/app.json，如设置tick_count_limit=1, 并手动运行tick.py可以实现单步调试
8. command/timetick/Tick.py是agent的主要逻辑，写的有点复杂，后续可以分拆逻辑，添加自己的逻辑如TickChat、TickMove等
9. tick程序和后端、前端和后端 都通过8000端口(固定)通讯。我们主要看前后端通讯，如command/timetick/Tick.py:42行的websocket.send()发送消息到前端，调用前端的人物移动。
10. 后端的数据同时持久化在snapshot/app.json 和 mysql数据库中。
11. 注意NPC是有状态的，一开始是inited状态，第一个tick后变成movings状态，有时候NPC不在movings状态就不会走movings逻辑。
"inited":[],"movings":["NPC-10002"],"chatted":[],"using":["NPC-10001","NPC-10002"],"cache":[]
``` 



How to evaluate the ability of large language models (LLM) is an open question after ChatGPT-like LLMs prevailing the community. Existing evaluation methods suffer from following shortcomings: (1) constrained evaluation abilities, (2) vulnerable benchmarks, (3) unobjective metrics. We suggest that task-based evaluation, where LLM agents complete tasks in a simulated environment, is a one-for-all solution to solve above problems. 

We present <a href="https://www.agentsims.com/" title="AgentSims">AgentSims</a>, an easy-to-use infrastructure for researchers from all disciplines to test the specific capacities they are interested in. Researchers can build their evaluation tasks by adding agents and buildings on an interactive GUI or deploy and test new support mechanisms, i.e. memory system and planning system, by a few lines of codes.  The demonstration is on https://agentsims.com/.

***Our system has better customization capabilities compared to other similar systems, as it is designed for open source custom task building. See our <a href="https://arxiv.org/abs/2308.04026" title="arXiv">arXiv paper</a>.*** 

![Image text](https://github.com/py499372727/AgentSims/blob/main/cover.png)

## Dependency
```
Python: 3.9.x
MySQL: 8.0.31
```
We recommend deploying on MacOS or Linux for better stability.

## API Key
For the security of your API Key, we have not included the parameter file in git. Please create the following file
```
config/api_key.json
``` 
yourself and remember not to push it to git.

The file parameter example is:
```
{"gpt-4": "xxxx", "gpt-3.5": "xxxx"}
``` 
If you want to deploy your own model, see <a href="https://github.com/py499372727/AgentSims/wiki" title="DOCS">DOCS</a>.

## Folder Creation
Before running, please
```
mkdir snapshot
mkdir logs
```
In addition, we recommend modifying the ***count_limit*** (number of loops per run) and ***cooldown*** (cooldown time between runs) in ***config/app.json*** to suitable values before running, in order to balance protection of your API key and experiment runtime efficiency.

If you encounter any issues during runtime, please first refer to our <a href="https://github.com/py499372727/AgentSims/wiki" title="DOCS">DOCS</a> in the wiki. If not resolved, please raise an issue or contact us directly.

--------------------------------------
To use our system, please follow these steps:

## 1.MySQL Init
MySQL is used for data storage on the server. After installing the appropriate version of MySQL, start the SQL service and initialize it as follows:
```
use mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
flush privileges;

create database `llm_account` default character set utf8mb4 collate utf8mb4_unicode_ci;
create database `llm_game` default character set utf8mb4 collate utf8mb4_unicode_ci;
create database `llm_game0001` default character set utf8mb4 collate utf8mb4_unicode_ci;
create database `llm_game0002` default character set utf8mb4 collate utf8mb4_unicode_ci;
```

## 2.Install

```bash
pip install tornado
pip install mysql-connector-python
pip install websockets
pip install openai_async
```

or
```bash
pip install -r requirements.txt
```
## 3.Design Tasks
You can build tasks at this point. If you just want to try out the system first, you can skip this step. For task building, please refer to the <a href="https://github.com/py499372727/AgentSims/wiki" title="DOCS">DOCS</a> in the wiki or Section 4.2 Developer Mode in our <a href="https://arxiv.org/abs/2308.04026" title="arXiv">arXiv paper</a>.

## 4.Run Server

Start server:
```bash
./restart.sh
```
When you see
```
--------Server Started--------
```
in Server Terminal, the server has been started successfully.
## 5.Run Client
Once the server has started successfully, please launch the client. In the current version, we provide a web-based client. Please open ***client/index.html*** in your browser.

Note: Sometimes the web client fails to open correctly. We recommend right-clicking the ***index.html*** in your python IDE and select ***open in browser***. If you are familiar with ***nginx***, that is also a great choice. 

When you see
```
somebody linked.
```
in Server Terminal, the client has been started successfully.

## 6.Create agents and buildings
You can create agents and buildings at this point. For creation, please refer to the <a href="https://github.com/py499372727/AgentSims/wiki" title="DOCS">DOCS</a> in the wiki or Section 4.1 User Mode in our <a href="https://arxiv.org/abs/2308.04026" title="arXiv">arXiv paper</a>. 

## 7.Set Evaluation Target and Measurements
In AgentSims, evaluation are made by QA forms. Every k ticks, system would ask the subject agent an evaluation question. You can customize your subject agent, evaluation question, measurement of response in config/eval.json 
The example in config/eval.json shows an experiment called 'know pH'. The experiment will ask agent Alan 'Are you acquainted with pH' every 1 tick and if 'Yes' in response, the eval function will return True.
```
{
  "id": "know pH", # the human-readable name of evaluation, 
  "target_nickname": "Alan", # name of the subject agent
  "query": "Are you acquainted with pH ?", # evaluation qustion 
  "measurement": " 'Yes' in response" # measurement, 
  "interval": 1 # Evaluate every 1 tick
}

```

## 8.Run Simulation

You can start ***tick*** or ***mayor*** with the buttons on the web client. You can also
start with:
```bash
python -u tick.py
```
```bash
python -u mayor.py
```

For the difference with ***tick*** and ***mayor***, refer to our <a href="https://arxiv.org/abs/2308.04026" title="arXiv">arXiv paper</a>.

## 9.Restart
The following reset steps need to be performed each time upon restarting:
```
  rm -rf snapshot/app.json
```
```
  sudo mysql
  drop database llm_account;
  drop database llm_game0001;
  create database `llm_game0001` default character set utf8mb4 collate utf8mb4_unicode_ci;
  create database `llm_account` default character set utf8mb4 collate utf8mb4_unicode_ci;
```
```
 ./restart.sh
```
-------------------------------
## Authors and Citation
***Authors***: Jiaju Lin,<a href="https://twitter.com/zhaohao919041" title="twitter">Haoran Zhao</a>*,Aochi Zhang,Yiting Wu, Huqiuyue Ping,Qin Chen

***About Us***: PTA Studio is a startup company dedicated to providing a better open source architecture for the NLP community and more interesting AI games for players.

***Contact Us***: zhaohaoran@buaa.edu.cn

Please cite our paper if you use the code or data in this repository.
```
@misc{lin2023agentsims,
      title={AgentSims: An Open-Source Sandbox for Large Language Model Evaluation}, 
      author={Jiaju Lin and Haoran Zhao and Aochi Zhang and Yiting Wu and Huqiuyue Ping and Qin Chen},
      year={2023},
      eprint={2308.04026},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
