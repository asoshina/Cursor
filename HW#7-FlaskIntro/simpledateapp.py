from flask import Flask, abort

from datetime import datetime, timedelta
app = Flask(__name__)


@app.route('/')
def basic():
    app.logger.info('Reached hello route')
    return '<h1>Hello, Flask!</h1>'


@app.route('/datetime/')
def date_time():
    app.logger.info('show local time')
    return f'Local time is : {datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")}'


@app.route('/datetime/<zone>')
def date_time_zone(zone):
    zone_str = zone
    zone = int(zone)
    app.logger.info('Show time in GMT %r zone', zone)

    if abs(zone) > 12:
        abort(406, "Timezone isn\'t correct. It should be less then 12")

    new_time = datetime.utcnow() + timedelta(hours=zone)
    if zone != 0:
        return f'Time in GMT {zone_str} : {new_time.strftime("%Y-%m-%d %H:%M:%S")}'
    else:
        return f'Greenwich time is : {new_time.strftime("%Y-%m-%d %H:%M:%S")}'


if __name__ == '__main__':
    # We need to set logging to be able to see everything
    import logging
    app.logger.setLevel(logging.DEBUG)

    app.run(host='127.0.0.1', port=5000, debug=True)