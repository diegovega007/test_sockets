from datetime import datetime
# from app import db

# class Chat(db.Model):
#     '''
#     Table chat
#     '''
#     __tablename__ = 'chat'

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(128))
#     text = db.Column(db.Text)
#     channel = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Corrected to utcnow()

#     def __repr__(self):
#         return '<Chat {0}>'.format(self.username)