
https://github.com/appleboy/drone-ssh

```bash
$# USER=python
$# KEY_FILE=${HOME}/.ssh/python_team_rsa
$# HOST=172.0.10.40
$# drone-ssh -u ${USER} -h ${HOST} -i ${KEY_FILE} -s "ls -l"
```