import argparse

from .service import run
from .setup.generate_schema import generate_schema

parser = argparse.ArgumentParser(prog="CleanEmonPopulator", description="The CLI for CleanEmon-Populator")
subparsers = parser.add_subparsers(dest="command", help='commands')

# Service
service_parser = subparsers.add_parser("service", help="Run a service")
service_parser.add_argument("service_name", action="store", choices=["populate"])

# Script
script_parser = subparsers.add_parser("script", help="Run a script")
script_parser.add_argument("script_name", action="store", choices=["setup"])

# Generate Schema
subparsers.add_parser("generate-schema", help="Generate the schema file")
script_parser.add_argument("script_name", action="store", choices=["setup"])

args = parser.parse_args()

if args.command == "service":
    if args.service_name == "populate":
        run()

elif args.command == "generate-schema":
    generate_schema()
