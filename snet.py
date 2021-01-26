import socket
import http.client
import urllib.parse,urllib.request, urllib.error
import re
import dns.resolver

#HTTP CODES
HTTP_OK =[http.client.OK,http.client.FOUND,http.client.MOVED_PERMANENTLY]


#Function to get ip
def get_IP(url):
	try:
		print("IP address of %s:%s"%(url,socket.gethostbyname(url)))  
	except socket.error as err_msg:
		print("%s: %s"%(url,err_msg))


def get_info(url):
	url='https://'+url
	host,path = urllib.parse.urlparse(url)[1:3]
	try:
		conn=http.client.HTTPConnection(host)

		conn.request('HEAD',path)
		return conn.getresponse().status

	except Exception as e:
		print("Server: %s status is: %s\n" %(url,e))

		return None


#Function to get Dns Record
def get_dns(url):
	ids =['NONE','A','NS','CNAME','MX','AAAA','PTR','CERT','TXT',]
	for a in ids:
		try:
			result= dns.resolver.resolve(url,a)
			for x in result:
				print(a,':',x.to_text())
		except Exception as e:
			print(e)


if __name__ == '__main__':
	
	url=input("Enter url:")
	get_IP(url)
	if get_info(url) in HTTP_OK:
		print("Server: %s status is OK: %s\n" %(url, get_info(url)))
	else:
		print("Server: %s status is NOT OK: %s\n"%(url,get_info(url)))

	get_dns(url)