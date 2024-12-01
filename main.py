from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from datetime import datetime, timedelta
from controller.controller import Controller

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')



@app.route('/')
def index():
    return render_template('index.html')

# @app.post("/add-organization")
# async def add_organization(
#     name: str = Form(...),
#     slogan: str = Form(...),
#     logo: str = Form(...),
#     duties: str = Form(...),
#     address: str = Form(...),
#     telephone: str = Form(...),
#     description: str = Form(""),
#     head_id: int = Form(None)
# ):
#     success, message = Controller.add_organization(name, slogan, logo, duties, address, telephone, description, head_id)
#     if success:
#         return {"message": "سازمان با موفقیت اضافه شد!"}
#     else:
#         return {"error": f"{message}"}

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5001, debug=True)