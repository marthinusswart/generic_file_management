from flask_restful import Resource
from flask import request, current_app, jsonify
from werkzeug.utils import secure_filename
import os
import uuid


class Files(Resource):
    def get(self, tenant_key):
        #from .models.generic_file_management_models import User
        #users = User.query.filter_by(tenant_key=tenant_key)
        #result = [u.as_json() for u in users]
        # print(tenant_key)
        # return jsonify(result)
        return {'result': 'Not implemented yet'}

    def post(self, tenant_key):
        if 'file' not in request.files:
            return {'result': 'No file provided to uploaded'}, 404

        uploaded_file = request.files['file']

        if uploaded_file.filename == '':
            return {'result': 'No file provided to uploaded'}, 404

        upload_directory = os.path.join(
            current_app.config['UPLOAD_FOLDER'], tenant_key)

        if not os.path.exists(upload_directory):
            print('Tenant directory does not exist, creating it.')
            os.makedirs(upload_directory)

        if uploaded_file and self.allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            unique_id = str(uuid.uuid1())
            ext = filename.rsplit('.', 1)[1].lower()
            filename = unique_id + '.' + ext
            full_path = os.path.join(upload_directory, filename)
            uploaded_file.save(full_path)

            from . import db
            from .models.generic_file_management_models import File

            new_file = File()
            new_file.filename = filename
            new_file.relative_path = upload_directory
            new_file.filesize = os.stat(full_path).st_size
            new_file.fileext = ext
            new_file.tenant_key = tenant_key
            db.session.add(new_file)
            db.session.commit()

            new_json_file = new_file.as_json()

        return {'result': 'File uploaded successfully', 'file': new_json_file}

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


class FileManagement(Resource):
    def get(self, tenant_key, file_id):
        from .models.generic_file_management_models import File
        db_file = File.query.filter_by(
            tenant_key=tenant_key, id=file_id).first()

        if not db_file:
            return {'result': 'No file by that id', 'Id received': file_id}, 404

        return jsonify(db_file.as_json())

    def put(self, tenant_key, file_id):
        from . import db
        from .models.generic_file_management_models import File
        db_file = File.query.filter_by(
            tenant_key=tenant_key, id=file_id).first()

        if not db_file:
            return {'result': 'No file by that id', 'Id received': file_id}, 404

        file_json = request.get_json()
        db_file.description = file_json['description']

        db.session.commit()
        return {'result': 'File updated', 'JSON received': file_json}

    def delete(self, tenant_key, file_id):
        from . import db
        from .models.generic_file_management_models import File
        db_file = File.query.filter_by(
            tenant_key=tenant_key, id=file_id).first()

        if not db_file:
            return {'result': 'No file by that id', 'Id received': file_id}, 404

        file_exists = True

        file_on_disk = db_file.relative_path + '/' + db_file.filename
        if os.path.exists(file_on_disk):
            os.remove(file_on_disk)
        else:
            file_exists = False

        db.session.delete(db_file)
        db.session.commit()

        if (file_exists):
            return {'result': 'File deleted', 'Id received': file_id}
        else:
            return {'result': 'File exists in the database but does not exist on the server, deleted from the database only', 'Id received': file_id}
