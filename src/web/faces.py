from flask import Flask, jsonify, make_response, request, abort, redirect, send_file
import logging, os

import emotion_gender_processor as eg_processor

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("https://ekholabs.ai", code=302)

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

@app.errorhandler(400)
def bad_request(erro):
    return make_response(jsonify({'error': 'We cannot process the file sent in the request.'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Resource no found.'}), 404)

if __name__ == '__main__':
    app.run(debug=True, threaded=False, host='0.0.0.0', port=8084)
    # "Cannot interpret feed_dict key as Tensor" =>
    # https://stackoverflow.com/a/50086909/5281446
