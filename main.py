
from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
import random
import time

# 注册插件
@register(name="XuenianStatus", description="XuenianStatus", version="0.1", author="LXHcat")
class MyPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    time = time.strftime(format[%H%M, time.localtime()])
    Hbps = random.random(40,70)
    Hbpn = random.random(65,120)
    Hbpq = random.random(135,170)
    StatusList=['学习', '空闲', '发情', '想江河']
    if (time >= 0000 & time <=615)
    Status='休眠'
    Hbp=Hbps
    elif (time >= 615 & time <=1155)
        Status=StatusList[i = random.random(0,3)]
        if (i==2|i==3)
            Hbp=Hbpq
        else 
            Hbp=Hbpn
    elif (time >= 1155 & time <=1400)
        Status=StatusList[i = random.random(1,3)]
        if (i==2|i==3)
            Hbp=Hbpq
        else 
            Hbp=Hbpn
    elif (time >= 1400 & time <=2130)
        Status=StatusList[i = random.random(0,3)]
        if (i==2|i==3)
            Hbp=Hbpq
        else 
            Hbp=Hbpn
    elif (time >= 2130 & time <=2400)
        Status=StatusList[i = random.random(1,3)]
        if (i==2|i==3)
            Hbp=Hbpq
        else 
            Hbp=Hbpn
 
    async def person_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 PersonNormalMessageReceived 的对象
        if msg == "XuenianStatus":  # 如果消息为hello

            # 输出调试信息
            self.ap.logger.debug("hello, {}".format(ctx.event.sender_id))

            # 回复消息 "hello, <发送者id>!"
            ctx.add_return("reply", ["雪年状态：" Status "心率：" Hbp "{}".format(ctx.event.sender_id)])

            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 GroupNormalMessageReceived 的对象
        if msg == "XuenianStatus":  # 如果消息为hello

            # 输出调试信息
            self.ap.logger.debug("hello, {}".format(ctx.event.sender_id))

            # 回复消息 "hello, everyone!"
            ctx.add_return("reply", ["hello, everyone!"])

            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
