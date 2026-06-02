from fastapi import FastAPI,HTTPException
import uvicorn
from shape_manager import ShapeManager
from shape import Shape
from rectangle import Rectangle
from square import Square
from circle import Circle

app = FastAPI()

shapeManager = ShapeManager()

# endpoints


@app.get("/shapes")
def get_all_shapes():
    return shapeManager.get_all_shapes()
   


@app.post("/shapes")
def create_new_shape(shape:dict):
    if shapeManager.shapes:
        shape_id = max(shape.id for shape in shapeManager.shapes) + 1  
    else:
        shape_id = 1

    if shape["type"] == "rectangle":
        new_rectangle = Rectangle(shape_id, shape["width"], shape["height"])
        shapeManager.create_shape(new_rectangle)
    elif shape["type"] == "circle":
        new_circle = Circle(shape_id , shape["radius"])
        shapeManager.create_shape(new_circle)
    elif shape["type"] == "square":
        new_square = Square(shape_id, shape["side"])
        shapeManager.create_shape(new_square)
    return {"success":True}


@app.put("/shapes/{id}")
def replace_shape(id:int,shape:dict):
    succes = shapeManager.update_shape(id,shape)
    if not succes:
        raise HTTPException(status_code=404 , detail="the shape not found")
    return {"success":True}


@app.delete("/shapes/{id}")
def delete_shape(id:int):
    succes = shapeManager.delete_shape(id)
    if not succes:
        raise HTTPException(status_code=404 , detail="the shape not found")
        
    return {"success": True}

@app.get("/shapes/total-area")
def sum_of_all_shapes():

    shapes = shapeManager.get_all_shapes()

    if not shapes:
        raise HTTPException(status_code=404 , detail="there are not shapes")

    return sum(shape.get_area() for shape in shapes)



@app.get("/shapes/{id}")
def shape_by_id(id:int):
    for shape in shapeManager.shapes:
        if shape.id == id:
            return shape.to_dict()
        
    raise HTTPException(status_code=404,detail="the shape not found")



# @app.get("/shapes/count")
# def total_shapes():
#     return len(shapeManager.get_all_shapes())


# @app.get("/shapes/type/{type}")
# def shape_type(type:str):
#     lst = []
#     shapes = shapeManager.get_all_shapes()
#     for shape in shapes:
#         lst.append(shape.shape_type)
    
#     return lst



if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)