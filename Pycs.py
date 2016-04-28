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

    def getunverifiedaccountwithdraws(self):
        """
		Gets a list of unverified Withdrawals for a Wallet.
		"""

    	data = {
        	"apiKey" : self.key
    	}

    	url = "/auth/getunverifiedaccountwithdraws"

    	return self.process(url,data)

    def newaccount(self,walletname,info):
        """
		Create a new Account/ Wallet.
		"""

    	data = {
        	"apiKey" : self.key,
			"walletName" : walletname,
			"info" : info
    	}

    	url = "/auth/newaccount"

    	return self.process(url,data)


    def sendtoaddress(self,fromwid,satoshis,msg,toaddress):
        """
		Sends Bitcoin to any On Chain Address. Fees of 0.0001 BTC is added to withdrawal amount.
		"""

    	data = {
        	"apiKey" : self.key,
			"fromWalletID" : fromwid,
			"satoshis" : satoshis,
			"msg" : msg,
			"toAddress" : toaddress
    	}

    	url = "/auth/sendtoaddress"

    	return self.process(url,data)


    def verifyaccountwithdrawcode(self,code):
        """
		Verifies a Withdrawal Code and processes the Transaction.
		"""

    	data = {
        	"apiKey" : self.key,
			"code" : code
    	}

    	url = "/auth/verifyaccountwithdrawcode"

    	return self.process(url,data)


    def cancelunverifiedaccountcoinwithdrawal(self,address,satoshis,withdrawid,reason):
        """
		Cancels an unverified Withdrawal Code the Transaction.
		"""

    	data = {
        	"apiKey" : self.key,
			"address" : address,
			"satoshis" : satoshis,
			"withdrawID" : withdrawid,
			"reason" : reason
    	}

    	url = "/auth/cancelunverifiedaccountcoinwithdrawal"

    	return self.process(url,data)


    def getaccountwithdrawverifycode(self,withdrawid):
        """
		Gets the account withdrawal Verification Code for a Withdraw ID.
		"""

    	data = {
        	"apiKey" : self.key,
			"withdrawID" : withdrawid
    	}

    	url = "/auth/getaccountwithdrawverifycode"

    	return self.process(url,data)


    def sendtotradeengine(self,fromwalletid,satoshis,msg):
        """
		Sends Bitcoin to Trade Engine. Can send as low as 1 satoshi.
		"""

    	data = {
        	"apiKey" : self.key,
			"fromWalletID" : fromwalletid,
			"satoshis" : satoshis,
			"msg" : msg
    	}

    	url = "/auth/sendtotradeengine"

    	return self.process(url,data)


    def newaddress(self,walletid,info):
        """
		Generates a new Bitcoin Address in an account/ wallet.
		"""

    	data = {
        	"apiKey" : self.key,
			"walletID" : walletid,
			"info" : info
    	}

    	url = "/auth/newaddress"

    	return self.process(url,data)

	
