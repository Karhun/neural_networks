from flask import Flask
from flask import json
from flask import Response, request
import tensorflow as tf
import urllib

app = Flask(__name__)
graph_path = 'output_graph.pb'
labels_path = 'output_labels.txt'

@app.route('/classify', methods=['POST'])
def classify():
	image_path = request.json['imageURL']
	output = {'result':[]}
	# Read in the image_data
	image_data = urllib.urlopen(image_path).read()
	# Loads label file, strips off carriage return
	label_lines = [line.rstrip() for line in tf.gfile.GFile(labels_path)]
	# Unpersists graph from file
	with tf.gfile.FastGFile(graph_path, 'rb') as f:
		graph_def = tf.GraphDef()
		graph_def.ParseFromString(f.read())
		_ = tf.import_graph_def(graph_def, name='')
		
	# Feed the image_data as input to the graph and get first prediction
	with tf.Session() as sess:
		softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
		predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})
		
		# Sort to show labels of first prediction in order of confidence
		top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
		for node_id in top_k:
			human_string = label_lines[node_id]
			score = predictions[0][node_id]
			output_ = {
				'class' : '%s' % human_string,
				'score' : '%.5f' % score
			}
			output['result'].append(output_)
	
	js = json.dumps(output, sort_keys=True, indent=4)
	resp = Response(js, status=200, mimetype='application/json')
	resp.headers['Link'] = 'http://myWeb.com'
	return js

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')