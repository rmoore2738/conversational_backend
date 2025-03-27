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

# Initialize models
generator_init()

@app.post("/suggest_next_word")
async def suggest_word(request: Request):
    data = await request.json()
    return suggest_next_word(data)

#@app.post("/get_next_options")
#async def next_options(request: Request):
    #data = await request.json()
    #return get_next_options(data)
