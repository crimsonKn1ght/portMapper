# portMapper
Port Scanner

Download the tool with following command from shell:
```
https://github.com/confusedHatHacker/portMapper
```

After cloning change directories and go to dirEnum folder. Run the following command from shell:
```
pip install -r requirements.txt
```

Usage: `python portMapper.py -i <ip> -p <ports range>`

options:
```
  -h, --help     show this help message and exit
  -i , --ip      Enter ip
  -p , --ports   Enter port range
  -v, --version  Show version of portMapper.py
```

Examples:
```
python portMapper.py -i 192.168.0.1 -p 200-300
python portMapper.py -i 192.168.0.1 -p 100-400,443
```
