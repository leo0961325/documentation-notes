

# io 相關

- 2018/08/13
- [Create and download a CSV file from a Flask view](https://stackoverflow.com/questions/28011341/create-and-download-a-csv-file-from-a-flask-view)

```py
# 只是 copy 過來, 程式碼還沒讀故...
import csv
from datetime import datetime
from cstringio import StringIO
from flask import Flask, stream_with_context
from werkzeug.datastructures import Headers
from werkzeug.wrappers import Response

app = Flask(__name__)

# example data, this could come from wherever you are storing logs
log = [
    ('login', datetime(2015, 1, 10, 5, 30)),
    ('deposit', datetime(2015, 1, 10, 5, 35)),
    ('order', datetime(2015, 1, 10, 5, 50)),
    ('withdraw', datetime(2015, 1, 10, 6, 10)),
    ('logout', datetime(2015, 1, 10, 6, 15))
]

@app.route('/')
def download_log():
    def generate():
        data = StringIO()
        w = csv.writer(data)

        # write header
        w.writerow(('action', 'timestamp'))
        yield data.getvalue()
        data.seek(0)
        data.truncate(0)

        # write each log item
        for item in log:
            w.writerow((
                item[0],
                item[1].isoformat()  # format datetime as string
            ))
            yield data.getvalue()
            data.seek(0)
            data.truncate(0)

    # add a filename
    headers = Headers()
    headers.set('Content-Disposition', 'attachment', filename='log.csv')

    # stream the response as the data is generated
    return Response(
        stream_with_context(generate()),
        mimetype='text/csv', headers=headers
    )

app.run()
```