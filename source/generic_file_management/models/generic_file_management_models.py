from generic_file_management import db


class File(db.Model):
    __tablename__ = 'generic_file'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(150))
    description = db.Column(db.String(150))
    relative_path = db.Column(db.String(150))
    filesize = db.Column(db.Integer)
    fileext = db.Column(db.String(150))
    tenant_key = db.Column(db.String(100))

    def as_json(self):
        return {
            'id': self.id,
            'filename': self.filename,
            'description': self.description,
            'relative_path': self.relative_path,
            'filesize': self.filesize,
            'fileext': self.fileext,
            'tenant_key': self.tenant_key
        }
