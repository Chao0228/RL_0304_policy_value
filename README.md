# Grid World: Value Iteration & Policy Extraction

這是一個基於強化學習（Reinforcement Learning）基礎概念開發的網格世界（Grid World）互動式網頁應用程式。使用者可以自訂地圖大小、設定起點與終點，並透過價值迭代（Value Iteration）演算法自動計算出避開障礙物的最佳路徑策略。

## 🌟 專案功能 (Features)

* **動態網格生成**：支援 $n \times n$ 的網格自訂大小（預設支援 $3 \le n \le 9$）。
* **互動式地圖設定**：使用者可透過滑鼠點擊依序設定：
    * 🟩 **起點 (Start)**：綠色標記
    * 🟥 **終點 (End)**：紅色標記
    * ⬛ **障礙物 (Obstacles)**：灰色標記，數量固定為 $n - 2$ 個。
* **策略與價值評估 (Policy & Value Iteration)**：
    * **Value Matrix (價值矩陣)**：顯示每個狀態 $V(s)$ 的收斂數值，越靠近終點扣分越少。
    * **Policy Matrix (策略矩陣)**：根據最大化價值推導出最佳策略，以箭頭（↑, →, ↓, ←）視覺化顯示走向終點的最佳路徑。

## 🛠️ 技術棧 (Tech Stack)

* **前端**：HTML, CSS, Vanilla JavaScript
* **後端**：Python, Flask
* **演算法**：貝爾曼最佳方程式 (Bellman Optimality Equation), Value Iteration

## 🚀 如何在本地端執行 (How to Run)

1.  **確保已安裝 Python 3**。
2.  **安裝 Flask 套件**：
    ```bash
    pip install flask
    ```
3.  **啟動伺服器**：
    在專案根目錄下執行以下指令：
    ```bash
    python app.py
    ```
4.  **開啟網頁**：
    在瀏覽器輸入 `http://127.0.0.1:5000/` 即可開始使用。

## 📝 演算法參數設定
* 每步獎勵 (Step Reward): `-1`
* 折扣因子 ($\gamma$): `0.9`
* 收斂門檻 ($\theta$): `1e-4`