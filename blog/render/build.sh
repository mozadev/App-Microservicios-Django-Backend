# sudo chmod -R 755 /ruta/a/tu/aplicacion
sudo chmod -R 755 ./blog

sudo mkdir -p /var/lib/apt/lists/partial
sudo mount -o remount,rw /var/lib/apt/lists/partial
apt-get update
#!/usr/bin/env bash
# Exit on error
set -o errexit

chown -R $(whoami) /var/lib/apt/lists/partial

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt
pip install wheel

# Convert static asset files
#python manage.py collectstatic --no-input

# Install system dependencies
apt-get update
apt-get install -y libsystemd-dev libsystemd-journal-dev

# Apply any outstanding database migrations
python manage.py migrate