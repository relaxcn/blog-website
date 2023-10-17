import os, tarfile, paramiko, shutil


if __name__ == '__main__':
    public_dir_path = "./public"
    targz_file_path = "./public.tar.gz"
    
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)
    if os.path.exists(targz_file_path):
        os.remove(targz_file_path)
    
    os.system("hugo -D")
    
    with tarfile.open(targz_file_path, "w:gz") as tar:
        tar.add(public_dir_path, arcname=os.path.basename(public_dir_path))
    
    
    hostname = "117.50.163.96"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname,
      port=22,
      username='root')
    sftp = ssh.open_sftp()
    
    ssh.exec_command("rm -rf /www/wwwroot/www.chens.life/*")
    print(os.getcwd() + "/" + targz_file_path[2:])
    sftp.put(os.getcwd() + "/" + targz_file_path[2:], "/www/wwwroot/www.chens.life/public.tar.gz", callback=None, confirm=True)
    # print("tar zxvf /www/wwwroot/www.chens.life/public.tar.gz -C /www/wwwroot/www.chens.life/")
    _, stdout, stderr = ssh.exec_command("tar zxvf /www/wwwroot/www.chens.life/public.tar.gz -C /www/wwwroot/www.chens.life/", timeout=10)
    
    print(stdout.read().decode('utf-8'))
    shutil.rmtree(public_dir_path)
    os.remove(targz_file_path)
    os.system(".\\gitupdate.bat")
    
