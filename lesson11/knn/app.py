from flask import Blueprint,render_template, jsonify,request
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

knn_bp = Blueprint(
    'knn',
    __name__,
    url_prefix='/knn',
    template_folder='../templates',
    static_folder='../static'
)

@knn_bp.route('/knn_index')
def knn_index():
    return render_template('knn.html')

@knn_bp.route('/api/data')
def knn_data():
    """knn 分類 API - 使用鳶尾花資料集"""
    iris = load_iris()
    print(iris)
    return jsonify({'sucess':True})

@knn_bp.route('/api/predict')
def knn_predict():
    return jsonify({'sucess':True})
