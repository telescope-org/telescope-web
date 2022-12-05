from flask import Blueprint, jsonify, request
from common.token import check_token, gen_token

from service.phone_service import PhoneService

phone = Blueprint('phone', __name__, url_prefix='/api/phone')


@phone.route('/register', methods=['GET'])
def register():
    phone = request.args.get('phone')
    if phone is None:
        return jsonify({
            'code': 500,
            'message': 'phone is not empty.'
        })
    location = request.args.get('location')
    deviceId = request.args.get('deviceId')
    operation = request.args.get('operation')
    createTime = request.args.get('createTime')
    version = request.args.get('version')
    is_ok = PhoneService.register({
        'phone': phone,
        'location': location,
        'deviceId': deviceId,
        'operation': operation,
        'createTime': createTime,
        'version': version
    })
    if is_ok is False:
        return jsonify({
            'code': 500,
            'message': 'param err!',
        })

    return jsonify({
        'code': 200,
        'message': 'register success!',
        'data': {
            'token': gen_token(phone=phone),
        },
        'type': 0,
    })


@phone.route('/location', methods=['GET'])
def location():
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

    address = request.args.get('address')
    if address is None:
        return jsonify({
            'code': 500,
            'message': 'address is not empty.'
        })
    operation = request.args.get('operation')
    createTime = request.args.get('createTime')
    version = request.args.get('version')
    is_ok = PhoneService.location({
        'phone': phone,
        'address': address,
        'token': token,
        'operation': operation,
        'createTime': createTime,
        'version': version
    })

    if is_ok is False:
        return jsonify({
            'code': 500,
            'message': 'param err!',
        })

    return jsonify({
        'code': 200,
        'message': 'update location success!',
        'type': 1,
        'data': {},
    })
