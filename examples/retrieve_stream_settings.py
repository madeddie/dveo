#!/usr/bin/env python
"""Basic usage example of the DVEO API module.

No variables given, outputs json string of all collected data.
"""

import argparse
import getpass
import json
import os
import re
import sys

from dveo import API

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Retrieve stream source and target settings."
    )
    parser.add_argument("encoder", nargs="+", help="address(es) of encoder(s) to query")
    parser.add_argument(
        "--format",
        choices=["json", "xml"],
        default="xml",
        help="xml or json format of API query results (used internally,default: xml)",
    )
    args = parser.parse_args()

    encoders = args.encoder
    data_format = args.format
    if os.environ.get("DVEO_PASSWORD"):
        password = os.environ.get("DVEO_PASSWORD")
    else:
        password = getpass.getpass()
    if not password:
        sys.exit("Set env variable DVEO_PASSWORD or type interactively.")

    input_config_keys = ("inputname", "inputmulticastip", "localport", "startmode")
    other_keys = ("encoder", "inputid", "status")
    output_config_keys = (
        "streamname",
        "rtmptargeturi",
        "rtmptargetstreamname",
        "program",
        "streamenabled",
    )
    all_config = list()
    all_config.append(list(input_config_keys + other_keys + output_config_keys))

    for encoder in encoders:
        dveo = API(encoder, password, data_format=data_format)
        for input_id in dveo.list_inputs():
            input_status = re.sub(" \d+", " X", dveo.service_status(input_id))
            input_config = dveo.input_config(input_id)
            if not input_config.get("inputname"):
                continue

            output_list = dveo.list_outputs(input_id)
            # If there are no outputs, add line with empty values
            # With a single output, add line with all values
            # With multiple ouputs, add multiple lines, repeat input values
            if any(output_list):
                for output_name in output_list:
                    stream_config = list()
                    output_config = dveo.output_config(input_id, output_name)
                    stream_config.extend(
                        [input_config.get(key, "") for key in input_config_keys]
                    )
                    stream_config.append(encoder)
                    stream_config.append(input_id)
                    stream_config.append(input_status)
                    stream_config.extend(
                        [output_config.get(key, "") for key in output_config_keys]
                    )

                    all_config.append(stream_config)
            else:
                stream_config = list()
                output_config = dict()
                stream_config.extend(
                    [input_config.get(key, "") for key in input_config_keys]
                )
                stream_config.append(encoder)
                stream_config.append(input_id)
                stream_config.append(input_status)
                stream_config.extend(
                    [output_config.get(key, "") for key in output_config_keys]
                )

                all_config.append(stream_config)

    print(all_config)
    with open("stream_config_output.json", "w") as outputfile:
        outputfile.write(json.dumps(all_config, indent=2, sort_keys=True))
