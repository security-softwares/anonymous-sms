echo "updating"
rm -rf anonymous-sms
git clone https://github.com/security-softwares/anonymous-sms/
cd anonymous-sms
python3 sms.py
