import logging
import aiohttp
from .models import QuickReply
from typing import Optional, Dict, Union, List

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='myapp.log',
    filemode='w'
)
logger.setLevel(logging.DEBUG)

class ReyClient:
    def __init__(self, bearer_token: str) -> None:
        self.__bearer_token = bearer_token
        self._base_url = "https://api.line.me"
        self._urls = {
            "messages": {
                "push": self._base_url + "/v2/bot/message/push",
                "reply": self._base_url + "/v2/bot/message/reply"
            }
        }

    async def send_message(
        self, 
        message: str, 
        *, 
        user_id: Optional[str] = None, 
        user_ids: Optional[list] = None, 
        disable_notif: bool = False, 
        reply_token: Optional[str] = None, 
        quote_token: Optional[str] = None,
        quick_reply: Optional[QuickReply] = None,
        display_name: Optional[str] = None,
        display_icon_url: Optional[str] = None
    ) -> aiohttp.ClientResponse:
        json_data: Dict[str, Union[Optional[str], bool, List, Dict]] = {"to": user_id if not user_ids else user_id} if not reply_token else {"replyToken": reply_token}
        data = {
            "type": "text",
            "text": message,
            "sender": {}
        }

        if quote_token:
            data["quoteToken"] = quote_token

        if quick_reply:
            data["quickReply"] = {
                "items": quick_reply._QuickReply__options  #type: ignore
            }

        if display_name:
            data["sender"]["name"] = display_name

        if display_icon_url:
            data["sender"]["iconUrl"] = display_icon_url

        json_data["notificationDisabled"] = disable_notif
        json_data["messages"] = [data]

        async with aiohttp.ClientSession() as session:
            async with session.post(
                self._urls["messages"]["push"] if not reply_token else self._urls["messages"]["reply"], 
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.__bearer_token}",
                },
                json=json_data
            ) as res:
                logger.debug(f"[{res.status}] Attepting to send message: json data:\n{json_data}\nresponse: {await res.json()}")
                return res