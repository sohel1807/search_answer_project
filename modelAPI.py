# api to get client information
from fastapi import FastAPI
from pydantic import BaseModel
from project import startModel  # Correct import
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return

class InputModel(BaseModel):
    query: str
    url: str

app = FastAPI()

@app.post('/')
async def test_api(payload: InputModel):
    res = await startModel(payload.url, payload.query)
    return {"result": res}

@app.get('/')
async def home():
    return {"message": "working"}