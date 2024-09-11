import aiohttp.web

async def handler(req: aiohttp.web.Request):
    return aiohttp.web.Response(headers={
        'X-Debug-Param': req.query.get('param', ''),
    })
app = aiohttp.web.Application()
app.add_get('/', handler)