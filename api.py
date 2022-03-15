from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# Create Flask App
app = Flask(__name__)

# Application Entry point
api = Api(app)


# Configure SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///texts.db'


# initialize SQLAlchemy
db = SQLAlchemy(app)

# Database Model


class TextModel(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)


# Resource Fields (to make it JSON serializable)
resource_fields = {
    '_id': fields.Integer,
    'text': fields.String
}

# REST api methods arguments
text_post_args = reqparse.RequestParser(bundle_errors=True)
text_post_args.add_argument(
    "text",
    type=str,
    help="Input Text is Required",
    required=True
)

text_update_args = reqparse.RequestParser()
text_update_args.add_argument("text", type=str)


# RESTful resource

class TextList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        records = TextModel.query.all()
        return records, 200

    @marshal_with(resource_fields)
    def post(self):
        args = text_post_args.parse_args()
        newText = TextModel(text=args["text"])
        db.session.add(newText)
        db.session.commit()
        return newText, 201


class InputText(Resource):
    @marshal_with(resource_fields)
    def get(self, text_id):
        return TextModel.query.filter_by(_id=text_id).first_or_404(f"Record with ID={text_id} not found..."), 200

    @marshal_with(resource_fields)
    def put(self, text_id):
        args = text_post_args.parse_args()
        record = TextModel.query.filter_by(_id=text_id)\
            .first_or_404(description=f'Record with id={text_id} is not available')
        record.text = args['text']
        db.session.commit()
        return record, 201

    def delete(self, text_id):
        record = TextModel.query.filter_by(_id=text_id).first_or_404(
            description=f'Record with id={text_id} is not available')
        db.session.delete(record)
        db.session.commit()
        return '', 204


api.add_resource(InputText, '/texts/<int:text_id>')

# Get all texts
api.add_resource(TextList, '/texts')


@app.route("/", methods=["GET", "POST"])
def hello():
    return "Hello, World!"


# Main block
if __name__ == '__main__':
    app.run(debug=True)
