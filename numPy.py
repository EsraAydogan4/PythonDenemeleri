import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Rastgele veri oluşturma
np.random.seed(0)
X = np.random.rand(50, 1) * 10
y = 2 * X + 1 + np.random.randn(50, 1) * 2

# Lineer regresyon modelini oluşturma
model = LinearRegression()
model.fit(X, y)

# Eğim (slope) ve kesme terimini elde etme
slope = model.coef_
intercept = model.intercept_

print("Eğim:", slope)
print("Kesme:", intercept)

# Veriyi modele uygulama
predicted_y = model.predict(X)

# Gerçek ve tahmin edilen değerlerin grafiği
plt.scatter(X, y, label='Gerçek Veri')
plt.plot(X, predicted_y, color='red', label='Tahmin Edilen Doğru')
plt.xlabel('X Değeri')
plt.ylabel('y Değeri')
plt.title('Lineer Regresyon')
plt.legend()
plt.show()
