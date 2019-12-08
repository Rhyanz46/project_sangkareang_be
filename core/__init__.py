from flask import make_response, jsonify, request, abort


def result(data, code):
    return make_response(jsonify(data), code)


def method_is(method):
    return request.method == method.upper()
