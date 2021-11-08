from fastapi import FastAPI

app = FastAPI()

# request Get methid url: "/"



@app.get("/")
def root():

    #return {"message": "Welcome to my api 1st instance"}
    return {"message": "Welcome to my api 2nd instance"}

@app.get("/posts")
def get_post():
    return {"data": "This is your post"}


#@app.get("/random")
#def get_data():
#    return {"post": "Another post"}

