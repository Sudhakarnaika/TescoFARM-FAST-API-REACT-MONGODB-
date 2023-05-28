from fastapi import FastAPI

app = FastAPI()


# farmapp get request
@app.get("/", tags=['ROOT'])
async def root() -> dict:    
    return {"Ding":"Dong bell"}



#Get farm
@app.get('/farm', tags=['farms'])
async def get_farm() -> dict:    
    return {"data": farms}


#Post farm
@app.post('/farm', tags=['farms'])
async def add_farm(farm:dict) -> dict:    
    farms.append(farm)
    return {"data": "A barrel has been added to farm"}


#Put farm
@app.put('/farm/{id}', tags=['farms'])
async def update_farm(id:int, body:dict) -> dict:   
    for farm in farms:
        if int((farm['id']))==id:
            farm['Activity'] = body['Activity']
        return {"data": f"A barrel Id {id} has been updated"}
    return
    {
        "data": f"A barrel Id {id} has not found"
        }




#Delete farm
@app.delete('/farm/{id}', tags=['farms'])
async def delete_farm(id:int) -> dict:   
    for farm in farms:
        if int((farm['id']))==id:
            farms.remove(farm)
        return {"data": f"A barrel with Id {id} has been deleted"}
    





farms =  [

    {"id": "1", 
     "Activity":"Stitching for Adults Night Suits"} ,
         
    {"id": "2", 
     "Activity":"Stitching for Children Uniforms"} 
] 