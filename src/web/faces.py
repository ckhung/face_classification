from flask import Flask, jsonify, make_response, request, abort, redirect, send_file
import argparse, logging, os

import emotion_gender_processor as eg_processor

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("https://newtoypia.blogspot.com/2018/08/emotion.html", code=302)

@app.route('/emo/<ret_type>', methods=['POST'])
def upload(ret_type):
    try:
        # with open('/tmp/debug.txt', "w+") as debug_file:
        #     print("bp A".format(), file=debug_file)
        image = request.files['image'].read()
        result_path = '/tmp/result.png'
        ret_array = eg_processor.process_image(image, result_path)
        if ret_type == 'label':
            return jsonify(ret_array)
        elif ret_type == 'mark':
            return send_file(result_path, mimetype='image/png')
        else:
            return 'unknown ret_type ' + ret_type
    except Exception as err:
        logging.error('An error has occurred whilst processing the file: "{0}"'.format(err))
        abort(400)

@app.route('/log')
def viewlog():
    if args.logfile:
        with open(args.logfile) as F:
            ret = '<pre>' + F.read() + '</pre>'
    else:
        ret = 'no log file'
    statinfo = os.stat(args.logfile)
    if args.truncate > 0 and statinfo.st_size > args.truncate:
        with open(args.logfile, 'w') as F:
            F.write('')
    return ret

@app.errorhandler(400)
def bad_request(erro):
    return make_response(jsonify({'error': 'We cannot process the file sent in the request.'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Resource no found.'}), 404)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='face classification by emotion',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-L', '--logfile', type=str,
        default='', help='log file name')
    parser.add_argument('-T', '--truncate', type=int,
        default='-1', help='truncate log file if larger than this many bytes (<0 means do not truncate)')
    args = parser.parse_args()
    # https://stackoverflow.com/questions/17743019/flask-logging-cannot-get-it-to-write-to-a-file
    if args.logfile:
        logging.basicConfig(filename=args.logfile, level=logging.DEBUG)
    app.debug = True
    app.run(threaded=False, host='0.0.0.0', port=8084)
    # "Cannot interpret feed_dict key as Tensor" =>
    # https://stackoverflow.com/a/50086909/5281446
