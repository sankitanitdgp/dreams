from flask import Flask, Response,render_template, url_for, request, redirect
from flask_restful import Resource, Api
from random import randint
from mongoengine import *
import config

app = Flask(__name__)
api = Api(app)


connect(db=config.DATABASE_CONFIGURATION['table_name'], config.DATABASE_CONFIGURATION['host'], int(config.DATABASE_CONFIGURATION['port']))

class User(Document):
    firstname = StringField(required=True, max_length=50)
    lastname = StringField(required=True, max_length=50)
    password = StringField(required=True, max_length=100)
    confirmpassword = StringField(required=True, max_length=100)
    uniqueid = IntField(required=True, max_value=10, default=randint(1, 199))

class Login(Resource):
    def get(self):
        return Response(render_template('login.html'), mimetype='text/html')

    def post(self):
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('dashboard'))


class Register(Resource):
    def get(self):
        return Response(render_template('register.html'), mimetype='text/html')
    def post(self):
        first_name_input = request.form['firstname']
        last_name_input = request.form['lastname']
        password_input = request.form['password']
        confirm_password_input = request.form['confirm_password']
        new_user_data = User(

            firstname = first_name_input,
            lastname = last_name_input,
            password = password_input,
            confirmpassword = confirm_password_input
        )

        new_user_data.save()
        app.logger.info('Document posted successfully')
        return Response(render_template('login.html'), mimetype='text/html')

@api.resource('/dasboard')
class Dashboard(Resource):
    def get(self):
        return Response(render_template('dashboard.html'), mimetype='text/html')

api.add_resource(Login, '/')
api.add_resource(Register, '/register')
api.add_resource(Dashboard)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
