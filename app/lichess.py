from contextlib import suppress
import aiohttp
from pytest import mark

TOKEN = 'lip_n5ck1hbqjoGV8hAwbcmh'
USER = 'EXTAZIA'

async def get_current_lichess_ratings(username: str = USER, auth_token: str = TOKEN):
    async with aiohttp.ClientSession(headers={'Authorization': auth_token}) as session:
        async with session.get(f'https://lichess.org/api/user/{username}/rating-history') as response:
            ratings_over_time = await response.json()
            
            current_ratings = {}
            for f in ratings_over_time:
                with suppress(IndexError):
                    current_ratings[f['name']] = f['points'][-1][3]

            return current_ratings
    
@mark.asyncio
async def test_get_current_ratings():
    current_ratings_ = await get_current_lichess_ratings()
    
    assert isinstance(current_ratings_, dict)
    for format_ in ('Bullet', 'Blitz', 'Rapid', 'Classical'):
        assert format_ in current_ratings_.keys()

    assert isinstance(current_ratings_['Classical'], (float, int))