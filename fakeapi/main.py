#!/usr/bin/env python
#-*- coding: utf-8
"""A simple translator web service"""

# import json
from aiohttp import web

async def handle(request):
    """Handle the request"""
    print("======================================")
    print(request)
    print(request.headers)
    print(request.method)
    print(request.url)
    print(await request.text())
    print("======================================")

    # response_obj = {'status': 'success'}
    response_obj = [
        {"translations": [{"text": 'hello world'}]}
    ]

    return web.json_response(response_obj)

app = web.Application()
app.router.add_get('/translator', handle)
app.router.add_get('/translator/', handle)
app.router.add_get('/translator/ttranslatev3', handle)
app.router.add_get('/translator/tlookupv3', handle)

app.router.add_post('/translator', handle)
app.router.add_post('/translator/', handle)
app.router.add_post('/translator/ttranslatev3', handle)
app.router.add_post('/translator/tlookupv3', handle)

app.router.add_route('*', '/{tail:.*}', handle)

web.run_app(app)
