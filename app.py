from flask import Flask, jsonify
import boto3
from boto3.dynamodb.conditions import Key, Attr
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Use session-based credentials
session = boto3.Session(
    aws_access_key_id='AKIAS2RBT7PDOMXMH6OM',
    aws_secret_access_key='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',
    region_name='us-east-1'
)

dynamodb = session.resource('dynamodb')
table = dynamodb.Table('jute_data')

@app.route('/', methods=['GET'])
def get_dye_bath_data():
    try:
        response = table.scan(
            FilterExpression=Attr('DataType').eq('DyeBath')
        )
        items = response.get('Items', [])
        return jsonify(items)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Serve on a different port
