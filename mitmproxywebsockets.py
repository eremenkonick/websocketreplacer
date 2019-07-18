import mitmproxy.http
from mitmproxy import ctx
import re

replacements = [
    ('lol', 'kek'),
]

class WebsocketReplacer:
    def __init__(self):
        self.num = 0

    def websocket_message(self, flow: mitmproxy.websocket.WebSocketFlow):
        message = flow.messages[-1] #get last message

        if message.from_client: #modify messages from client
            ctx.log.info("Original message:\n {}".format(message.content))
            for old,new in replacements: # cycle for subs
                message.content = re.sub(old, new, message.content)
            ctx.log.info("Modified message:\n {}".format(message.content))
        else:
            ctx.log.info(message.content)

    # manipulate the message content


addons = [
    WebsocketReplacer()
]

