from .serviceUtils import *
import argparse

registry = {"super_resolution_service": {"grpc": 7016, "snetd": 7017}}


def common_parser(script_name):
    parser = argparse.ArgumentParser(prog=script_name)
    service_name = os.path.splitext(os.path.basename(script_name))[0]
    parser.add_argument(
        "--grpc-port",
        help="port to bind gRPC service to",
        default=registry[service_name]["grpc"],
        type=int,
        required=False,
    )
    return parser