# Made by brz

import asyncio
import json
from random import randint
import sys
import websockets
from scripts import player
from decouple import config

auth_token = config('AUTH_TOKEN')


async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    #print(message)
    await websocket.send(message)


async def start(auth_token):
    uri = "ws://megachess.herokuapp.com/service?authtoken={}".format(auth_token)
    async with websockets.connect(uri) as websocket:
        await send(websocket, 'login', {})
        while True:
            try:
                response = await websocket.recv()
                print(f"< {response}")
                data = json.loads(response)
                if data['event'] == 'update_user_list':
                    # This function shows all connected users in the platform
                    pass
                if data['event'] == 'gameover':
                    # This function tells if the game is over
                    pass
                if data['event'] == 'ask_challenge':
                    # This function accepts any challenge
                    # if data['data']['username'] == 'brz':
                    #     await send(
                    #         websocket,
                    #         'accept_challenge',
                    #         {
                    #             'board_id': data['data']['board_id'],
                    #         },
                    #     )
                    await send(
                            websocket,
                            'accept_challenge',
                            {
                                'board_id': data['data']['board_id'],
                            },
                        )
                if data['event'] == 'your_turn':
                    board = data['data']['board']
                    color = data['data']['actual_turn']
                    from_row, from_col, to_row, to_col = player.play(board, color)
                    await send(
                        websocket,
                        'move',
                        {
                            'board_id':     data['data']['board_id'],
                            'turn_token':   data['data']['turn_token'],
                            'from_row':     from_row,
                            'from_col':     from_col,
                            'to_row':       to_row,
                            'to_col':       to_col,
                        },
                    )

            except Exception as e:
                print('retry')


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        auth_token = sys.argv[1]
        asyncio.get_event_loop().run_until_complete(start(auth_token))
    else:
        asyncio.get_event_loop().run_until_complete(start(auth_token))