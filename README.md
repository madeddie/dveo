DVEO REST API wrapper for Python
================================

This module tries to make using the [DVEO][dveo] REST API easier to use with Python.

Example of usage:

```{.sourceCode .python}
>>> from dveo import API
>>> dveo = API('203.0.113.12', 'p455w0rd')
>>> dveo.system_status()['system']['uptime']
OrderedDict([('days', '20'), ('hours', '7'), ('mins', '51')])
>>> dveo.list_inputs()
['net_stream1', 'net_stream2', 'net_stream3', 'net_stream4', ...]
>>> dveo.input_config('net_stream2')['inputname']
'BigTV'
>>> dveo.input_by_output_param('rtmptargeturi', 'acme', partial=True, include_value=True)
[('net_stream1', 'rtmp://vid1.acme.net/stream'), ('net_stream2', 'rtmp://stream10.acme.com/rtmp'), ('net_stream3', 'rtmp://stream11.acme.com/rtmp'), ...]
```

Check out the variables and commands of your DVEO device API on `http(s)://YOURDVEODEVICE:25599/metadata`. The URL isn't protected. The port is set in the DVEO configuration.

Installation
------------

``` {.sourceCode .bash}
$ pipenv install dveo
```

Example scripts
---------------

In the `examples` directory you'll find some implementation examples.

- `retrieve_stream_settings.py` loads input and output settings for one or more encoders and prints them and writes them to a json file.

[dveo]: https://dveo.com/