echo [$(date)]: "START"
echo [$(date)]: "Creating env with python=3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "Activating env"
source activate ./env
echo [$(date)]: "Installing requirements"
pip install -r requirements.txt
echo [$(date)]: "END"