if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/k-n-o-x/EvaMaria2 /EvaMaria2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /EvaMaria2
fi
cd /EvaMaria2
pip3 install -U -r requirements.txt
echo "Starting EvaMaria2...."
python3 bot.py
