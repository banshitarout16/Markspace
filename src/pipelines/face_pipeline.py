import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st


from src.database.db import get_all_students