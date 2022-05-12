import connection
import asyncio

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoibGVhbmRyb2NvcmlhMTlAZ21haWwuY29tIn0.tA0VMyJQKz5b6wk1dI3hkPIxfupEHw8LMyu-ngl80Ic'
newConnection = conecction.Connection(token)

try:
    asyncio.run(newConnection.start())
except KeyboardInterrupt:
    print('Exiting...')