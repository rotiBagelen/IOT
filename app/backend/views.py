from flask import Blueprint, request, jsonify, render_template, redirect, url_for, Flask
from . import db
from .models import Taplog, Temperature, cardID
from datetime import datetime

views = Blueprint('views', __name__) # Inititally off

@views.route('/', methods=['GET'])
def index():
    logs = Taplog.query.order_by(Taplog.id.desc()).all()
    return render_template('index.html', logs=logs)

@views.route('/api/taplog', methods=['POST'])
def add_taplog():
    try:
        if request.method == 'POST':
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No data provided'}), 400
            try:
                date = datetime.now().replace(microsecond=0).isoformat(sep=" ")
                cardId = data['card_id']

                if not cardID.query.filter_by(card_id=cardId).first():
                    username = "Unknown User"
                else:
                    username = cardID.query.filter_by(card_id=cardId).first().userName

                new_taplog = Taplog(timestamp=date, card_id=data['card_id'], userName=username)
                db.session.add(new_taplog)
                db.session.commit()
                return jsonify({'message': 'Taplog added successfully'}), 201
            
            except Exception as e:
                db.session.rollback()
                return jsonify({'error': str(e)}), 500
    
        # # GET request only for debuging purposes, this should be disabled in production
        # return Taplog.query.filter_by(userName='isa').first().timestamp, 200

    except Exception as e:
        return "something went wrong", 500
    
@views.route('/api/lamp', methods=['GET', 'POST'])
def lamp_control():
    global lamp_state
    try:
        if request.method == 'POST':
            data = request.get_json()
            if not data or 'state' not in data:
                return jsonify({'error': 'No state provided'}), 400
            
            lamp_state = data['state']
            # print(f"Lamp state set to: {lamp_state}")
            return jsonify({'message': f'Lamp state set to {lamp_state}'}), 200
        
        # GET request to check the current state of the lamp
        return lamp_state, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@views.route('/api/temp', methods=['GET', 'POST'])
def temperature_display():
    try:
        if request.method == 'POST':
            data = request.get_json()
            if not data or 'temperature' not in data:
                return jsonify({'error': 'No temperature provided'}), 400
            temp = data['temperature']
            date = datetime.now().replace(microsecond=0).isoformat(sep=" ")
            new_temp = Temperature(timestamp=date, temperature=float(temp))
            db.session.add(new_temp)
            db.session.commit()
            return jsonify({'message': 'Temperature logged successfully'}), 201
        
        temps = Temperature.query.with_entities(Temperature.temperature).order_by(Temperature.id.asc()).all()
        temperature_list = [t[0] for t in temps]

        timestamps = Temperature.query.with_entities(Temperature.timestamp).order_by(Temperature.id.asc()).all()
        timestamp_list = [t[0] for t in timestamps]

        resp = {
            'temperatures': temperature_list[-20:],
            'timestamps': timestamp_list[-20:]
        }
        return jsonify(resp), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@views.route('/api/delete-history', methods=['POST'])
def delete_taplog():
    try:
        data = request.get_json()
        if not data or 'delete' not in data:
            return jsonify({'error': 'No ID provided'}), 400

        taplog_id = data['delete']
        desicion = data['delete']
        if desicion != True:
            return jsonify({'delete':'failed'}), 200
        db.session.query(Taplog).delete()
        db.session.commit()

        return jsonify({"delete":"success"}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500