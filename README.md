# Today

Simple container to return the date and time. 

## Usage
To start the container run the follow command:

```bash
docker run -p 3000:3000 gsdenys/today:v2.0
```

you also start it in a custom port like:

```bash
docker run -e SYSTEM_PORT=5000 -p 5000:5000 gsdenys/today:v2.0
```

then access [http://\<host\>:\<port\>/\<anything\>](http://localhost:5000/today)

the response should be

```json
{
    "date": "11/06/2021",
    "time": "00:25:00"
}
```