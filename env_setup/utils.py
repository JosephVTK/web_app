from pprint import pformat

class Response:
    def __init__(self, key) -> None:
        self.key = key
    
BACK = Response("Back")

def get_string(query, default=None):
    while True:
        if default:
            print (f"Default: [{default}]")
        response = input(f"{query}\n> ")

        if response == "" and default:
            return default

        confirm = input (f"...\n{response}\n...\nIs this correct? (Y/N) > ")
        if confirm.lower() == 'y':
            return response

def get_from_options(options, default=None):
    while True:
        if default:
            print (f"Default: [{default}]")
            
        response = input(f'{pformat ([ f"{x + 1}: {option}" for x, option in enumerate(options) ] + ["0: Back"], indent=4)}\n > ')
        
        if response == "" and default:
            return default
        
        try:
            reponse_int = int(response)
        except:
            input ("Invalid response..\nPress Enter")
            continue

        if reponse_int == 0:
            return BACK

        if reponse_int < 1 or reponse_int > len(options):    
            input ("Invalid response..\nPress Enter")       
            continue          

        return options[reponse_int - 1]
    