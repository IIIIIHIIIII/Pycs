import requests
import json

class CSError(Exception):
    pass


class Pycs:

    def __init__(self, apikey, wid):
        self.key = apikey
        self.wid = wid

    def process(self,url,data):
        response = requests.post("https://api.coinsecure.in/v0%s" %(url), 
                            data=json.dumps(data), 
                            headers={"content-type":"text/json"}).json()

        if "error" in response.values() or "error" in response.keys(): 
            message = response["error"] if("error" in response.keys()) else response["message"]
            raise CSError(message)

        if "result" in response.keys() and "error" in response["result"][0]:
            message = response["result"][0]["error"]
            raise CSError(message)        
    
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


    def getmaxuserbid(self):
        """
        Returns highest bid details from users orders.
        """

        data = {
            "apiKey" : self.key
        }

        url = "/auth/getmaxuserbid"
        return self.process(url,data)


    def cancelleduserasks(self):
        """
        Returns all cancelled Ask Orders in Json. The Rate is displayed paisa
        and Volume in Satoshis.
        """

        data = {
            "apiKey" : self.key
        }

        url = "/auth/cancelleduserasks"
        return self.process(url,data)

    def completeduserasks(self):
        """
        Returns all completed ask Orders in Json. The Rate is displayed in
        Paisa and Volume in Satoshis.
        """

        data = {
            "apiKey" : self.key
        }

        url = "/auth/completeduserasks"
        return self.process(url,data)


    def cancelleduserbids(self):
        """
        Returns all cancelled Bid Orders in Json. The Rate is displayed in
        Paisa and Volume in SAtoshis.
        """

        data = {
            "apiKey" : self.key
        }

        url = "/auth/cancelleduserbids"
        return self.process(url,data)

    def alluserasks(self):
        """
        Returns all User Asks Orders in Json. The Rate is displayed in Paisa
        and Volume in Satoshis.
        """

        data = {
            "apiKey" : self.key
        }
        
        url = "/auth/alluserasks"
        return self.process(url,data)

    def completeduserbids(self):
        """
        Returns all completed Bid Orders in Json. The RAte is displayed in
        Paisa and Volume in Satoshis.
        """

        data = {
            "apiKey" : self.key
        }

        url = "/auth/completeduserbids"
        return self.process(url,data)

    
    def alluserbids(self):
        """
        Returns all User Bid Orders in Json. The Rate is displayed in 
        Paisa and Volume in Satoshis.
        """

        data = {
            "apiKey" : self.key
        }

        url = "/auth/alluserbids"
        return self.process(url,data)


    def getminuserask(self):
        """
        Returns lowest ask details from users orders.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/getminuserask"
        return self.process(url,data)


    def getunverifiedcoinwithdraws(self):
        """
        Returns all unverified coin withdrawal data. This call is needed to
        get withdrawID for getcoinverifycode()
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/getunverifiedcoinwithdraws"
        return self.process(url,data)

    def voucherdetails(self,vochercode):
        """
        Returns the Details of any Coinsecure Vocher
        """
    
        data = {
            "apiKey" : self.key,
            "vouchercode" : vochercode
        }

        url = "/auth/voucherdetails"
        return self.process(url,data)


    def getfiatbankdetails(self):
        """
        Returns users INR Account Bank details
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/getfiatbankdetails"
        return self.process(url,data)


    def intradecoinbalance(self):
        """
        Returns users in trade or pending coin balance in satoshi.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/intradecoinbalance"
        return self.process(url,data)


    def getcoinverifycode(self,withdrawid):
        """
        Returns the final code that can be used to verify the payment.
        You can get the withdrawID from getunverifiedcoinwithdraws()
        """
    
        data = {
            "apiKey" : self.key,
            "withdrawID" : withdrawid
        }

        url = "/auth/getcoinverifycode"
        return self.process(url,data)


    def getunverifiedfiatwithdraws(self):
        """
        Returns unverified fiat withdrawal details for a user.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/getunverifiedfiatwithdraws"
        return self.process(url,data)

    def fiatfeepercentage(self):
        """
        Returns users fiat fee in percentage.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/fiatfeepercentage"
        return self.process(url,data)

    def intradefiatbalance(self):
        """
        Returns users in trade or pending fiat balance in satoshi.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/intradefiatbalance"
        return self.process(url,data)


    def actualfiatbalance(self):
        """
        Returns users total fiat balance in paisa.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/actualfiatbalance"
        return self.process(url,data)


    def getcoinaddresses(self):
        """
        Returns users bitcoin deposit addresses.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/getcoinaddresses"
        return self.process(url,data)

    def coinbalance(self):
        """
        Returns users usable coin balance in satoshi.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/coinbalance"
        return self.process(url,data)


    def actualcoinbalance(self):
        """
        Returns users total coin balance in paisa.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/actualcoinbalance"
        return self.process(url,data)

    def coinfeepercentage(self):
        """
        Returns users coin fee in percentage.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/coinfeepercentage"
        return self.process(url,data)

    def getfiatverifycode(self,withdrawid):
        """
        Returns the fiat withdrawal verification code.
        """
    
        data = {
            "apiKey" : self.key,
            "withdrawID" : withdrawid
        }

        url = "/auth/getfiatverifycode"
        return self.process(url,data)


    def fiatbalance(self):
        """
        Returns users usable fiat balance in paisa.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/fiatbalance"
        return self.process(url,data)


    def sendcoin(self,satoshis,toaddr,msg):
        """
        Send Coins to any valid address. The result needs to be used to 
		call getcoinverifycode()
        """
    
        data = {
            "apiKey" : self.key,
			"satoshis" : satoshis,
			"toAddr" : toaddr,
			"msg" : msg
        }

        url = "/auth/sendcoin"
        return self.process(url,data)


    def createask(self,rate,vol):
        """
        Create a new ask order. KYC & Bank Link must be complete.
        """
    
        data = {
            "apiKey" : self.key,
			"rate" : rate,
			"vol" : vol
        }

        url = "/auth/createask"
        return self.process(url,data)


    def cancelbid(self,orderid):
        """
        Cancel bid order. You can get your OrderID from alluserbids.
        """
    
        data = {
            "apiKey" : self.key,
			"orderID" : orderid
        }

        url = "/auth/cancelbid"
        return self.process(url,data)


    def withdrawfiat(self,fiat,acctnickname,msg):
        """
        Send fiat to a bank account. The result needs to be used to call
		getfiatverifycode()
        """
    
        data = {
            "apiKey" : self.key,
			"fiat" : fiat,
			"acctNickName" : acctnickname,
			"msg" : msg
        }

        url = "/auth/withdrawfiat"
        return self.process(url,data)


    def createbid(self,rate,vol):
        """
        Create a new Bid Order. KYC & Bank Link must be complete.
        """
    
        data = {
            "apiKey" : self.key,
			"rate" : rate,
			"vol" : vol
        }

        url = "/auth/createbid"
        return self.process(url,data)

    def cancelunverifiedfiatwithdrawal(self,address,satoshis,withdrawid,reason):
        """
        Verifies the coin withdrawal Request. You can get the unverified codes
		from getunverifiedfiatwithdraws.
        """
    
        data = {
            "apiKey" : self.key,
			"address" : address,
			"satoshis" : satoshis,
			"withdrawID" : withdrawid,
			"reason" : reason
        }

        url = "/auth/cancelunverifiedfiatwithdrawal"
        return self.process(url,data)


    def cancelask(self,orderid):
        """
        Cancels the ask order. You can get your OrderID from alluserasks.
        """
    
        data = {
            "apiKey" : self.key,
			"orderID" : orderid
        }

        url = "/auth/cancelask"
        return self.process(url,data)


    def redeemvoucher(self,vouchercode,pin):
        """
        Redeems a Coinsecure Voucher. Pin can be sent only if needed
		else can be avoided from the request.
        """
    
        data = {
            "apiKey" : self.key,
			"vouchercode" : vouchercode,
			"pin" : pin
        }

        url = "/auth/redeemvoucher"
        return self.process(url,data)


    def verifyfiatwithdrawal(self,code):
        """
        Verifies the coin withdrawal request. You can get the unverified codes
		from getunverifiedfiatwithdraws()
        """
    
        data = {
            "apiKey" : self.key,
			"code" : code
        }

        url = "/auth/verifyfiatwithdrawal"
        return self.process(url,data)


    def allbankdata(self):
        """
        Returns a short summary of bank data & account related information.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/allbankdata"
        return self.process(url,data)


    def timeline(self):
        """
        Returns timeline data. This data shows a comprehensive list of all
		Transactions of the user.
        """
    
        data = {
            "apiKey" : self.key
        }

        url = "/auth/timeline"
        return self.process(url,data)


    def verifycoinwithdrawal(self,code):
        """
        Verifies the coin withdrawal request. You can get the unverified codes
		from getunverifiedcoinwithdraws()
        """
    
        data = {
            "apiKey" : self.key,
			"code" : code
        }

        url = "/auth/verifycoinwithdrawal"
        return self.process(url,data)


    def cancelunverifiedcoinwithdrawal(self,address,satoshis,withdrawid,reason):
        """
        Verifies the coin withdrawal request. You can get the unverified codes
		from getunverifiedcoinwithdraws.
        """
    
        data = {
            "apiKey" : self.key,
			"address" : address,
			"satoshis" : satoshis,
			"withdrawID" : withdrawid,
			"reason" : reason
        }

        url = "/auth/cancelunverifiedcoinwithdrawal"
        return self.process(url,data)
