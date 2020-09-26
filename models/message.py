from datetime import datetime
from db import db
from models.board import Board


class Message(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    part_id = db.Column(db.Integer, db.ForeignKey('part.id'))

    def set_part_id(self):
        board = Board.query.get(self.board_id)
        parts = board.parts
        tag_content = self.content.split()[0]

        for part in parts:
            if tag_content == part.tag:
                self.content = ' '.join(self.content.split()[1:])
                self.part_id = part.id
                break
