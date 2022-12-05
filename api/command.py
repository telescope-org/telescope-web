import json
from flask import Blueprint, jsonify, request
from common.logger import Logger
from common.token import check_token
from service.command_service import CommandService


command = Blueprint('command', __name__, url_prefix='/api/command')


@command.route('/poll', methods=['GET'])
def poll():
    phone = request.args.get('phone')
    token = request.args.get('token')
    if phone is None or token is None:
        return jsonify({
            'code': 403,
            'message': 'auth failed.'
        })
    phone = phone[3:]
    if check_token(token=token, phone=phone):
          return jsonify({
            'code': 403,
            'message': 'auth failed.'
        })  

    commands = CommandService.get_commands(phone)

    for cmd_id in list(commands.keys()):
        CommandService.del_command(phone=phone, cmd_id=cmd_id)
        Logger.info(f"获取完成，清除命令缓存, command_id: {cmd_id}!")

    return jsonify({
        'code': 200,
        'message': 'poll success!',
        'data': {
            'commands': commands,
        },
        'type': 2,
    })


@command.route('/receive', methods=['POST'])
def receive():
    data = request.get_data()
    form_data = json.loads(data)
    print(json.loads(data)['phone'])
    phone = form_data['phone']
    token = form_data['token']
    if phone is None or token is None:
        return jsonify({
            'code': 403,
            'message': 'auth failed.'
        })
    phone = phone[3:]
    if check_token(token=token, phone=phone):
          return jsonify({
            'code': 403,
            'message': 'auth failed.'
        })  
    CommandService.receive(form_data)
    return jsonify({
        'code': 200,
        'message': 'ok',
        'data': {},
        'type': 3,
    })

@command.route('/addCommand', methods=['GET'])
def add_command():
    phone = request.args.get('phone')
    if phone is None:
        return jsonify({
            'code': 403,
            'message': 'auth failed.'
        })

    command = request.args.get('command')

    if CommandService.add_commands(phone=phone, command_key=command) is False:  
        return jsonify({
            'code': 500,
            'message': 'command add failed!',
            'data': {},
            'type': 3,
        })
    return jsonify({
        'code': 200,
        'message': 'ok',
        'data': {},
        'type': 3,
    })

@command.route('/deleteKey', methods=['GET'])
def delete_key():
    phone = request.args.get('phone')
    if phone is None:
        return jsonify({
            'code': 403,
            'message': 'auth failed.'
        })

    command = request.args.get('command')

    if CommandService.del_command(phone=phone, command_key=command) is False:  
        return jsonify({
            'code': 500,
            'message': 'command add failed!',
            'data': {},
            'type': 3,
        })
    return jsonify({
        'code': 200,
        'message': 'ok',
        'data': {},
        'type': 3,
    })