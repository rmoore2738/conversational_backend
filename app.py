from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from Api import suggest_next_word
from Generator import Generator

gen = Generator()
app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/suggest_next_word")
async def suggest_word(request: Request):
    data = await request.json()
    return suggest_next_word(data)

#@app.post("/get_next_options")
#async def next_options(request: Request):
    #data = await request.json()
    #return get_next_options(data)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run_server(debug=True, host="0.0.0.0", port=port)

