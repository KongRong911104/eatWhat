from flask import Flask, request
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

rooms = {}

@app.route('/')
def index():
    return "Server is running!"

@socketio.on('join-room')
def on_join(data):
    print('initiated')
    room = data['room']
    if room not in rooms:
        rooms[room] = []
    rooms[room].append(request.sid)
    join_room(room)
    socketio.emit('room-users', rooms[room], room=room)

@socketio.on('leave-room')
def on_leave(data):
    room = data['room']
    if room in rooms and request.sid in rooms[room]:
        rooms[room].remove(request.sid)
        leave_room(room)
        if len(rooms[room]) == 0:
            del rooms[room]
        else:
            socketio.emit('room-users', rooms[room], room=room)

@socketio.on('disconnect')
def on_disconnect():
    # 使用备份列表来遍历和修改 rooms 字典
    for room in list(rooms.keys()):
        if request.sid in rooms[room]:
            rooms[room].remove(request.sid)
            if len(rooms[room]) == 0:
                del rooms[room]
            else:
                socketio.emit('room-users', rooms[room], room=room)

@socketio.on('new-order')
def on_new_order(data):
    room = data['room']
    # 处理新订单逻辑
    socketio.emit('order-notification', data, room=room, include_self=False)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
