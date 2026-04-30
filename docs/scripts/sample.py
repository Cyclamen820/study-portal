#%%
import numpy as np
import matplotlib.pyplot as plt
import os

# x軸のデータ（周波数や波数などのイメージ）
x = np.linspace(-10, 10, 500)

# ガウス関数（ドップラー広がりなどのモデル）
def gaussian(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

# ローレンツ関数（圧力広がりなどのモデル）
def lorentzian(x, x0, gamma):
    return (1 / (np.pi * gamma)) * (gamma**2 / ((x - x0)**2 + gamma**2))

# グラフの描画設定
plt.figure(figsize=(8, 5))

# それぞれの関数をプロット
plt.plot(x, gaussian(x, 0, 1.5), label='Gaussian (Doppler)', color='#3498db', linewidth=2)
plt.plot(x, lorentzian(x, 0, 1.5), label='Lorentzian (Pressure)', color='#e74c3c', linestyle='--', linewidth=2)

# グラフの装飾
plt.title('Comparison of Spectral Line Profiles', fontsize=14)
plt.xlabel('Frequency / Wavenumber', fontsize=12)
plt.ylabel('Intensity / Arbitrary Units', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
# === ここから保存先の指定 ===
# sample.py のある場所(scripts)から見て、1つ上の階層(docs)にある images フォルダを指定
script_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(script_dir, '..', 'images')

# imagesフォルダが存在しない場合は自動で作成
os.makedirs(save_dir, exist_ok=True)

# 画像を保存
save_path = os.path.join(save_dir, 'profile_plot.png')
plt.savefig(save_path, dpi=300, bbox_inches='tight')

# 画面に表示
plt.show()
# %%
