import sys
from flask import Flask
from requests import get

def server_running():
     return get('https://api.ipify.org').text

def main():
  app = Flask(__name__)
  app.add_url_rule('/', view_func=server_running)

  app.run(host= '0.0.0.0', port=80)
  print ('exiting...')
  sys.exit(0)

if __name__ == '__main__':
  main()