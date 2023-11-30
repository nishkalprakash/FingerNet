## Create conda Evironment
```bash
conda create -n fingernet python=3.10 tensorflow
conda activate fingernet
pip install -r requirements.txt
```

## delete the environment
```bash
conda deactivate
conda remove --name fingernet --all
```