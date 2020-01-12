
class scheme_class:

    def __init__(self, so_code: str, sr_code: str, policy_no: str, policy_holder_address: str, 
        issue_date: str, risk_date: str, next_due: str, m: str, tb: int, premium: int, 
        sum_assumed: str, status):

        self.__so_code = so_code
        self.__sr_code = sr_code
        self.__policy_no = policy_no                  
        self.__policy_holder_address = policy_holder_address        
        self.__issue_date = issue_date                   
        self.__risk_date = risk_date                   
        self.__next_due = next_due                    
        self.__m = m                           
        self.__tb = tb                        
        self.__premium = premium                     
        self.__sum_assumed = sum_assumed                 
        self.__status = status                     
    
    def get_so_code(self) -> str:
        return self.__so_code
    
    def get_sr_code(self) -> str:
        return self.__sr_code

    def get_policy_no(self) -> str:
        return self.__policy_no

    def get_policy_holder_address(self) -> str:
        return self.__policy_holder_address

    def get_issue_date(self) -> str:
        return self.__issue_date

    def get_risk_date(self) -> str:
        return self.__risk_date

    def get_next_due(self) -> str:
        return self.__next_due

    def get_m(self) -> str:
        return self.__m

    def get_tb(self) -> int:
        return self.__tb

    def get_premium(self) -> int:
        return self.__premium

    def get_sum_assumed(self) -> str:
        return self.__sum_assumed

    def get_status(self) -> str:
        return self.__so_code
