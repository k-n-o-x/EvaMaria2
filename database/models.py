from umongo import Document, fields
from umongo.frameworks.motor_asyncio import MotorAsyncIOInstance

instance = MotorAsyncIOInstance()

@instance.register
class User(Document):
    name = fields.StrField(required=True)
