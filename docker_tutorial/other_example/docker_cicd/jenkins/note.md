進容器取密碼
cat /var/jenkins_home/secrets/initialAdminPassword
docker exec -it jenkins-jenkins-1 cat /var/jenkins_home/secrets/initialAdminPassword

0bba25a73153492f909d61588d143578

權限設置
sudo chown -R 1000:1000 workspace/