import requests
import json

class Pycs:

    def __init__(self, apikey, wid):
        self.key = apikey
        self.wid = wid

    def process(self,url,data):
        try:
            response = requests.post("https://api.coinsecure.in/v0%s" %(url), 
                                    data=json.dumps(data), 
                                    headers={"content-type":"text/json"}).json()

            if "error" in response.values() or "error" in response.keys(): 
                raise Exception()

            return response

        except Exception:
            message = response["error"] if("error" in response.keys()) else response["message"]	
            print "Error: ",message

        return response

    def getallaccountsconfirmedbalance(self):
        """
                Gets the total confirmed balance across all accounts and addresses
        """

        data = {
                "apiKey" : self.key
        }

        url = "/auth/getallaccountsconfirmedbalance"

        return self.process(url,data)

    def getaccountconfirmedbalance(self):
        """
                Gets the confirmed balance on an account/ wallet.
        """

        data = {
                "apiKey" : self.key,
                "walletID" : self.wid
        }

        url = "/auth/getaccountconfirmedbalance"

        return self.process(url,data)

    def getaccounts(self):
        """
                Gets all users accounts/ wallet details.
        """

        data = {
                "apiKey" : self.key
        }

        url = "/auth/getaccounts"

        return self.process(url,data)

    def getallaccountsunconfirmedbalance(self):
        """
    	Gets the total unconfirmed balance across all accounts and addresses
		"""

    	data = {
        	"apiKey" : self.key
    	}

    	url = "/auth/getallaccountsunconfirmedbalance"

        return self.process(url,data)

    def getaccountaddresses(self):
        """
    	Gets the Bitcoin address based on account/ wallet name.
		"""

    	data = {
        	"apiKey" : self.key,
			"walletID" : self.wid
    	}

    	url = "/auth/getaccountaddresses"

    	return self.process(url,data)

    def getaddressunconfirmedbalance(self,address):
        """
    	Gets the total unconfirmed balance on a user addresses.
		"""

    	data = {
        	"apiKey" : self.key,
        	"address" : address
    	}

    	url = "/auth/getaddressunconfirmedbalance"

    	return self.process(url,data)

    def getaccountunconfirmedbalance(self):
        """
   		Gets the unconfirmed balance on an account/ wallet.
		"""

    	data = {
        	"apiKey" : self.key,
        	"walletID" : self.wid
    	}

    	url = "/auth/getaccountunconfirmedbalance"

    	return self.process(url,data)

    def getaddressconfirmedbalance(self,address):
        """
   		Gets the total confirmed balance on a user addresses
		"""

    	data = {
        	"apiKey" : self.key,
        	"address" : address
    	}

    	url = "/auth/getaddressconfirmedbalance"

    	return self.process(url,data)

