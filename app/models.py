from app import db
from sqlalchemy import text, ForeignKey
from sqlalchemy.dialects import postgresql
import bcrypt

class BaseModel(db.Model):
    """
        Base Abstract controlled model
        not showing on Database
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    archived = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    @classmethod
    def match_by(self, **kwargs):
        attrs = kwargs.keys()
        for attr in attrs:
            if not hasattr(self, attr):
                return "{} is not a valid attribute name".format(attr)
        return self.query.filter_by(archived=False).filter_by(**kwargs)

    @classmethod
    def all(self, order_by="created_at DESC"):
        """
        >>> Book.all()
        """
        return self.query.filter_by(archived=False).order_by(text(order_by)).all()

    @classmethod
    def find(self, id):
        """
        >>> Book.find(2)
        """
        return self.query.filter_by(id=id, archived=False).first()

    @classmethod
    def find_by(self, **kwargs):
        """
        >>> Book.find_by(name='Oliver Twist')
        """
        return self.match_by(**kwargs).first()

    @classmethod
    def destroy(self, id):
        """
        >>> Book.destroy(2)
        """
        entity = self.query.filter_by(id=id)
        entity.archived = True
        entity.save()
        return True

    @classmethod
    def paginate_by(self, page, per_page):
        """
        >>> Book.paginate_by(page=1, per_page=5)
        """
        return self.query.filter_by(archived=False).order_by(text("created_at DESC")).paginate(page=page,
                                                                                               per_page=per_page,
                                                                                               error_out=False).items

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(BaseModel):
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(postgresql.BYTEA, nullable=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def authenticate(self, password):
        if bcrypt.checkpw(password.encode("utf-8"), self.password):
            return True
        else:
            # user password is false
            return False

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self.save()


