import pytest
from channels.testing import WebsocketCommunicator
from chat.consumers import ChatConsumer


@pytest.mark.asyncio
async def test_chat_consumer_connect():
    # Test a normal connection
    communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), "/testws/")
    communicator.scope["url_route"] = {'args': (), 'kwargs': {'room_name': 'ok'}}
    connected, _ = await communicator.connect()
    assert connected
    await communicator.disconnect()


@pytest.mark.asyncio
async def test_chat_consumer_receive():
    # Test a normal connection
    communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), "/testws/")
    communicator.scope["url_route"] = {'args': (), 'kwargs': {'room_name': 'ok'}}
    connected, _ = await communicator.connect()
    r = await communicator.send_to(text_data="hello")
    response = await communicator.receive_from()
    assert response == "hello"
    await communicator.disconnect()

