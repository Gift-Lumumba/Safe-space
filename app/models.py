from . import db
import random
import string
from random import choice
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer)
    username = db.Column(db.String(255),primary_key = True)
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    crisis = db.relationship('Crisis', backref='user', lazy='dynamic')
    commentscrisis = db.relationship('Commentcrisis', backref = 'user', lazy = 'dynamic')
    Fam = db.relationship('Fam', backref = 'user', lazy = 'dynamic')
    commentsfam = db.relationship('Commentfam', backref = 'user', lazy = 'dynamic')
    health = db.relationship('Health', backref = 'user', lazy = 'dynamic')
    commentshealth = db.relationship('Commenthealth', backref = 'user', lazy = 'dynamic')
    mental = db.relationship('Mental', backref = 'user', lazy = 'dynamic')
    commentsmental = db.relationship('Commentmental', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def random_username():
        alphabet = string.ascii_letters
        username = ''.join(choice(alphabet) for i in range(8))
        return username
        

    def verify_password(self,password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Crisis(db.Model):
    __tablename__ = 'crisis'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    user_name = db.Column(db.String, db.ForeignKey("users.username"))
    comments = db.relationship('Commentcrisis', backref='crisis', lazy='dynamic')

    def save_crisis(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_crisis(cls):
        crisis = Crisis.query.all()
        return crisis

class Commentcrisis(db.Model):
    __tablename__ = 'crisiscomments'
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String, db.ForeignKey("users.username"))
    crisis_id = db.Column(db.Integer, db.ForeignKey('crisis.id'))
    description = db.Column(db.String(255))

    def save_comment(self):
        """
        Function that saves the crisis comments
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Commentcrisis.query.filter_by(crisis_id=id).all()
        return comment

    def __repr__(self):
        return f'Comment: {self.content}'
class Fam(db.Model):
    __tablename__ = 'fams'
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(255))
    user_name = db.Column(db.String, db.ForeignKey("users.username"))
    comments = db.relationship('Commentfam', backref='title', lazy='dynamic')

    def save_Fam(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_Fam(cls):
        fam = Fam.query.all()
        return fam

class Commentfam(db.Model):
    __tablename__ = 'famcomments'
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String, db.ForeignKey("users.username"))
    fam_id = db.Column(db.Integer, db.ForeignKey('fams.id'))
    description = db.Column(db.String(255))

    def save_commentl(self):
        """
        Function that saves the fam' comments
        """
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_commentsl(self, id):
        comment = Commentfam.query.filter_by(fam_id=id).all()
        return comment

    def __repr__(self):
        return f'Comment: {self.content}'

class Health(db.Model):
    __tablename__ = 'health'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    user_name = db.Column(db.String, db.ForeignKey("users.username"))
    comments = db.relationship('Commenthealth', backref='title', lazy='dynamic')

    def save_health(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_health(cls):
        health = Health.query.all()
        return health

class Commenthealth(db.Model):
    __tablename__ = 'healthcomments'
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String, db.ForeignKey("users.username"))
    health_id = db.Column(db.Integer, db.ForeignKey('health.id'))
    description = db.Column(db.String(255))

    def save_commenthealth(self):
        """
        Function that saves the health' comments
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_commenthealth(self, id):
        comment = Commenthealth.query.filter_by(health_id=id).all()
        return comment

    def __repr__(self):
        return f'Comment: {self.content}'

class Mental(db.Model):
    __tablename__ = 'mental'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    user_name = db.Column(db.String, db.ForeignKey("users.username"))
    comments = db.relationship('Commentmental', backref='mental', lazy='dynamic')

    def save_mental(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_mental(cls):
        mental = Mental.query.all()
        return mental
                   
class Commentmental(db.Model):
    __tablename__ = 'mentalcomments'
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String, db.ForeignKey("users.username"))
    mental_id = db.Column(db.Integer, db.ForeignKey('mental.id'))
    description = db.Column(db.String(255))

    def save_commentmental(self):
        """
        Function that saves the depression' comments
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_commentmental(self, id):
        comment = Commentmental.query.filter_by(mental_id=id).all()
        return comment

    def __repr__(self):
        return f'Comment: {self.content}'        
