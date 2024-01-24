import subprocess
from datetime import datetime

def backup_to_remote(source_path, remote_user, remote_host, remote_path):
    try:
        # Create a timestamp for the backup folder
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        backup_folder = f'backup_{timestamp}'

        # Use rsync to copy the directory to the remote server
        rsync_command = f'rsync -avz -e ssh {source_path} {remote_user}@{remote_host}:{remote_path}/{backup_folder}'
        subprocess.run(rsync_command, shell=True, check=True)

        print(f'Success: Backup created at {remote_host}:{remote_path}/{backup_folder}')
        return True
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')
        return False

# Example usage:
source_directory = '/path/to/source'
remote_user = 'your_remote_user'
remote_host = 'your_remote_host'
remote_path = '/path/to/remote/backup'

backup_to_remote(source_directory, remote_user, remote_host, remote_path)
