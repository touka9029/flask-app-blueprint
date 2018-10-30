# use flask Blueprint

exec `make_flask.sh`
access: 
`http://localhost:5000` -> hello world!
`http://localhost:5000/blue/blue01` -> blue01
`http://localhost:5000/blue/blue02` -> blue02

## alternate url_prefix

```python
for bp in bp_list:
    app.register_blueprint(bp, url_prefix='/blue')
```

register_blueprint() docs: http://flask.pocoo.org/docs/1.0/api/#flask.Flask.register_blueprint
Blueprint() docs: http://flask.pocoo.org/docs/1.0/api/#flask.Flask.register_blueprint
