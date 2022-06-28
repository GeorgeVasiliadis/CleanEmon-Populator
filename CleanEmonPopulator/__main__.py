import argparse

from .service import run
from .setup import setup

parser = argparse.ArgumentParser(prog="CleanEmonPopulator", description="The CLI for CleanEmon-Populator")
subparsers = parser.add_subparsers(help='commands')

# Service
populate_parser = subparsers.add_parser("service", help="Run a service")
populate_parser.add_argument("service_name", action="store", choices=["populate"])

# Script
script_parser = subparsers.add_parser("script", help="Run a script")
script_parser.add_argument("script_name", action="store", choices=["setup"])

args = parser.parse_args()
print(args)

if args.service_name:
    if args.service_name == "populate":
        run()

elif args.script_name:
    if args.script_name == "setup":
        setup()
