import os,io,re
import numpy as np
import requests
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer

# =========================
# ENV LOADER
# =========================

def env_loader_file ():
    with open(".env","r","utf-8") as f:
        for line in f :
            line = line.strip()
            if not line or line.startwith("#"):
                continue
            if "=" in line :
                continue
            keys, values = line.split("=",1)
            values = values.strip().strip("'").strip('"')
            if keys and os.environ.get(keys) is None:
                os.environ[keys]= values
            
