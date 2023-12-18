import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):

        addresses_regex = re.findall(r'\S+@\S+', self.email_addresses)        
        
        addresses_split = [address.strip() for address in re.split(r'[,\s]+', self.email_addresses) if address and '@' in address]
        
        unique_addresses = sorted(set(addresses_regex + addresses_split))

        return unique_addresses