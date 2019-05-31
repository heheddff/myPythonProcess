from account_extraction import AccountExtraction
from ip_filter import IpFilter

file = "/usr/local/nginx/htdocs/goaccess/0528/account.log"
m = AccountExtraction(file)
m.main()

# ip_filter = IpFilter("logs/basic_info.log")
# ip_filter.main()