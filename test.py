import db

message = '456'
message_id = '12345'
db.data_base_update("UPDATE users SET personal_account = '{}' WHERE \"personal_account\" IS NULL".format(message))