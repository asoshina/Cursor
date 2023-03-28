from flask import Flask, abort
import logging
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route('/')
def basic():
    app.logger.info('Reached hello route')
    return '<h1>Hello, Flask!</h1>'


@app.route('/datetime')
def date_time_def():
    """
     Returns current datetime  or with optional timezone

     ./datetime/ return current datetime on server
     >>Local time is : 2023-03-28 14:02:32 EEST

     ./datetime/+3 return time in GMT+3 zone
     >> Time in GMT +3 : 2023-03-28 14:00:58

     ./datetime/0 return Greenwich datetime:
        >> Greenwich time is : 2023-03-28 11:01:30
    """
    app.logger.info('Show documentation')

    return date_time_def.__doc__.replace('\n', '<br>')


@app.route('/datetime/')
@app.route('/datetime/<zone>')
def date_time_zone(zone='local'):
    app.logger.info('Show time in GMT %r zone', zone)
    if zone == 'local':
        return f'Local time is : {datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")}'
    zone_str = zone
    zone = int(zone)

    if abs(zone) > 12:
        abort(406, "Timezone isn\'t correct. It should be less then 12")

    new_time = datetime.utcnow() + timedelta(hours=zone)
    if zone != 0:
        return f'Time in GMT {zone_str} : {new_time.strftime("%Y-%m-%d %H:%M:%S")}'
    else:
        return f'Greenwich time is : {new_time.strftime("%Y-%m-%d %H:%M:%S")}'


if __name__ == '__main__':
    # We need to set logging to be able to see everything
    app.logger.setLevel(logging.DEBUG)

    app.run(host='127.0.0.1', port=5000, debug=True)