import configparser

def generate_config(config_file):
    config = configparser.ConfigParser(interpolation=None)
    config["Emon"] = {}

    # EmonPi Section
    print("--- Configure EmonPi ---")

    # IP
    default = "127.0.0.1"
    temp = input(f"IP of EmonPi ({default}): ")
    emon_ip = temp if temp else default

    # Bearer Credentials
    bearer_credentials = input("EmonPi Bearer Credentials (only the hash): ")
    if not bearer_credentials:
        bearer_credentials = "REPLACE_ME"
        print("Bearer Credentials cannot be omitted. This will cause trouble!")
        print(f"Please refer to http://{emon_ip}/feed/api, look up for the API-Key")
        print("and replace it in the generated config file.")
        input("Press enter to continue...")

    config["Emon"]["endpoint"] = f"http://{emon_ip}"
    config["Emon"]["bearer_credentials"] = bearer_credentials

    with open(config_file, "w", encoding="utf8") as f_out:
        config.write(f_out)

    print(f"Config file was successfully generated at: {config_file}")
