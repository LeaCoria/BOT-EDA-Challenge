import connection
import asyncio

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiTGVhQ29yaWEwMDEifQ.41K46CdQ6MpSq4RrucdDxt8LhPax_XRUXo8ac2dpj80"
newConnection = connection.Connection(token)

try:
    asyncio.run(newConnection.start())
except KeyboardInterrupt:
    print('Exiting...')