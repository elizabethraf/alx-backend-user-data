#!/usr/bin/env python3
"""Display  Log out"""
from flask import request, redirect, jsonify
from werkzeug.exceptions import Forbidden


@app.route('/sessions', methods=['DELETE'])
def logout():
    session_id = request.cookies.get('session_id')

    try:
        user = User.query.filter_by(session_id=session_id).one()

        user.session_id = None
        db.session.commit()
        return redirect('/')
    except:
        raise Forbidden(description='Invalid session ID.')
